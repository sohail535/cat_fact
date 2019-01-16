from . import __version__

import click
import requests

from cat_fact.client import CatClient

cat_client = CatClient(requests.Session(), "http://cat-fact.herokuapp.com")



@click.command()
@click.version_option(version=__version__)
def cli(verbose=False):
    random_fact = cat_client.get_random_fact()
    if not random_fact:
        click.echo("Unable to get cat facts at the moment :'(")
    else:
        click.echo(random_fact["text"])


