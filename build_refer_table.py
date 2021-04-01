import math
import copy
import re
import numpy as np
import csv

# Find the coefficients of the pair which has highest score. And save that info int a csv file.
def build_lookup_table(path):
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
                elif i == 2:
                    e = line[i].strip('[').strip(']').split("'")
                    element.append(e[1])
                    element.append(e[3])
                else: element.append(line[i])
            flag = 0
            for t in table:
                if (t[2] == element[2] and t[3] == element[3]) or (t[2] == element[3] and t[3] == element[2]):
                    if t[0] < element[0]:
                        t[0] = element[0]
                        t[1] = element[1]
                        t[4] = element[4]
                    flag = 1
                    break
            if flag == 0: table.append(element)
    return table

refer_table = build_lookup_table('cello/input/cello_scores_round_2.csv')
file_out = open('cello/input/reference_table.csv','w',newline="")
csv_w = csv.writer(file_out)
csv_w.writerow(["score","modifications","signal_pair1", "signal_pair2","chassis"])
for t in refer_table:
    csv_w.writerow(t)
file_out.close()