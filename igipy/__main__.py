from typer import Typer

from .thm.apps import thm_app


app = Typer(
    short_help="Convert and decompile Project IGI and Project IGI 2 fileformats",
    help="Here should be long description...",
    add_completion=False
)

app.add_typer(thm_app)


if __name__ == "__main__":
    app()
