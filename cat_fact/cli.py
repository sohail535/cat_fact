from . import __version__

import click


@click.group()
@click.version_option(version=__version__)
def cli(verbose=False):
    pass


@cli.command()
def fact():
    print "this is supposed to be a fact"

