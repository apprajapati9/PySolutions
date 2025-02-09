import os
import sys
import pandas as pd

#pd.set_option('display.max_columns', None)
pd.set_option('display.encoding', 'utf-8')
print(sys.getdefaultencoding())

entries = os.listdir('./files/')


file_path = os.path.dirname(os.path.abspath(__file__))

file_path += "\\files\\{}".format(entries[0])

print("File path: ", file_path)

# xls_file = pd.ExcelFile(file_path, engine='openpyxl')

data_file = pd.read_html(file_path, flavor='lxml', encoding ='utf-8')

#pd.set_option('display.max_columns', None) 

for i, table in enumerate(data_file):
    print(f"Table {i}:")
    print(table)
    print("\n")

output_file = "output.txt"

data_file[0].map(lambda x: str(x).replace('\u25bc', ''))

data_file[0].to_csv(output_file, sep = '\t', index= False, header = False, encoding='utf-8')

print(data_file[0].head())
