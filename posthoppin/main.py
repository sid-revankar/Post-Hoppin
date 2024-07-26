import typer
from view import View

def main():
    myView = View()
    myView.fileInput()
if __name__ == '__main__':
    typer.run(main)