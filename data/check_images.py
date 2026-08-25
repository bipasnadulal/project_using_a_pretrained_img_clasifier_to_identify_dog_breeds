from time import time, sleep

from get_input_args import get_input_args

def main():
    # 0. Measures total program runtime by collecting start time
    
    start_time = time()

    sleep(60)

    end_time = time()

    tot_time = end_time - start_time

    print(f"Total Elapsed Runtime: {tot_time} in seconds.")

    # 1. 

    in_arg = get_input_args()

    #function that checks command line argument using in_arg
    check_command_line_arg(in_arg)