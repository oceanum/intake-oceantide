"""Console script for intake_oceantide."""
import intake_oceantide

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for intake_oceantide."""
    console.print("Replace this message by putting your code into "
               "intake_oceantide.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
