from time import time, sleep

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isdog import adjust_results4_isdog

def main():
    # 0. Measures total program runtime by collecting start time
    
    start_time = time()

    sleep(60)

    end_time = time()

    tot_time = end_time - start_time

    print(f"Total Elapsed Runtime: {tot_time} in seconds.")

    # 1. Command Line Arguments

    in_arg = get_input_args()

    #function that checks command line argument using in_arg
    # check_command_line_arg(in_arg)

    # 2. Creating pet image labels
    results = get_pet_labels(in_arg.dir)

    # check_creating_pet_image_labels(results)

    # 3. Classify Images
    classify_images(in_arg.dir, results, in_arg.arch)

    # check_classifying_images(results)

    # 4. Classifying labels as dog
    adjust_results4_isdog(results, in_arg.dogfile)