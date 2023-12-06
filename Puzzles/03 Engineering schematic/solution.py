#%% Import file
with open("input.txt") as file:
    code = file.read().splitlines()

#%% Functions
def find_numbers(line:str):
    """ Finds the numbers in a string. Returns all numbers list of numbers, 
        and start and end indices in three separate lists """
    
    # Create empty lists for results
    numbers = []
    istart = []
    iend = []

    # Check characters one by one
    temp_char = ""
    start_flag = 0 # Flag to know whether a number sequence has started

    for (c, char) in enumerate(line):      
        # If the character is a digit, save its value and index
        if char.isdigit():
            temp_char += char
            if (not start_flag):
                istart.append(c)
                start_flag = 1

            # If the last character is a digit, save values in output
            if (c == len(line)-1):
                numbers.append(int(temp_char))
                iend.append(c)

        # When done with contiguous digits, save previous index as end
        else:
            if (start_flag):
                numbers.append(int(temp_char))
                iend.append(c-1)

                # Reset temp variables
                temp_char = ""
                start_flag = 0

    return numbers, istart, iend

def find_symbols(line:str):
    """ Finds non-alphanumeric symbols and returns their indices. """
    symbols_indices = []

    for (c, char) in enumerate(line):
        if (not char.isalnum()) & (char != "."):
            symbols_indices.append(c)

    return symbols_indices

def find_numbers_next_to_symbol(test_line:str, contiguous_lines:list[str]):
    """ Returns the list of the numbers in `test_line` next to a symbol all other lines.
        Contiguous lines must include `test_line` as well. """
    
    # Find numbers and their indices
    (numbers, istart, iend) = find_numbers(test_line)
    lines_len = len(test_line)  # All lines should be the same length, 
                                # get length from test_line

    # Find symbols and their indices
    isymbols = []
    for line in contiguous_lines:
        temp_symbols = find_symbols(line)
        # Make sure that the list has some values
        if temp_symbols != []:
            isymbols.append(temp_symbols)

    # Create flatenned list
    all_symbols = sum(isymbols, [])

    # For each number, check if it is contiguous to a symbol
    contiguous_numbers = []
    for (n,number) in enumerate(numbers):
        for isymbol in all_symbols:
            # Make sure you don't go below 0
            temp_start = istart[n] - 1
            if (temp_start < 0):
                temp_start == 0

            # Make sure you don't go over the length of the string
            temp_end = iend[n] + 1
            if (iend[n] > lines_len-1):
                temp_end = iend[n]

            if (isymbol >= temp_start) & (isymbol <= temp_end):
                contiguous_numbers.append(number)
                break

    return contiguous_numbers

def find_asterisks(line):
    """ Returns the index of * in a line """
    iasteriks = [c for (c,char) in enumerate(line) if (char == "*")]
    
    return iasteriks

def find_gear_ratios(test_line:str, contiguous_lines:list[str]):
    iasterisks = find_asterisks(test_line)

    # Preallocate sizes of number lists
    numbers = [None] * len(contiguous_lines)
    istart = [None] * len(contiguous_lines)
    iend = [None] * len(contiguous_lines)

    # Get nunmbers and indices
    for (l,line) in enumerate(contiguous_lines):
        (numbers[l], istart[l], iend[l]) = find_numbers(line)

    # Keep numbers that touch an asterisk symbol    
    gear_ratios = []
    for asterisk in iasterisks:
        adjacent_nums = 0   # Counter for numbers adjacent to an asterisk
        temp_ratio = 1

        for (l,line) in enumerate(contiguous_lines):
            for n,number in enumerate(numbers[l]):
                # Make sure you don't check below index 0
                temp_start = istart[l][n] - 1
                if temp_start < 0: 
                    temp_start = 0 

                # Make sure you don't check over last index
                temp_end = iend[l][n] + 1
                if temp_end > len(line)-1:
                    temp_end = len(line)-1

                # If asterisk is touching the number
                if (asterisk >= temp_start) & (asterisk <= temp_end):
                    temp_ratio *= number
                    adjacent_nums += 1
        
        # If there was more than one number next to an asterisk
        if (adjacent_nums > 1):
            gear_ratios.append(temp_ratio)
        
        # If there where no numbers next to an asterisk
        if gear_ratios == []:
            gear_ratios = [0]
        
    return gear_ratios        


#%% Part 1
#   - Find all numbers that are next to a symbol in the previous or next line
contiguous_numbers = []
nlines = len(code) - 1

for l,line in enumerate(code):
    # Test case for first line
    if (l == 0):
        contiguous_numbers.append(find_numbers_next_to_symbol(line, [code[0], code[1]]))
    # Test case for last line
    elif (l == nlines):
        contiguous_numbers.append(find_numbers_next_to_symbol(line, [code[-2], code[-1]]))
    # Any other line
    else:
        contiguous_numbers.append(find_numbers_next_to_symbol(line, [code[l-1], code[l], code[l+1]]))

all_numbers = sum(sum(contiguous_numbers, []))
print(f"Part 1\nAll numbers = {all_numbers}")

#%% Part 2
#   - Find gear ratios based on * symbol
gear_ratios = []
nlines = len(code) - 1

for l,line in enumerate(code):
    # Test case for first line
    if (l == 0):
        gear_ratios.append(find_gear_ratios(line, [code[0], code[1]]))
    # Test case for last line
    elif (l == nlines):
        gear_ratios.append(find_gear_ratios(line, [code[-2], code[-1]]))
    # Any other line
    else:
        gear_ratios.append(find_gear_ratios(line, [code[l-1], code[l], code[l+1]]))

total_ratio = sum(sum(gear_ratios, []))
print(f"Part 1\nAll numbers = {total_ratio}")