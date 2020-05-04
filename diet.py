''' File: diet.py
    Author: Orlando Rodriguez
    Purpose: 
'''
import os, sys
import csv
import entry
import diet_lims
import argparse

module_name = "DietTracker: Track nutrition and make better choices"
__version__ = "0.1"    
    
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
    with open(datasets + dataset_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            for i in range(1, 4):
                macro_sums[i] += int(line[i])
            lines.append(line)
    
    entries = entry.make_entries(lines)
    limit = diet_lims.Lim(args.age, args.sex)
    
    outputs = 'outputs/'
    output_file_name = args.dataset_file_name + '_output.txt'
    
    f = open(outputs + output_file_name, 'w')
    f.write("This should be working")
    f.close()

if __name__ == "__main__":
    main()