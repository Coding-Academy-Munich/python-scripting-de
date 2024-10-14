import click
import time
import tempfile
import os
import sqlite3

DB_FILE = 'tasks.db'

def get_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.execute('''CREATE TABLE IF NOT EXISTS tasks
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
    db.commit()

@click.group()
def cli():
    """Simple Task Manager"""
    init_db()

@cli.command()
@click.argument('task')
def add(task):
    """Add a new task"""
    db = get_db()
    db.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    db.commit()
    click.secho(f"Added task: {task}", fg="green")

@cli.command()
def list():
    """List all tasks"""
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks').fetchall()
    if not tasks:
        click.secho("No tasks found.", fg="yellow")
    else:
        for task in tasks:
            click.secho(f"{task['id']}. {task['task']}", fg="blue")

@cli.command()
def process():
    """Simulate processing tasks"""
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks').fetchall()
    if not tasks:
        click.secho("No tasks to process.", fg="yellow")
        return

    with click.progressbar(tasks, label="Processing tasks") as bar:
        for task in bar:
            # Simulate some work
            time.sleep(0.5)

    click.secho("All tasks processed!", fg="green")

@cli.command()
@click.argument('task_id', type=int)
def edit(task_id):
    """Edit a task using an external editor"""
    db = get_db()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()

    if not task:
        click.secho("Invalid task ID.", fg="red")
        return

    # Create a temporary file with the task content
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as tf:
        tf.write(task['task'])
        tf.flush()
        tmp_filename = tf.name

    # Open the editor and wait for it to close
    click.edit(filename=tmp_filename)

    # Read the possibly edited content
    with open(tmp_filename, 'r') as tf:
        edited_task = tf.read().strip()

    # Remove the temporary file
    os.unlink(tmp_filename)

    # Check if the task was changed
    if edited_task and edited_task != task['task']:
        db.execute('UPDATE tasks SET task = ? WHERE id = ?', (edited_task, task_id))
        db.commit()
        click.secho(f"Task updated: {edited_task}", fg="green")
    else:
        click.secho("Task not changed.", fg="yellow")

@cli.command()
@click.argument('task_id', type=int)
def remove(task_id):
    """Remove a task"""
    db = get_db()
    task = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()

    if not task:
        click.secho("Invalid task ID.", fg="red")
        return

    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
    click.secho(f"Removed task: {task['task']}", fg="green")

if __name__ == '__main__':
    cli()
