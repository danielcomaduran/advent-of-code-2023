#%% Import data
with open("input.txt") as file:
            games = file.read().splitlines()

#%% Part 1
#   - Determine which games could be possible if you started with:
#     12 red cubes, 13 green cubes, and 14 blue cubes
possible_colors = {"red":12, "green":13, "blue":14}
feasible_games = [index+1 for index in range(len(games))]
ngames = len(games)

# For each game, get all the sets played
for g, game in enumerate(games):
    game_sets = game.split(": ")[-1].split("; ")

    # For each set, get the individual games and cubes picked
    for _, game_set in enumerate(game_sets):
        cubes_per_game = game_set.split(", ")
        cubes_colors_per_game = [cube.split(" ")[-1] for cube in cubes_per_game]
        cubes_numbers_per_game = [int(cube.split(" ")[0]) for cube in cubes_per_game]

        # Check that each cube is below the total available
        for color, number in zip(cubes_colors_per_game, cubes_numbers_per_game):
            # If the game is feasible, store ID number
            if (number > possible_colors[color]):
                feasible_games[g] = 0

print(f"Part 1\nResult: {sum(feasible_games)}")                        

#%% Part 2
#   - Determine the minimum number of cubes needed for each game


cubes_colors = ["red", "green", "blue"]
minimum_ncolors = [[0,0,0] for _ in range(len(games))]
# minimum_power = [_ for _ in range(len(games))]

# For each game, get all the sets played
for g, game in enumerate(games):
    game_sets = game.split(": ")[-1].split("; ")
    color_per_game_set = [0,0,0]

    # For each set, get the individual games and cubes picked
    for gs, game_set in enumerate(game_sets):
        cubes_per_game = game_set.split(", ")
        cubes_colors_per_game = [cube.split(" ")[-1] for cube in cubes_per_game]
        cubes_numbers_per_game = [int(cube.split(" ")[0]) for cube in cubes_per_game]

        for (color, number) in zip(cubes_colors_per_game, cubes_numbers_per_game):
            temp_number = color_per_game_set[cubes_colors.index(color)]
            if (number > temp_number):
                color_per_game_set[cubes_colors.index(color)] = number

    minimum_ncolors[g] = color_per_game_set

# Compute power
minimum_power = 0
for game in minimum_ncolors:
    temp_multiplication = 1
    for g in game:
         temp_multiplication *= g
    
    minimum_power += temp_multiplication
