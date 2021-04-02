import csv
import json

# Find the coefficients of the pair which has highest score. And save that info int a csv file.
def build_lookup_table(path, in_dir):
    table = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        index = 0
        for line in reader:
            if index == 0 or len(line[0]) == 0:
                index = 1
                continue
            element = []
            # stretch first five values: score, name include modificaiton_info, pair1, pair2, chassis
            for i in range(len(line)):
                if i == 0: element.append(float(line[0]))
                elif i == 2:
                    e = line[i].strip('[').strip(']').split("'")
                    element.append(e[1])
                    element.append(e[3])
                else: element.append(line[i])

            # Directly find the ymax, ymin, alpha, beta values in the json file.
            file = open(f"{in_dir}/input_range/{element[4]}.input.{element[1]}", "r")
            content = file.read()
            data = json.loads(content)
            dict1 = {}
            dict2 = {}
            s = ['ymax', 'ymin', 'alpha', 'beta']
            for i in range(len(data)):
                name = data[i]['name'].split('_')[0]

                # To ensure the value of first object in the pair also appear before the second object values.
                if data[i]['collection'] == "models" and name == element[2]:

                    # To ensure ymax, ymin, beta are in the default order
                    for j in range(len(data[i]["parameters"])):
                        for k in range(len(s)):
                            if data[i]["parameters"][j]['name'] == s[k]:
                                dict1[s[k]] = data[i]["parameters"][j]['value']
                                break
                if data[i]['collection'] == "models" and name == element[3]:
                    for j in range(len(data[i]["parameters"])):
                        for k in range(len(s)):
                            if data[i]["parameters"][j]['name'] == s[k]:
                                dict2[s[k]] = data[i]["parameters"][j]['value']
                                break
            # For odd situation with two parameter values, we only add four values into one line of reference table .
            if len(dict1) < len(s):
                for k in range(len(dict1)):
                    element.append(dict1[s[k]])
                for k in range(len(dict2)):
                    element.append(dict2[s[k]])
            # For normal situation with four parameter values, we will add eight values.
            else:
                for k in range(2):
                    element.append(dict1[s[k]])
                for k in range(2):
                    element.append(dict2[s[k]])
                for k in range(2,len(s)):
                    element.append(dict1[s[k]])
                for k in range(2,len(s)):
                    element.append(dict2[s[k]])
            # flag = 0: the input sensor pair of element[] doesn't exist in the table
            flag = 0
            for t in table:
                if (t[2] == element[2] and t[3] == element[3]) or (t[2] == element[3] and t[3] == element[2]):
                    if t[0] < element[0]:
                        for i in range(len(t)):
                            t[i] = element[i]
                    flag = 1
                    break

            if flag == 0: table.append(element)
    return table

in_dir = 'cello/input'
refer_table = build_lookup_table('cello/input/cello_scores_round_2.csv', in_dir)
file_out = open('cello/input/reference_table.csv','w',newline="")
csv_w = csv.writer(file_out)
csv_w.writerow(["score","modifications","signal_pair1", "signal_pair2","chassis", "ymax1", "ymin1", "ymax2", "ymin2", "alpha1","beta1",
                "alpha2", "beta2"])
for t in refer_table:
    csv_w.writerow(t)
file_out.close()