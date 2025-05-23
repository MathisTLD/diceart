from pathlib import Path
from typing import Optional
import typer

app = typer.Typer()


@app.command()
def convert(source: Path, output: Optional[Path] = None):
    img = convert(source)
    # use PNG to avoid compression
    save_path = output if output is not None else source.with_suffix(".diceart.png")
    img.save(save_path)
