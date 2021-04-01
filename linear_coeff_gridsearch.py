from itertools import combinations
import glob
from celloapi2 import CelloQuery, CelloResult
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from mpl_toolkits import mplot3d
import numpy as np



# Set our directory variables.
in_dir = '/Users/Shockwing/Dropbox/Boston/Curriculum/EC_552/Homework/HW1/EC552_HW1/cello/input'
out_dir = '/Users/Shockwing/Dropbox/Boston/Curriculum/EC_552/Homework/HW1/EC552_HW1/cello/output'
v_file = 'and.v'
options = 'options.csv'
# Calculate number of inputs into the Circuit.
signal_input = 2


# Populate list of paths for all modified *.inpput.json files
input_files = glob.glob("cello/input/input_modified/*.json")

# Screen: iteratively pass modified inputs into CelloQuery() and record scores
all_scores = []
for file in input_files:
    file_name = file.split('/')[-1]
    file_chassis = file.split('/')[-1].split('.')[0]
    modifications = \
        ".".join(file.split('/')[-1].split('.')[2:])
    print(modifications)

    best_score = 0
    best_chassis = None
    best_input_signals = None

    in_ucf = f'{file_chassis}.UCF.json'
    input_sensor_file = file_name
    output_device_file = f'{file_chassis}.output.json'
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
    # signals.remove('AraC')
    signal_pairing = list(combinations(signals, signal_input))
    for signal_set in signal_pairing:
        signal_set = list(signal_set)
        q.set_input_signals(signal_set)
        q.get_results()
        try:
            res = CelloResult(results_dir=out_dir)
            res_ID = [res.circuit_score, modifications, signal_set, file_chassis]
            all_scores.append(res_ID)
            if res.circuit_score > best_score:
                best_score = res.circuit_score
                best_chassis = file_chassis
                best_input_signals = signal_set
        except:
            pass
        q.reset_input_signals()
    print('-----')

    score_results = [best_score, modifications, file_chassis]
    all_scores.append(score_results)
    print(all_scores)


# Saving screen results to csv
# df = pd.DataFrame(all_scores, columns=['score', 'modifications', 'signal_pairing', 'chassis'])
# df.to_csv('cello_scores_round_2.csv', index=False)






