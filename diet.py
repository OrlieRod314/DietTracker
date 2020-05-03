''' File: diet.py
    Author: Orlando Rodriguez
    Purpose: 
'''
import csv
import diet_lims
import argparse

module_name = "DietTracker: Track nutrition and make better choices"
__version__ = "0.1"

'''
class entry:
    def __init__(name, cals, carbs, prot, fat, water):
        # calories, carbs, prot, fat, water
        self._name = name
        self._cals = cals
        self._carbs = carbs
        self._prot = prot
        self._fat = fat
        self._water = water
    def str():
        
'''
def make_entries():
    
def main():
    
    # Might want to add an arg for where they want deficits/surplus to be printed
    # Could be in cmd or text file
    
    # Could also have an arg for manual terminal input or spreadsheet input
    parser = argparse.ArgumentParser(description = f"{module_name} (Version {__version__})")
    parser.add_argument('age', 
                            metavar = 'AGE', required=True, type=int,
                            help='User age')
    parser.add_argument('sex', 
                            metavar = 'SEX', required=True, type=int,
                            help='User sex')
    parser.add_argument('file', 
                            metavar = 'FILE_NAME', required=True, type=str,
                            help='Input file to which information will be saved')
    parser.add_argument('-kg', '--ketogenic', 
                            action='store_true', dest='kg', default = False, 
                            help='Offers recommendation based on ketogenic diet')
    parser.add_argument('-ver', '--version',
                            action='version',  version=__version__,
                            help='Display version information and dependencies.')
    detail = parser.add_mutually_exclusive_group()
    detail.add_argument('-q', '--quiet',
                            action='store_true', 
                            help='Print quiet')
    detail.add_argument('-v', '--verbose',
                            action='store_true', 
                            help='Print verbose')
    args = parser.parse_args()
    
    with open('log.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        

if __name__ == "__main__":

    main()


