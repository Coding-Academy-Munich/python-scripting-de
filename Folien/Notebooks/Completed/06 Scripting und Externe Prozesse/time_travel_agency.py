import click
import datetime

@click.command()
@click.argument('destination', type=click.Choice(['past', 'future']))
@click.option('--years', default=1, show_default=True, help='Number of years to travel')
@click.option('--return-trip/--one-way', default=True, help='Whether to book a return trip')
@click.option('--verbose', is_flag=True, help='Print verbose output')
def time_travel(destination, years, return_trip, verbose):
    """Book your next time travel adventure!"""
    current_year = datetime.datetime.now().year
    travel_year = current_year + years if destination == 'future' else current_year - years

    if verbose:
        click.echo(f"Preparing time machine...")
        click.echo(f"Calculating temporal coordinates...")

    click.echo(f"Booking your trip to the {destination}!")
    click.echo(f"You will arrive in the year {travel_year}.")

    if return_trip:
        click.echo("Round-trip booked. Don't forget your return ticket!")
    else:
        click.echo("One-way trip booked. Enjoy your new timeline!")

    if verbose:
        click.echo("Time jump completed successfully!")

if __name__ == '__main__':
    time_travel()
