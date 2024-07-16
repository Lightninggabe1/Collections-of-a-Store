import csv
import random as rand


def read_maze(name):
    maze_chars = []
    with open(name, 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            maze_chars.append(row)
    return maze_chars


def print_maze(maze_data):
    for row in maze_data:
        printed_row = ''
        for col in row:
            printed_row += col + '  '
        print(printed_row)
    print('\n')

def is_race_over(bots):
    done = True
    for bot in bots:
        if not bot.has_finished:
            done = False
    return done


def print_results(bot_score_data):
    bot_score_data.sort(key=lambda b: b.score)
    place = 1
    print("----- RESULTS -----")
    for score_data in bot_score_data:
        print(str(place) + '. Robot: ' + str(score_data.name))
        print('  ' +  'Score: ' + str(score_data.score) + ' Moves: ' + str(score_data.num_moves) + ' Collisions: ' + str(score_data.num_collisions))
        place += 1


def process_maze_init(maze_data):
    walls = []
    goal = None
    bots = []
    for r, row in enumerate(maze_data):
        for c, col in enumerate(row):
            if col == '#':
                walls.append(Wall(c,r))
            elif col == '$':
                goal = Goal(c,r)
            elif col.isalpha():
                bots.append(Robot(c,r, col))
    return [walls, goal, bots]


def compute_robot_logic(walls, goal, bot):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    move_names = {(-1, 0): 'left', (1, 0): 'right', (0, -1): 'down', (0, 1): 'up', (0, 0): 'nothing'}

    selected_move = moves[rand.randint(0,3)]
    move_dist = []
    for m, move in enumerate(moves):
        dist = calc_manhattan_dist(bot.calc_x + move[0], bot.calc_y + move[1], goal.x, goal.y)
        move_dist.append([m,dist])
    move_dist.sort(key=lambda x: x[1])
    if rand.random() < 0.45:
        selected_move = moves[move_dist[0][0]]

    hit_wall = False
    for wall in walls:
        if bot.calc_x + selected_move[0] == wall.x and bot.calc_y + selected_move[1] == wall.y:
            hit_wall = True

    found_alternate_move = False
    if hit_wall:
        for next_move in move_dist:
            move = moves[next_move[0]]
            hit_wall_move = False
            for wall in walls:
                if bot.calc_x + move[0] == wall.x and bot.calc_y + move[1] == wall.y:
                    hit_wall_move = True

            if not hit_wall_move:
                selected_move = move
                found_alternate_move = True
                break

        if not found_alternate_move:
            selected_move = (0,0)

    if bot.calc_x + selected_move[0] == goal.x and bot.calc_y + selected_move[1] == goal.y:
        bot.has_finished = True
        bot.calc_x += selected_move[0]
        bot.calc_y += selected_move[1]
        return bot.name, 'finished', hit_wall

    bot.calc_x += selected_move[0]
    bot.calc_y += selected_move[1]
    return bot.name, move_names[selected_move], hit_wall


def update_maze_characters(old_maze_chars, bots):
    to_replace = []
    for r, row in enumerate(old_maze_chars):
        for c, col in enumerate(row):
            if col.isalpha() or col == '+':
                to_replace.append((c,r))
    for elem in to_replace:
        old_maze_chars[elem[1]][elem[0]] = '_'
    for bot in bots:
        if not bot.remove:
            if old_maze_chars[bot.y][bot.x].isalpha():
                old_maze_chars[bot.y][bot.x] = '+'
            else:
                old_maze_chars[bot.y][bot.x] = bot.name


def calc_manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Robot:
    def __init__(self, x, y, name):
        self.x = x
        self.calc_x = x
        self.y = y
        self.calc_y = y
        self.has_finished = False
        self.remove = False
        self.name = name

    def process_move(self, direction):
        if direction == 'left':
            self.x += -1
        if direction == 'right':
            self.x += 1
        if direction == 'up':
            self.y += 1
        if direction == 'down':
            self.y += -1
        if direction == 'finished':
            self.remove = True


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
