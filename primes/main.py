import click

@click.command()
@click.option("--name", default="World", help="Name to greet.")
def main(name: str):
    """Greet the user by name."""
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    main()
