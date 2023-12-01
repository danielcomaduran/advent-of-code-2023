#%% Decoder object
class Decoder:
    def __init__(self, code_file:str):
        """
            Decoder object.

            Attributes
            ----------
            - `code_file`: Path to text file with secret code
            

        """
        self.code_file = code_file

        # Read code file and store as list of values
        with open(code_file) as file:
            self.code = file.read().splitlines()

    def digits_from_list(self):
        """ Extracts digits from list of strings. Returns list of digits. """
        digit_list = [[] for _ in range(len(self.code))]    # Create empty list
        
        for l,line in enumerate(self.code):
            temp_digit_list = []
            [temp_digit_list.append(char) for char in line if char.isdigit()]

            digit_list[l] = self._number_from_string_(temp_digit_list)

        return digit_list
    
    def written_nums_to_digit_list(self):
        """ Decodes string considering written numbers (e.g., two = 2wo). """
        digit_list = [[] for _ in range(len(self.code))]    # Create empty list

        for l, line in enumerate(self.code):
            digits_line = self._replace_written_digits_(line)

            temp_digit_list = []
            [temp_digit_list.append(char) for char in digits_line if char.isdigit()]

            digit_list[l] = self._number_from_string_(temp_digit_list)

        return digit_list

    def _number_from_string_(self, string_code:str):
        """ Creates two digit number from string. """
        number = int(string_code[0] + string_code[-1])
        
        return number
  
    def _replace_written_digits_(self, line:str):
        """ Finds if there are written numbers and replaces the first char of
            the number with its corresponding digit (e.g., two = 2wo). """

        number_strings = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        
        line_with_digits = line  # In case the string doesn't have any written numbers

        # Iterate through the characters in the list and compare to numbers in number_string
        for i in range(len(line)):          
            for key,val in number_strings.items():
                # Cut string to match length of number_string.key()
                slice = line[i:i+len(key)]

                # If slice matches key, replace first char with corresponding number
                if slice == key:
                    line_with_digits = self._replace_char_by_index_(line_with_digits, i, val)
                    # print("Hola")
                    # print(line_with_numbers)

        return line_with_digits    

    def _replace_char_by_index_(self, string:str, index:int, new_char:str):
        """ Replaces a single character with `new_char` at `index` in a string. """
        
        # Check if index is in correct range.
        # - Return new string if index is in range
        # - Return original string otherwise
        if 0 <= index < len(string):
            return string[:index] + new_char + string[index+1:]
        else:
            return string      

#%% Part one
#   - Look at the digits (e.g., 0,1,2) use the first and last to create
#     a two digit number and sum them all.
part_one_decoder = Decoder("input.txt")
digit_sum = sum(part_one_decoder.digits_from_list())
print(f"Sum of all digits is = {digit_sum}")

#%% Part two
#   - Numbers might be written in text, repeat the steps from part one
#     but consider the written numbers as well.
part_two_decoder = Decoder("input.txt")
digit_sum_2 = sum(part_two_decoder.written_nums_to_digit_list())
print(f"sum of digits considering written numbers is = {digit_sum_2}")