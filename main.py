from itertools import combinations
from celloapi2 import CelloQuery, CelloResult

# Set our directory variables.
in_dir = '/Users/Shockwing/Dropbox/Boston/Curriculum/EC_552/Homework/HW1/EC552_HW1/cello/input'
out_dir = '/Users/Shockwing/Dropbox/Boston/Curriculum/EC_552/Homework/HW1/EC552_HW1/cello/output'
v_file = 'and.v'
options = 'options.csv'
# Calculate number of inputs into the Circuit.
signal_input = 2



# We want to try every e-coli chassis.
chassis_name = ['Eco1C1G1T1', 'Eco1C2G2T2', 'Eco2C1G3T1']

best_score = 0
best_chassis = None
best_input_signals = None
for chassis in chassis_name:
    in_ucf = f'{chassis}.UCF.json'
    input_sensor_file = f'{chassis}.input.json'
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











# We need to define functions that grab linear coefficients from *.input.json
# files, calculate response curves, optimize response curve, etc.

def get_linear_coefficients():
    """
    
    
    :input:
    :input:
    :returns:
    """
    pass

def calculate_response_curve():
    """
    :input:
    :input:
    :returns:
    """
    pass

def optimize_response_curve():
    """
    :input:
    :input:
    :returns:
    """
    pass

def optimize_repressor():
    """
    Use Scipy optimization functionality, where DNA and protein parameters
    (i.e., linear coefficients) are iteratively modified and submitted to
    CelloQuery() for scoring. We can test different Scipy optimization methods
    and see which one works best.

    :input in_repressor: the input circuit to optimize.
    :input optimization_method: a specified scipy optimization method.
    :returns:
    """
    pass

