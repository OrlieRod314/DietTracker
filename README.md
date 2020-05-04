# DietTracker
Python program that tracks nutritional information and offers suggestions for an improved diet.

## Installation
```bash
# clone the repo
$ git clone https://github.com/OrlieRod314/DietTracker.git

# change the working directory to DietTracker
$ cd DietTracker

# install the requirements
$ python -m pip install -r requirements.txt
```
## Folder Structure
```bash
.
├── datasets
└── outputs
```
## Input Layout
Input file should be .csv with each food item entered on a row.
File must be in dataset directory.
Attributes should be entered accordingly:

<table>
    <tr>
        <th>Name</th>
        <th>Calories</th>
        <th>Carbohydrates</th>
        <th>Protein</th>
        <th>Fat</th>
    </tr>
</table>
Macro nutrients are in grams

## Output
Output file is automatically created using name of input file.
File is created inside output directory.
## Usage
```
$ python diet.py --help

usage: 
diet.py [-h] [-kg] [-docx] [-ver] [-nocol] [-q | -v] AGE SEX DATASET_FILE_NAME

DietTracker: Track nutrition and make better choices (Version 1.0)

positional arguments:
  AGE                User age
  SEX                User sex
  DATASET_FILE_NAME  Input file that information will be read from

optional arguments:
  -h, --help         show this help message and exit
  -kg, --ketogenic   Offers recommendation based on ketogenic diet
  -docx, --word      Writes report to .docx file instead of .txt
  -ver, --version    Display version information and dependencies.
  -nocol, --nocolor  Disables color in terminal
  -q, --quiet        Print quiet
  -v, --verbose      Print verbose
  ```
### Examples
```
$ python diet.py -v 19 m orell
$ python diet.py -q -docx 18 f kat
```
## Team
Original Creator - <a href= "https://github.com/OrlieRod314">Orlando Rodriguez</a>