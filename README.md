# DietTracker
Python program that tracks nutritional information and offers suggestions for an improved diet.


## Installation
**NOTE**: Python 3.6 or higher is required
```bash
# clone the repo
$ git clone https://github.com/OrlieRod314/DietTracker.git

# change the working directory to DietTracker
$ cd DietTracker

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```
## Usage

```
$ python3 diet.py --help
usage: diet.py [--kg] [--help] [--csv][--version] FILE_NAME[file]

DietTracker: Track Nutrition and make more 

positional arguments:
  FILE_NAME         Input file to which information will be saved

optional arguments:
  --help            Show this help message and exit
  --kg              Offers recommendation based on ketogenic diet
  --version         Display version information and dependencies.
  --csv             Create Comma-Separated Values (CSV) File.
  ```
