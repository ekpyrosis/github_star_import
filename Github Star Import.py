import click

@click.group()
def github_star_import():
    pass

@github_star_import.command()
def cmd1():
    '''Command on github_star_import'''
    click.echo('github_star_import cmd1')

@github_star_import.command()
def cmd2():
    '''Command on github_star_import'''
    click.echo('github_star_import cmd2')

if __name__ == '__main__':
    github_star_import()
