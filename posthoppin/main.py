"""
Command-line interface for the Post-Hoppin application.

This module provides a CLI for managing dotfiles, allowing users to copy
directories or individual files to their .config directory.

Dependencies:
    typer, os, pathlib, rich, typing, typing_extensions, backend, config
"""

import typer
import os
from pathlib import Path
from rich import print as rprint
from rich import print as show
from rich.prompt import Prompt
from typing import Optional
from typing_extensions import Annotated
from backend import FileHandling
import config

app = typer.Typer()

def version(value: bool) -> None:
    """
    Display the application version and exit.

    Args:
        value (bool): Flag to trigger version display.
    """
    if value:
        ver_name = {
            "name": config.NAME,
            "version": config.version,
        }
        show(
            f":rabbit: [bold magenta1]{ver_name['name']}[/bold magenta1] [green]v{ver_name['version']}[/green]"
        )
        raise typer.Exit()

def path_option():
    """Prompt the user to input a path."""
    
    get_userPath = input("Please provide the path here: ")
    return get_userPath

def list_option():
    """
    Display a list of dotfiles and prompt user to select one.

    Returns:
        Optional[str]: The selected file/directory path or None if user quits.
    """
    
    home = Path(os.environ["HOME"], "cli project")
    if home.is_dir():
        dotfiles_path = home / "dotfiles"
        if dotfiles_path.is_dir():
            entries = list(os.scandir(dotfiles_path))

            # Display entries with numbers
            for i, entry in enumerate(entries, 1):
                icon = ":file_folder:" if entry.is_dir() else ":page_facing_up:"
                rprint(f"{i}. {icon} [green]{entry.name}[/green]")

                # Print a newline after every 3 entries
                if i % 3 == 0:
                    rprint()

            # Prompt user for selection
            while True:
                selection = Prompt.ask(
                    "Enter the number of your selection (or 'q' to quit)"
                )

                if selection.lower() == "q":
                    return None

                try:
                    index = int(selection) - 1
                    if 0 <= index < len(entries):
                        selected_entry = entries[index]
                        return selected_entry.path
                    else:
                        rprint("[red]Invalid selection. Please try again.[/red]")
                except ValueError:
                    rprint(
                        "[red]Invalid input. Please enter a number or 'q' to quit.[/red]"
                    )

@app.callback()
def main(
    start: Annotated[Optional[str], typer.Argument()] = None,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Shows Version",
        callback=version,
        is_eager=True,
    ),
):
    """
    Main function for the Post-Hoppin CLI.

    Run by typing 'posthoppin'.
    """
    try:
        def choose_option(s):
            """
            Present options to the user and handle their choice.

            Args:
                s (str): The start argument passed to the CLI.

            Returns:
                Optional[str]: The selected path or None.
            """
            
            if s == 'posthoppin':
                show(
                    f":rabbit: [bold cyan]Post-Hoppin \n [/bold cyan][bold magenta1]1. Copy directory\n 2. Single directory/files[/bold magenta1]"
                )
                option = int(typer.prompt(typer.style("User Choice ",typer.colors.BRIGHT_GREEN)))
                match option:
                    case 1:
                        return path_option()
                    case 2:
                        return list_option()
            else:
                typer.echo("Are you sure?... try '--help' ")
                raise typer.Abort()
            
        user_option = choose_option(start)
        basename = os.path.basename(user_option)
        
        if basename == 'dotfiles':
            # Handle entire dotfiles directory
            file_handle = FileHandling(user_option)
            folders_path = file_handle.getPath()
            path_dir_list = file_handle.getSubDir(folders_path)
            path_file_list = file_handle.getSubDir_file(folders_path)
            file_handle.putFiles(path_dir_list, path_file_list)
        else:
            # Handle single file or directory
            m_file_handle = FileHandling(None)
            m_file_handle.putSingleDir(user_option)
            m_file_handle.putSingleFiles(user_option)
            
    
    except Exception as e:
        typer.echo(e)

if __name__ == "__main__":
    typer.run(main)
