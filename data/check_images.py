from time import time, sleep

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isdog import adjust_results4_isdog
from calculate_results_stats import calculate_results_stats
from print_results import print_results

def main():
    # 0. Measures total program runtime by collecting start time
    
    start_time = time()

    sleep(60)
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

    # 5. Calculating results stats

    results_stats = calculate_results_stats(results)

    # 6. Printing results

    print_results(results, results_stats, in_arg.arch, True, True)

    # 0. Measure total program runtime by collecting end time

    end_time = time()

    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()

