import argparse

#Argument to input a file with any name.
parser = argparse.ArgumentParser(description="ACME Company")
parser.add_argument('file',  help="File name with the employees time frame")
args = parser.parse_args()


#Function to read a file
def read_file(file):
    with open(file) as f:
        contents = f.readlines()
    return contents

#Function that present data with a format
def presentation(dictionary):
    print('Times that employees were at the same time.')
    for key in dictionary.keys():
        print('{key}: {value}'.format(key=key,value=dictionary[key]))