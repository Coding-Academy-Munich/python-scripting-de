import click
import json
from pathlib import Path

DEFAULT_FILE = 'superheroes.json'

class SuperheroTeam:
    def __init__(self):
        self.heroes = {}

    def add_hero(self, name, power):
        self.heroes[name] = power

    def remove_hero(self, name):
        return self.heroes.pop(name, None)

    def list_heroes(self):
        return self.heroes

    def save_to_file(self, file_path):
        with file_path.open('w') as f:
            json.dump(self.heroes, f)

    def load_from_file(self, file_path):
        if file_path.exists():
            with file_path.open('r') as f:
                self.heroes = json.load(f)
        else:
            self.heroes = {}

@click.group()
@click.option('--file', type=click.Path(path_type=Path), default=DEFAULT_FILE,
              help=f'JSON file to store heroes (default: {DEFAULT_FILE})')
@click.pass_context
def superhero(ctx, file):
    """Manage your superhero team!"""
    ctx.ensure_object(dict)
    team = SuperheroTeam()
    team.load_from_file(file)
    ctx.obj['team'] = team
    ctx.obj['file'] = file

@superhero.command()
@click.argument('name')
@click.option('--power', default='Flying', help='Superhero\'s power')
@click.pass_context
def add(ctx, name, power):
    """Add a new superhero to your team."""
    team = ctx.obj['team']
    team.add_hero(name, power)
    click.echo(f"Added {name} with {power} power to your team!")
    team.save_to_file(ctx.obj['file'])

@superhero.command()
@click.argument('name')
@click.pass_context
def remove(ctx, name):
    """Remove a superhero from your team."""
    team = ctx.obj['team']
    if team.remove_hero(name):
        click.echo(f"Removed {name} from your team. Goodbye, hero!")
    else:
        click.echo(f"Hero {name} not found in your team.")
    team.save_to_file(ctx.obj['file'])

@superhero.command()
@click.pass_context
def list(ctx):
    """List all superheroes in your team."""
    team = ctx.obj['team']
    heroes = team.list_heroes()
    if heroes:
        click.echo("Your current team:")
        for i, (name, power) in enumerate(heroes.items(), 1):
            click.echo(f"{i}. {name} (Power: {power})")
    else:
        click.echo("Your team is empty. Add some heroes!")

if __name__ == '__main__':
    superhero()
