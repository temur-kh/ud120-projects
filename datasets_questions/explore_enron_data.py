#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = dict(pickle.load(open("../final_project/final_project_dataset.pkl", "r")))
# print enron_data.keys()
names = []
with open("../final_project/poi_names.txt", "r") as file:
    lines = file.readlines()
    for i in range(2, len(lines)):
        name = lines[i].split(')')[1].strip().replace(',', '').upper()
        names.append(name)

for key in enron_data:
    if key.startswith('Prentice James'.upper()):
        print enron_data[key]['total_stock_value']
