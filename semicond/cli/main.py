import click

from semicond import __version__

from datetime import datetime, timedelta

@click.option("--hours", "-h", default = 0, type = click.FLOAT, help = "Number of hours to forward")
@click.option("--days", "-d", default = 0, type = click.FLOAT, help = "Number of days to forward")
@click.option("--weeks", "-w", default = 0, type = click.FLOAT, help = "Number of weeks to forward")
@click.command()
def forward(**kwargs):
    """Forward time by a specified amount from now onwards."""
    fd = datetime.now() + timedelta(**kwargs)
    click.echo(f"Forwarded time: {fd.strftime('%Y-%m-%d %H:%M')}")

@click.version_option(__version__)
@click.group(commands = {
    "forward": forward,
})
def main():
    """Semicond CLI"""

