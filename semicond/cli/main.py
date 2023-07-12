import click

from semicond import __version__

from datetime import datetime, timedelta

@click.option("--fmt", "-f", type = click.Choice(["hours", "days", "years"]), help = "Output time units", default = "years")
@click.command()
def powerlaw(fmt):
    """Accelerate time using power law formula."""
    top = click.prompt("Operation voltage (V)", type = click.FLOAT)
    tst = click.prompt("Stress voltage (V)", type = click.FLOAT)
    m = click.prompt("Power law exponent", type = click.FLOAT)
    tim = click.prompt("Time (hours)", type = click.FLOAT)

    from semicond.utils.formulas import apply_power_law
    acc_time = apply_power_law(m, top, tst, tim)
    if fmt == "days":
        acc_time /= 24
    elif fmt == "years":
        acc_time /= (365 * 24)
    click.echo("Accelerated time ({}): {}".format(fmt, acc_time))

@click.option("--fmt", "-f", type = click.Choice(["hours", "days", "years"]), help = "Output time units", default = "years")
@click.command()
def arrhenius(fmt):
    """Accelerate time using Arrhenius formula."""
    top = click.prompt("Operation temperature (°C)", type = click.FLOAT)
    tst = click.prompt("Stress temperature (°C)", type = click.FLOAT)
    ea = click.prompt("Activation energy (eV)", type = click.FLOAT)
    tim = click.prompt("Time (hours)", type = click.FLOAT)

    from semicond.utils.formulas import apply_arrhenius
    acc_time = apply_arrhenius(ea, top, tst, tim)
    if fmt == "days":
        acc_time /= 24
    elif fmt == "years":
        acc_time /= (365 * 24)
    click.echo("Accelerated time ({}): {}".format(fmt, acc_time))

@click.group(commands = {
    "arrhenius": arrhenius,
    "powerlaw": powerlaw,
})
def accelerate():
    """Accelerate time using reliability formulas."""
    pass

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
    "accelerate": accelerate,
})
def main():
    """Semicond CLI"""
    pass

