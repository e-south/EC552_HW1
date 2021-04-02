import json
import math
import copy
import gc

# Secondly generate a bunch of new input json files with more narrow range of coefficients to change parameter values in each input sensor
def optimization(data, name1, name2, promoter, rbs):
    d = copy.deepcopy(data)
    for x_p in range(len(promoter)):
        for x_r in range(len(rbs)):
            for i in range(len(data)):
                if data[i]['collection'] == name1:
                    for j in range(len(data[i][name2])):
                        if data[i][name2][j]['name'] == 'ymax' or data[i][name2][j]['name'] == 'ymin':
                            range1 = math.pow(2,promoter[x_p])
                            data[i][name2][j]['value'] *= range1
                        if data[i][name2][j]['name'] == 'beta':
                            range1 = math.pow(2, rbs[x_r])
                            data[i][name2][j]['value'] /= range1
            output_json(f"{in_dir}/input_range/{chassis}.input.range_p+{promoter[x_p]}_0.5_r+{rbs[x_r]}_0.5.json", data)
            del data
            gc.collect()
            data = copy.deepcopy(d)

def input_json(input_path):
    file = open(input_path, "r")
    content = file.read()
    data = json.loads(content)

    promoter = [-1, -0.5, 0, 0.5, 1]
    rbs = [5, 5.5, 6, 6.5, 7]
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
for chassis in chassis_name:
    input_json(f"{in_dir}/{chassis}.input.json")

