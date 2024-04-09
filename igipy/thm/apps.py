import json
from pathlib import Path

import typer

from .models import Thm

thm_app = typer.Typer(name="thm", short_help="Tool for working with .thm format")
thm_app.info.help = """
Original .thm files include heightmaps required for constructing terrain geometry.
These files feature a 52-byte header followed by a list of levels of detail (LODs), 
typically one LOD sized at 128 x 128. 
Each LOD consists of a two-dimensional array of float32 numbers.
"""


@thm_app.command(short_help="Represent .thm file internals as JSON")
def convert_to_json(source: Path, indent: int = 2):
    print(Thm.from_file(source).to_json(indent=indent))


@thm_app.command(short_help="Convert .thm file into TIFF")
def convert_to_tiff(source: Path, target: Path):
    Thm.from_file(source).to_tiff(target)
