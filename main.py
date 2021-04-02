from itertools import combinations
from celloapi2 import CelloQuery, CelloResult
import json
import math
import copy
import re
import csv

# Change parameter values in different input sensors
def value_change(data, i, name2, rbs, promoter, flag=0):
    # flag = 0: promtor and rbs are both calculate coefficients
    # flag = 1: ymax, ymin and beta should be set as the arguments value we put in
    # flag = 2: ymax, ymin should be set as the arguments value we put in, but rbs is still a calculate coefficient
    if flag != 0:
        for j in range(len(data[i][name2])):
            if data[i][name2][j]['name'] == 'ymax':
                data[i][name2][j]['value'] = promoter[0]
            if data[i][name2][j]['name'] == 'ymin':
                data[i][name2][j]['value'] = promoter[1]
            if flag == 1:
                if data[i][name2][j]['name'] == 'beta':
                    data[i][name2][j]['value'] = rbs
            else:
                if data[i][name2][j]['name'] == 'beta':
                    range1 = math.pow(2, rbs)
                    data[i][name2][j]['value'] /= range1
    else:
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
        # score is a variable saving the highest score so far for the current input sensor.
        # We don't need to compare more if score > e[0], because that won't help use get parameter values provide higher score.
        if score > e[0]: continue

        # pair1 in the current line of table is the same as name we want to check.
        if (e[2] == name):
            if e[3] in name_list:
                promoter = [float(e[5]), float(e[6])]
                # if length of e > 9, we know the rbs value can be used here. Otherwise, we only have ymax and ymin value to be directly used here
                if len(e) > 9:
                    value_change(data, i, name2, float(e[10]), promoter, 1)
                else:
                    candidate = re.split('\+|_',e[1])
                    rbs = float(candidate[5])
                    value_change(data, i, name2, rbs, promoter, 2)
                flag = 1
                score = e[0]
                continue

        # pair2 in the current line of table is the same as name we want to check.
        if (e[3] == name):
            if e[2] in name_list:
                promoter = [float(e[7]), float(e[8])]
                if len(e) > 9:
                    value_change(data, i, name2, float(e[12]), promoter, 1)
                else:
                    candidate = re.split('\+|_',e[1])
                    rbs = float(candidate[5])
                    value_change(data, i, name2, rbs, promoter, 2)
                flag = 1
                score = e[0]
                continue
    return flag

# Generate a new input file by changing parameter values in each input sensor
def optimization(data, name1, name2, promoter, rbs, name_list, refer_table):
    d = copy.deepcopy(data)
    for i in range(len(data)):
        if data[i]['collection'] == name1:
            if search_table(data, i, name2, refer_table, name_list) == 1: continue
            value_change(data, i, name2, rbs, promoter)
    output_json(f"{in_dir}/{chassis}.input.new.json", data)

# Get name list of all input sensors in the test input json file
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
    # Default coefficient analyzed from a bunch of json files with different coefficients.
    promoter = 0.75
    rbs = 6
    name_list = get_name(data)
    optimization(data, "models", "parameters", promoter, rbs, name_list, refer_table)
    file.close()

def output_json(out_path, new_dict):
    f = open(out_path, "w")
    json.dump(new_dict,f,indent=4)
    f.close()

# Read reference table into a list from reference_table.csv file
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
in_dir = '/cello/input'
out_dir = '/cello/output'
v_file = 'and.v'
options = 'options.csv'
# Calculate number of inputs into the Circuit.
signal_input = 2
chassis_name = ['Eco1C1G1T1', 'Eco1C2G2T2', 'Eco2C1G3T1']

refer_table = read_lookup_table('cello/input/reference_table.csv')
for chassis in chassis_name:
    input_json(f"{in_dir}/{chassis}.input.json", refer_table)

best_score = 0
best_chassis = None
best_input_signals = None
for chassis in chassis_name:
    in_ucf = f'{chassis}.UCF.json'
    input_sensor_file = f'{chassis}.input.new.json'
    output_device_file = f'{chassis}.output.json'
    q = CelloQuery(
        input_directory=in_dir,
        output_directory=out_dir,
        verilog_file=v_file,
        compiler_options=options,
        input_ucf=in_ucf,
        logging=False,
        input_sensors=input_sensor_file,
        output_device=output_device_file,
    )
    signals = q.get_input_signals()
    signal_pairing = list(combinations(signals, signal_input))
    for signal_set in signal_pairing:
        signal_set = list(signal_set)
        q.set_input_signals(signal_set)
        # a string for corresponding input filename, specially for scripting and generating programmatic inputs for HW
        q.get_results()
        try:
            res = CelloResult(results_dir=out_dir)
            if res.circuit_score > best_score:
                best_score = res.circuit_score
                best_chassis = chassis
                best_input_signals = signal_set
        except:
            pass
        q.reset_input_signals()
    print('-----')
print(f'Best Score: {best_score}')
print(f'Best Chassis: {best_chassis}')
print(f'Best Input Signals: {best_input_signals}')