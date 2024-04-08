from pathlib import Path

import typer

from .models import Wav


wav_app = typer.Typer(name="wav", short_help="Tool for working with .wav format")
wav_app.info.help = """
The WAV files found within the game directory are not typical waveform audio files.
They utilize a proprietary format developed by InnerLoop.
This format supports four different audio compression methods:
Currently, the tool is capable of processing only the first two compression methods.

* SOUND_PACK_METHOD_RAW = 0

* SOUND_PACK_METHOD_RAW_RESIDENT = 1

* SOUND_PACK_METHOD_ADPCM = 2

* SOUND_PACK_METHOD_ADPCM_RESIDENT = 3
"""


@wav_app.command()
def convert(source: Path, target: Path):
    """
    Convert single file to waveform (regular wav audio file supported by almost anyone).
    """

    wav = Wav.from_file(source)
    wav.to_waveform(target)


@wav_app.command()
def convert_directory(source_dir: Path, target_dir: Path):
    """
    Walking a directory recursively and convert every *.wav file.
    Target file will be saved with same tree but in the target directory.
    """

    for source_path in source_dir.glob("**/*.wav"):
        target_path = target_dir.joinpath(source_path.relative_to(source_dir))

        wav = Wav.from_file(source_path)
        wav.to_waveform(target_path)

        print(wav.sound_pack_method, target_path)
