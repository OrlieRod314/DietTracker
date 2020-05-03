import argparse

parser = argparse.ArgumentParser(description = 'DietTracker: Track Nutrition and make better decisions')
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
                        action='version',  version=version_string,
                        help='Display version information and dependencies.')
detail = parser.add_mutually_exclusive_group()
detail.add_argument('-q', '--quiet',
                        action='store_true', 
                        help='Print quiet')
detail.add_argument('-v', '--verbose',
                        action='store_true', 
                        help='Print verbose')
args = parser.parse_args()