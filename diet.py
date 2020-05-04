''' File: diet.py
    Author: Orlando Rodriguez
    Purpose: 
'''
import os, sys
import csv
from entry import make_entries, Entry
from diet_lims import Lim
import argparse

module_name = "DietTracker: Track nutrition and make better choices"
__version__ = "0.1"    

# def write_report():
    
def main():
    parser = argparse.ArgumentParser(description = f"{module_name} (Version {__version__})")
    parser.add_argument('age', 
                            metavar = 'AGE', type=int,
                            help='User age')
    parser.add_argument('sex', 
                            metavar = 'SEX', type=str,
                            help='User sex')
    parser.add_argument('dataset_file_name', 
                            metavar = 'DATASET_FILE_NAME', type=str,
                            help='Input file that information will be read from')
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
    
    lines = []
    macro_sums = [0, 0, 0, 0]
    datasets = 'datasets/'
    dataset_file_name = args.dataset_file_name + '.csv'
    
    if args.verbose:
        print("Reading from file " + dataset_file_name)
    
    with open(datasets + dataset_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            for i in range(1, 5):
                macro_sums[i - 1] += int(line[i])
            lines.append(line)
    
    if args.verbose:
        print("Macro sums: " + str(macro_sums))
    
    entries = make_entries(lines)
    limit = Lim(args.age, args.sex)
    
    if not args.quiet:
        print("Entries: ")
        for entry in entries:
            print(entry)
        print("Limit: " + str(limit.get_lims()))
    
    outputs = 'outputs/'
    output_file_name = args.dataset_file_name + '_output.txt'
    
    f = open(outputs + output_file_name, 'w')
    f.write("This should be working")
    f.close()

if __name__ == "__main__":
    main()