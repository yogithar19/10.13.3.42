import numpy as np

# Generate a shuffled list of numbers from 1 to 1000
numbers = np.arange(1, 1001)
np.random.shuffle(numbers)

# Count the occurrences of perfect squares greater than 500
perfect_squares_gt_500 = [num for num in numbers if num > 500 and int(num ** 0.5) ** 2 == num]
count_prizes = len(perfect_squares_gt_500)

# Total number of simulations
total_simulations = len(numbers)

# Probability calculation
probability_first_player = count_prizes / total_simulations

# After first player wins, remove their card from the list
numbers = np.delete(numbers, np.where(numbers == perfect_squares_gt_500[0]))

# Count the occurrences of perfect squares greater than 500 among remaining cards
count_prizes_second_player = len([num for num in numbers if num > 500 and int(num ** 0.5) ** 2 == num])
total_simulations_second_player = len(numbers)

# Probability calculation for second player
probability_second_player = count_prizes_second_player / total_simulations_second_player

print(f"Probability that the first player wins a prize: {probability_first_player:.4f}")
print(f"Probability that the second player wins a prize, given that the first player has won: {probability_second_player:.4f}")

print(f"Simulation results : {numbers[:100]}")
