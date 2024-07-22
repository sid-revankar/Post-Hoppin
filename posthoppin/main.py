import typer
from typing import Optional

from posthoppin import __app_name__, __version__

app = typer.Typer()

def version_callback(value: bool) -> None:
    if value:
        app_name_version = {
            "name": typer.style(__app_name__,fg=typer.colors.BRIGHT_YELLOW),
            "version": typer.style(__version__,fg=typer.colors.BRIGHT_GREEN),
        }
        typer.echo(f"{app_name_version['name']} {app_name_version['version']}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's name and version then exit.",
        callback=version_callback,
        is_eager=True,
    )
) -> None:
    return

if __name__ == '__main__':
    typer.run(main)