import json
import copy
import gc

# Firstly generate a bunch of new input json files with different coefficients to change parameter values in each input sensor
def optimization(data, name1, name2, promoter, rbs):
    d = copy.deepcopy(data)
    for x_p in promoter:
        for x_r in rbs:
            for i in range(len(data)):
                if data[i]['collection'] == name1:
                    for j in range(len(data[i][name2])):
                        if data[i][name2][j]['name'] == 'ymax' or data[i][name2][j]['name'] == 'ymin':
                            data[i][name2][j]['value'] *= x_p
                        if data[i][name2][j]['name'] == 'beta':
                            data[i][name2][j]['value'] /= x_r
            output_json(f"{in_dir}/input_modified/{chassis}.input.new_p+{x_p}_r+{x_r}.json", data)
            del data
            gc.collect()
            data = copy.deepcopy(d)

# Read input json file and use a list of promoter and rbs to change parameter values of different input sensors
def input_json(input_path):
    file = open(input_path, "r")
    content = file.read()
    data = json.loads(content)
    print(data)
    promoter = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    rbs = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    optimization(data, "models", "parameters", promoter, rbs)
    file.close()

# Write data into new json file with modified values in input sensors
def output_json(out_path, new_dict):
    f = open(out_path, "w")
    json.dump(new_dict,f,indent=4)
    f.close()

# Set our directory variables.
in_dir = 'cello/input'
out_dir = 'cello/output'
chassis_name = ['Eco1C1G1T1', 'Eco1C2G2T2', 'Eco2C1G3T1']
for chassis in chassis_name:
    input_json(f"{in_dir}/{chassis}.input.json")

