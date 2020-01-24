
"""
Methods for loading and wirting for data serialization
"""

############################## csv ##############################

# read file
import csv

with open('/path/file.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#  write to file
import csv

with open('/path/file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(iterable)

############################## json ##############################

# Reading JSON content from a file
import json

with open('/path/file.json', 'r') as f:
    data = json.load(f)

############################## pickle ##############################

# serialization
import pickle

data = {'A': 1, 'B': 2, 'C': 3}
fw = open('dataFile.pkl','wb')
# Use dumps to convert the object to a serialized string
# Use dump to dumps + write to stream write stream
serial_data = pickle.dump(data, fw)
fw.close()

fr = open('dataFile.pkl','rb')
# Use loads to de-serialize an object
# Use load to load a file stream
received_data = pickle.load(fr)
fr.close()
############################## xml ##############################

# loal file
import xml.etree.ElementTree as ET

tree = ET.parse('/path/file.xml')
root = tree.getroot()

############################## yaml ##############################

# loal .yaml
import yaml
from pprint import pprint

with open('/path/file.yaml', 'r', newline='') as f:
    try:
        pprint(yaml.safe_load(f))
    except yaml.YAMLError as ymlexcp:
        pprint(ymlexcp)
