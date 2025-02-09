import os
import sys
import pandas as pd
from bs4 import BeautifulSoup

#pd.set_option('display.max_columns', None)
pd.set_option('display.encoding', 'utf-8')
print(sys.getdefaultencoding())

entries = os.listdir('./files/')


file_path = os.path.dirname(os.path.abspath(__file__))

files = []

for i in entries:
    path = file_path + "\\files\\{}".format(i)
    files.append(path)
    print(path)


# xls_file = pd.ExcelFile(files[0], engine='openpyxl')

data_file = pd.read_html(files[0], flavor='lxml', encoding ='utf-8', header=1, keep_default_na=True) #header=1 property one removes the 0th column that has no meaningful header for data.

#pd.set_option('display.max_columns', None) 

output_file = "output.txt"

#data_file[0].map(lambda x: str(x).replace('\u25bc', ''))

# for i, table in enumerate(data_file):
#     print(f"Table {i}:")
#     print(table)
#     print("\n")

data_file[0].to_csv(output_file, sep = '\t', index= False, header = True, encoding='utf-8')

#data = data_file[0].astype(str)

#data.to_string(output_file, index= False, header = True, encoding='utf-8')


#print(data_file[0].columns.tolist())
