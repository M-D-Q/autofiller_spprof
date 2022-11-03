import json
import csv

def email_split(email):
    id1 = email.split("@")
    id=id1[0].split("+")
    id2=id[1]
    return str(id2)

def write_json(new_data, filename):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		# Join new_data with file_data inside emp_details
		file_data["comptes"].append(new_data)
		# Sets file's current position at offset.
		file.seek(0)
		# convert back to json.
		json.dump(file_data, file, indent = 4)


#get CSV info per line
def get_stuff_from_csv(filename) :
	with open (filename, mode='r') as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		data=list(reader)
	print(data)
