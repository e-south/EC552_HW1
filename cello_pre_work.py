import json
import math
import copy
import gc
import re
import numpy as np
import csv

# Change parameter values in different input sensors
def value_change(data, i, name2, promoter, rbs):
    for j in range(len(data[i][name2])):
        if data[i][name2][j]['name'] == 'ymax' or data[i][name2][j]['name'] == 'ymin':
            range1 = math.pow(2, promoter)
            data[i][name2][j]['value'] *= range1
        if data[i][name2][j]['name'] == 'beta':
            range1 = math.pow(2, rbs)
            data[i][name2][j]['value'] /= range1

# Search the ith element of data in the refer table. If it exists in the table and the pair partner of it in the table also exist in name_list,
# we can use the coefficient of that pair in the refer table to change the parameter value of that input sensor.
def search_table(data, i, name2, refer_table, name_list):
    flag = 0
    score = 0
    name = data[i]['name'].split('_')[0]
    for e in refer_table:
        if score > e[0]: continue
        if (e[2] == name):
            if e[3] in name_list:
                candidate = re.split('\+|_',e[1])
                promoter = float(candidate[2])
                rbs = float(candidate[5])
                value_change(data, i, name2, promoter, rbs)
                continue
        if (e[3] == name):
            if e[2] in name_list:
                candidate = re.split('\+|_', e[1])
                promoter = float(candidate[2])
                rbs = float(candidate[5])
                value_change(data, i, name2, promoter, rbs)
    return flag

# Generate a new input file by changing parameter values in each input sensor
def optimization(data, name1, name2, promoter, rbs, name_list, refer_table):
    d = copy.deepcopy(data)
    for i in range(len(data)):
        if data[i]['collection'] == name1:
            if search_table(data, i, name2, refer_table, name_list) == 1: continue
            value_change(data, i, name2, promoter, rbs)
    output_json(f"{in_dir}/{chassis}.input.range_p_{promoter}_r_{rbs}.json", data)

# get name list of all input sensors in the test input json file
def get_name(data):
    name = []
    for i in range(len(data)):
        if data[i]['collection'] == "models":
            name.append(data[i]['name'].split('_')[0])
    return name

def input_json(input_path, refer_table):
    file = open(input_path, "r")
    content = file.read()
    data = json.loads(content)
    promoter = 0.5
    rbs = 6
    name_list = get_name(data)
    optimization(data, "models", "parameters", promoter, rbs, name_list, refer_table)
    file.close()

def output_json(out_path, new_dict):
    f = open(out_path, "w")
    json.dump(new_dict,f,indent=4)
    f.close()

# Read reference table in from reference_table.csv file
def read_lookup_table(path):
    table = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        index = 0
        for line in reader:
            if index == 0 or len(line[0]) == 0:
                index = 1
                continue
            element = []
            for i in range(len(line)):
                if i == 0: element.append(float(line[0]))
                else: element.append(line[i])
            table.append(element)
    return table

# Set our directory variables.
in_dir = 'cello/input'
out_dir = 'cello/output'
chassis_name = ['Eco1C1G1T1', 'Eco1C2G2T2', 'Eco2C1G3T1']
refer_table = read_lookup_table('cello/input/reference_table.csv')
for chassis in chassis_name:
    input_json(f"{in_dir}/{chassis}.input.json", refer_table)

