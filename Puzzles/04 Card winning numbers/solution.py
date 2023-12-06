#%% Import data
with open("input.txt") as file:
    code = file.read().splitlines()

#%% Functions
def get_card_id(line:str):
    """ Returns card ID numbers in list. """
    
    card_id = int(line.split(":")[0].split()[-1])
    return card_id

def get_winning_numbers(line:str):
    """ Gets the winning numbers (i.e., left of '|") for a single line.
        Returns a list with the numbers.  """

    str_winning_numbers = line.split("|")[0].split(":")[1]
    list_winning_numbers = [int(number) for number in str_winning_numbers.split()]

    return list_winning_numbers

def get_card_numbers(line:str):
    """ Gets the numbers in the card (i.e., right of '|') for a single line.
        Returns a list with the numbers. """

    str_numbers = line.split("|")[1]
    list_numbers = [int(number) for number in str_numbers.split()]

    return list_numbers
    
def calculate_card_points(line:str):
    """ Calculates how many points is a card worth.
        - First match between winning numbers and card numbers = 1 point.
        - Subsequent matches = 2 points. """
    
    # Count number of winning cards
    winning_numbers_counter = count_winning_cards(line)

    # Compute number of points
    points = 0
    if (winning_numbers_counter > 0):
        points = 2**(winning_numbers_counter-1)
    
    return points

def count_winning_cards(line:str):
    """ Counts number of winning cards. """
    
    winning_numbers = get_winning_numbers(line)
    card_numbers = get_card_numbers(line)

    winning_numbers_counter = 0

    # Count how many numbers match between the winning set and the card set
    for winning_number in winning_numbers:
        for card_number in card_numbers:
            if (winning_number == card_number):
                winning_numbers_counter += 1 

    return winning_numbers_counter


def count_scratch_cards(code):
    """ Counts the number of original and repeated winning scratching cards. """

    card_ids = [get_card_id(line)-1 for line in code]
    
    # Calculate number of winning cards and append to end of list
    for card_id in card_ids:    
        line_id = get_card_id(code[card_id])
        winning_cards = count_winning_cards(code[card_id])

        repeated_cards = [card for card in range(line_id, line_id+winning_cards)]
        for card in repeated_cards:
            card_ids.append(card)
        # card_ids.append([repeated_cards for repeated_cards in range(card_id+1, card_id+winning_cards+1)])
    
    return len(card_ids)

#%% Part one
#   - Get the total number of points
total_points = [calculate_card_points(line) for line in code]
sum_total_points = sum(total_points)
print(f"Part 1\nTotal number of points: {sum_total_points}")

#%% Part two
#   - Count total number of winning cards
total_cards = count_scratch_cards(code)
print(f"Part 2\nTotal number of cards: {total_cards}")