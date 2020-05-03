# DietTracker
Python program that tracks nutritional information and offers suggestions for an improved diet.

## Installation
```bash
# clone the repo
$ git clone https://github.com/OrlieRod314/DietTracker.git

# change the working directory to DietTracker
$ cd DietTracker
```
## Folder Structure
```bash
.
├── datasets
├── outputs
└── __pycache__
diet.py
diet_lims.py
entry.py
README.md
```
## Input Layout
Input file should be .csv with each food item entered on a row.
Attributes should be entered accordingly:
<p align=center>
Name    Calories    Carbohydrates   Protein     Fat
</p>

## Output
Output file is automatically created using name of input file.
File is created inside output directory.
## Usage
```
$ python diet.py -h 19 m orlando
usage: diet.py [-h] [-kg] [-ver] [-q | -v] AGE SEX DATASET_FILE_NAME

DietTracker: Track nutrition and make better choices (Version 0.1)

positional arguments:
  AGE                User age
  SEX                User sex
  DATASET_FILE_NAME  Input file that information will be read from

optional arguments:
  -h, --help         show this help message and exit
  -kg, --ketogenic   Offers recommendation based on ketogenic diet
  -ver, --version    Display version information and dependencies.
  -q, --quiet        Print quiet
  -v, --verbose      Print verbose
  ```
  ## Team
  Orlando Rodriguez