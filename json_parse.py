import json
import math
import copy
import gc
import numpy as np

def optimization(data, name1, name2, promoter, rbs):

    # parameters = {'ymax':0, 'ymin':1, 'alpha':2, 'beta':3}
    d = copy.deepcopy(data)
    for x_p in promoter:
        for x_r in rbs:
            for i in range(len(data)):
                if data[i]['collection'] == name1:
                    for j in range(len(data[i][name2])):
                        # change values of each parameter
                        # index = parameters.get(data[i][name2][j]['name'], None)
                        if data[i][name2][j]['name'] == 'ymax' or data[i][name2][j]['name'] == 'ymin':
                            data[i][name2][j]['value'] *= x_p
                        if data[i][name2][j]['name'] == 'beta':
                            data[i][name2][j]['value'] /= x_r
            output_json(f"{in_dir}/input_modified/{chassis}.input.new_p+{x_p}_r+{x_r}.json", data)
            print(id(data), id(d))
            del data
            gc.collect()
            data = copy.deepcopy(d)

            print(id(data),id(d))


def input_json(input_path):
    file = open(input_path, "r")
    content = file.read()
    data = json.loads(content)
    print(data)
    promoter = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    rbs = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    optimization(data, "models", "parameters", promoter, rbs)
    file.close()


def output_json(out_path, new_dict):
    f = open(out_path, "w")
    json.dump(new_dict,f,indent=4)
    f.close()

# Set our directory variables.
in_dir = 'cello/input'
out_dir = 'cello/output'
chassis_name = ['Eco1C1G1T1', 'Eco1C2G2T2', 'Eco2C1G3T1']
# chassis_name = ['Eco1C1G1T1']
for chassis in chassis_name:
    input_json(f"{in_dir}/{chassis}.input.json")

