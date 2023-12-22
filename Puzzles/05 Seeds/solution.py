#%% Import libraries
import numpy as np
import re

#%% Import data
with open("input.txt") as file:
    code = file.read().splitlines()

#%% Functions
def extract_mapping_functions(code:list[str]):
    """ Extracts mapping functions from the code.
        Returns a dictionary with the mapping functions. """
    
    mapping_dict = {}

    dict_key = ""
    dict_vals = []
    ikey_vals = [0,0]
    for (l,line) in enumerate(code):
        # Get key for dictionary
        if ((line != "") and (line[-1] == ":")):
            dict_key = line.split(":")[0].split(" ")[0]
            ikey_vals[0] = l+1

        # If we already passed the key, we started looking at maping values.
        # Mapping values are done when we and are in an empty line.
        # Added an extra clause at the end for the last line
        if ((ikey_vals[0] != 0) & ((line == "") or (l == len(code)-1))):
            ikey_vals[1] = l

            # Create list with values
            for i in range(ikey_vals[0], ikey_vals[1]):
                dict_vals.append([int(number) for number in code[i].split()])

            # Create numpy array with values
            # dict_vals = np.array()

            # Add entry to dictionary
            mapping_dict[dict_key] = dict_vals

            # Reset temp variables
            dict_key = ""
            dict_vals = []
            ikey_vals = [0,0]

    return mapping_dict

def create_extended_maps(mapping_dict):
    """" Returns extended version of the mapping dictionary. 
        This is so that you don't have to do multiple mappings each time. """
    
    extended_dict = {}
    for key,values in mapping_dict.items():

        # Create extended list of values
        origin_list = []
        destination_list = []
        for val in values:
            destination_list.extend([value for value in range(val[0], val[0]+val[2])])
            origin_list.extend([value for value in range(val[1], val[1]+val[2])])         

        values_array = np.array((destination_list, origin_list))
        extended_dict[key] = values_array

    return extended_dict


def translate_list(input:int, mapping_vals:list[int]):
    """ Maps `input` value from `mapping_vals` with shape `[destination, origin, range]`. """
    
    # Preallocate lists
    origin_list = []
    destination_list = []

    # Create mapped list
    for vals in mapping_vals:
        destination_list.extend([value for value in range(vals[0], vals[0]+vals[2])])
        origin_list.extend([value for value in range(vals[1], vals[1]+vals[2])])        

    # Check if input needs to be mapped
    output = input
    for v,value in enumerate(origin_list):
        if (value == input):
            output = destination_list[v]

    return output


def complete_mapping(mapping_dict, seed):
    """ Returns translated the `seed` using `mapping dict` """ 

    temp_val = seed
    for [_,val] in mapping_dict.items():
        temp_val = translate_list(temp_val, val)
    
    location = temp_val

    return location

#%% Part 1
#   Translate all the seeds to locations. Return the lowest number

# Get mapping dictionary
mapping_dict = extract_mapping_functions(code)

#%% Get seeds
seeds = code[0].split(":")[-1].split(" ")[1:]

#%% Translate seeds to locations
locations = []
for seed in seeds:
    locations.append(complete_mapping(mapping_dict, int(seed)))

# Return lowest location
print(f"Lowest location is {min(locations)}")