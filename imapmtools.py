import click

@click.command()
@click.option('--origin', help='Origin IMAP server')
@click.option('--destination', help='Destination IMAP server')
@click.option('--originusername', help='Origin login')
@click.option('--destinationusername', help='Destination login')
@click.option('--originpassword', help='Origin password')
@click.option('--destinationpassword', help='Origin password')
@click.option('--testconnection', default=False, help='Only test account login on booth server')
def run(origin, destination, originusername, destinationusername, originpassword, destinationpassword, testconnection):
    """Simple program that greets NAME for a total of COUNT times."""
    if testconnection:
        pass
    else:    
        click.secho('Starting migration: %s:%s ==> %s:%s' % (origin, originusername, destination, destinationusername), blink=True, bold=True, fg='green')
    
if __name__ == '__main__':
    run()