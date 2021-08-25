"""Console script for hexatron."""
import sys

import click

from hexatron.hexatron import to_hexadecimal
from hexatron.server import start_server


@click.group()
def main():
    """Console script for hexatron."""


@main.command()
@click.argument("number", type=int)
def convert(number):
    """ Convert integer to hexadecimal string """
    click.echo(to_hexadecimal(number))


@main.command()
@click.argument("port", type=int, default=8080)
def server(port):
    """ Run hexatron API """
    start_server(port)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
