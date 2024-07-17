import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = 'maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

# Displaying race
bot_data = {}
for bot in bots:
  bot_data[bot.name] = bot
# Populate a deque of all robot commands for the provided maze
robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
    # For every bot in the list of bots, if the bot has not reached the end, add a new move to the robot_moves deque
    # Add your code below!
    for bot in bots:
      if not bot.has_finished:
        robot_moves.append(rr.compute_robot_logic(walls, goal, bot))
    num_of_turns += 1

# Count the number of moves based on the robot names
# Add your code below!
move_count = Counter(move[0] for move in robot_moves)

# Create a namedtuple to
BotScoreData = namedtuple('BotScoreData', ['name', 'num_moves', 'num_collisions', 'score'])
