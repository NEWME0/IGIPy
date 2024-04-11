# IGIPy

**IGIPy** is a CLI (Command Line Interface) tool crafted for the purpose of converting game assets from "Project IGI" and "Project IGI 2" into widely recognized formats. \
This utility is essential for modders, developers, and enthusiasts looking to work with or analyze the game's internal resources.

## Documentation

The documentation for **IGIPy** is available in the https://igipy.readthedocs.io/.


## Getting Started with Installation

**IGIPy** is developed in Python, ensuring a seamless setup and execution process. To get started, follow the steps outlined below:

1. **Python Installation:** Ensure Python is installed on your system. \
Minimal required version is `python>=3.11`.

2. **Install Dependencies:** Install all necessary Python packages. \
Open your terminal or command prompt and navigate to the IGIPy directory. \
Execute the following command:

```bash
pip install -r requirements.txt
```

3. **Launching IGIPy:** with all dependencies in place, IGIPy is ready to use. \
You can access its features directly from your terminal. \
Start by checking out the help section to familiarize yourself with the available commands:

```bash
python -m igipy --help
```

You must see something like this:

```
(venv) PS D:\PycharmProjects\Strike> python -m igipy --help
Usage: python -m igipy [OPTIONS] COMMAND [ARGS]...

  Here should be long description...

Options:
  --help  Show this message and exit.

Commands:
  thm  Sub tool to work with .thm files
```

## Usage examples

#### List all handled formats

```bash
python -m igipy --help
```

Under section `Commands:` you'll see a list of all handled file formats right now.

#### List all available commands per format use:

```bash
python -m igipy thm --help
```

And again, under section `Commands:` you will se a list of available commands.

#### Show help text for an individual command:

```bash
python -m igipy thm convert-to-json --help
```

#### Convert THM file to JSON and Dump to Terminal
To convert a `.thm` file to JSON format and dump the output directly to the terminal, use the following command:

```bash
python -m igipy thm convert-to-json path/to/file.thm
```

Make sure to replace `path/to/file.thm` with the actual path to your `.thm` file.

#### Handling File Paths with Spaces
If your file path contains spaces, ensure to wrap the path in quotes to escape the empty spaces. \
Here is an example:

```bash
python -m igipy thm convert-to-json "D:\IGI 2 - Covert Strike\MISSIONS\location1\level1\heightmaps\heightmaps000.thm"
```

#### Dump Output to a File
If you prefer to dump the converted JSON output directly into a file instead of the terminal, you can redirect the output as shown below:

```
python -m igipy thm convert-to-json path/to/file.thm > path/to/output/file.json
```

Again, replace `path/to/file.thm` and `path/to/output/file.json` with the actual paths to your source `.thm` file and desired output `.json` file, respectively.
