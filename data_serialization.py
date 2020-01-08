
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

#Use dumps to convert the object to a serialized string
serial_data = pickle.dumps(data)

#Use loads to de-serialize an object
received_data = pickle.loads(data)

############################## xml ##############################

# loal file
import xml.etree.ElementTree as ET

tree = ET.parse('/path/file.xml')
root = tree.getroot()

############################## yaml ##############################

# loal .yaml
import yaml

with open('/path/file.yaml', 'r', newline='') as f:
    try:
        print(yaml.load(f))
    except yaml.YAMLError as ymlexcp:
        print(ymlexcp)
