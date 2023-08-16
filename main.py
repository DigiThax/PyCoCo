import os
import glob
from bs4 import BeautifulSoup

from pprint import pprint

# First implementation will have the script along side the report.
# After this matures in feature, parameter inputs for path will be made available
base_directory = os.getcwd() + '\\html'

# Find all index.html files
index_files = (glob.glob(os.path.join(base_directory, '**/index.html'), recursive=True))


for index_file in index_files:
    with open(index_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        pprint(soup)
        exit()