# IGIPy

**IGIPy** is a CLI (Command Line Interface) tool crafted for the purpose of converting game assets from "Project IGI" and "Project IGI 2" into widely recognized formats.

This utility is essential for modders, developers, and enthusiasts looking to work with or analyze the game's internal resources.

## Installation

Ensure Python is installed on your system. Minimal required version is `python>=3.11`.

Install `igipy` using pip:

```bash
pip install igipy
```

## Getting Started

Ensure `igipy` is installed on your system. You can access its features directly from your terminal.

```bash
igipy --help
```

## Usage examples

#### List all handled formats

```bash
igipy --help
```

Under section `Commands:` you'll see a list of all handled file formats right now.

#### List all available commands per format use:

```bash
igipy thm --help
```

And again, under section `Commands:` you will se a list of available commands.

#### Show help text for an individual command:

```bash
igipy thm convert-to-json --help
```

#### Convert THM file to JSON and dump to terminal

To convert a `.thm` file to JSON format and dump the output directly to the terminal, use the following command:

```bash
igipy thm convert-to-json path/to/file.thm
```

Make sure to replace `path/to/file.thm` with the actual path to your `.thm` file.

#### Handling File Paths with Spaces

If your file path contains spaces, ensure to wrap the path in quotes to escape the empty spaces:

```bash
igipy thm convert-to-json "D:\IGI 2 - Covert Strike\MISSIONS\location1\level1\heightmaps\heightmaps000.thm"
```

#### Dump Output to a File
If you prefer to dump the converted JSON output directly into a file instead of the terminal, you can redirect the output as shown below:

```bash
igipy thm convert-to-json path/to/file.thm > path/to/output/file.json
```

Again, replace `path/to/file.thm` and `path/to/output/file.json` with the actual paths to your source `.thm` file and desired output `.json` file, respectively.
