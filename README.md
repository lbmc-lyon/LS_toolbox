# LS_toolbox
A collection of tools for working with LS-DYNA and LS-PrePost.

## Installation
pip install LS_toolbox.\
Create environment variables named `LSDYNA_PATH` and `LSPREPOST_PATH` and set them to the paths of the LS-DYNA and LS-PrePost executables, respectively.\
To do this, open the terminal and type:\

For Windows:
```bash
setx LSDYNA_PATH "path\to\lsdyna\executable"
setx LSPREPOST_PATH "path\to\lsprepost\executable"
```
For Linux:
```bash
export LSDYNA_PATH="path/to/lsdyna/executable"
export LSPREPOST_PATH="path/to/lsprepost/executable"
```

## Usage
```python
import LS_toolbox as lst
```