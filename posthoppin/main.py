import typer
from rich import print as show
from typing import Optional
from backend import FileHandling
import config

app = typer.Typer()

def version(value: bool) -> None:
    if value:
        ver_name = {
            'name': config.NAME,
            'version': config.version,
        }
        show(
            f":rabbit: [bold magenta1]{ver_name['name']}[/bold magenta1] [green]v{ver_name['version']}[/green]"
        )
        raise typer.Exit()

@app.callback()
def main(
    greet: str,
    path: str = typer.Option("","--copy","-c", help='Copies the entire directory >> .config \n **NOTE: path should be in " " Quotes.'),
    version: Optional[bool] = typer.Option(None,"--version","-v",help="Shows Version",callback=version,is_eager=True,),
):
    """
    If you say "yo" it will greet!
    else executes normally.
    """
    user_path = path
    match greet:
        case "yo":
            show("[red]Hello User[/red] :ghost:")
        case _:
            pass
    file_handle = FileHandling(user_path)
    
    folders_path = file_handle.getPath()
    path_dir_list = file_handle.getSubDir(folders_path)
    path_file_list = file_handle.getSubDir_file(folders_path)

    file_handle.putFiles(path_dir_list,path_file_list)

if __name__ == "__main__":
    typer.run(main)
