import click
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
]

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def tell_joke(name):
    """This script tells a random joke to the user."""
    click.echo(f"Hello, {name}! Here's a joke for you:")
    click.echo(random.choice(jokes))

if __name__ == '__main__':
    tell_joke()
