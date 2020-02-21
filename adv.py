from room import Room
from player import Player
from world import World
from utils import Stack
from utils import Queue
# from hardcode import traversal_path

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# class Graph:
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, vertex_id):
#         if vertex_id not in self.vertices:
#             self.vertices[vertex_id] = set()
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError('That vertex does not exisit!')


# def dft(self, starting_vertex, traversal_path, v = 0):
#         # Create an empty Stack
#         s = Stack()
#         # Add A PATH TO the starting_vertex to the queue
#         s.push(starting_vertex)
#         # Create an empty set to store visited rooms
#         visited_rooms = set()
#         # While the stack is not empty...
#         while s.size() > 0:
#             directions = ['n', 'e', 's', 'w']
#             first_dir = random.choice(directions)
#             directions.remove(first_dir)
#             second_dir = random.choice(directions)
#             directions.remove(second_dir)
#             third_dir = random.choice(directions)
#             directions.remove(third_dir)
#             fourth_dir = random.choice(directions)
#             directions.remove(fourth_dir)
#             exits = list()
#             # Get all avaible exits of current room
#             for door in player.current_room.get_exits():
#                 exits += list(door)
#             # Hold the prev room
#             prev_v = v
#             # Pop the last in stack
#             v = s.pop()
#             # Check if it has been visited
#             # If not visited...
#             if v not in visited_rooms:
#                 # Add current room to visited_rooms
#                 visited_rooms.add(v)
#                 #Check to see if we visited all the rooms!
#                 if len(visited_rooms) == 18:
#                     print(f'You have visited every room! {len(visited_rooms)}')
#                     return traversal_path
#                 else:
#                     # If the exit exists and is not visited we will go that direction
#                     if first_dir in exits and player.current_room.get_room_in_direction(first_dir).id not in visited_rooms:
#                         player.travel(first_dir)
#                         traversal_path.append(first_dir)
#                         s.push(player.current_room.id)
#                     elif second_dir in exits and player.current_room.get_room_in_direction(second_dir).id not in visited_rooms:
#                         player.travel(second_dir)
#                         traversal_path.append(second_dir)
#                         s.push(player.current_room.id)
#                     elif third_dir in exits and player.current_room.get_room_in_direction(third_dir).id not in visited_rooms:
#                         player.travel(third_dir)
#                         traversal_path.append(third_dir)
#                         s.push(player.current_room.id)
#                     elif fourth_dir in exits and player.current_room.get_room_in_direction(fourth_dir).id not in visited_rooms:
#                         player.travel(fourth_dir)
#                         traversal_path.append(fourth_dir)
#                         s.push(player.current_room.id)
#                     # If all exits are visited then we need to backtrack
#                     else:
#                         traversal_path_copy = list(traversal_path)
#                         last_move = traversal_path_copy.pop()
#                         player.travel(backwords[last_move])
#                         traversal_path.append(backwords[last_move])
#                         s.push(prev_v)
#             # If room has already been visited
#             else:
#                 # If the exit exists and is not visited we will go that direction
#                 if first_dir in exits and player.current_room.get_room_in_direction(first_dir).id not in visited_rooms:
#                      player.travel(first_dir)
#                      traversal_path.append(first_dir)
#                      s.push(player.current_room.id)
#                 elif second_dir in exits and player.current_room.get_room_in_direction(second_dir).id not in visited_rooms:
#                     player.travel(second_dir)
#                     traversal_path.append(second_dir)
#                     s.push(player.current_room.id)
#                 elif third_dir in exits and player.current_room.get_room_in_direction(third_dir).id not in visited_rooms:
#                     player.travel(third_dir)
#                     traversal_path.append(third_dir)
#                     s.push(player.current_room.id)
#                 elif fourth_dir in exits and player.current_room.get_room_in_direction(fourth_dir).id not in visited_rooms:
#                         player.travel(fourth_dir)
#                         traversal_path.append(fourth_dir)
#                         s.push(player.current_room.id)
#                 # If all exits have been visited then we need to backtrack
#                 else:
#                     last_move = traversal_path_copy.pop()
#                     player.travel(backwords[last_move])
#                     traversal_path.append(backwords[last_move])
#                     s.push(prev_v)
#         return traversal_path
        
        
# dft(player, 0, traversal_path)


def adventure_time(world, traversal_path):
    # Unknown_check will check if we have any ? left in the visted rooms
    def question_check(graph):
        for key in graph:
            if '?' in graph[key].values():
                return True
        return False

    # Find_move takes the current room and figures out what the directions avaible are
    def find_move(visited_rooms, curr_room):
        curr_room = curr_room.id
        room_exits = visited_rooms[curr_room]
        for direction in room_exits:
            if room_exits[direction] == '?' and curr_room.get_room_in_direction(direction).id not in visited_rooms:
                return direction
        return None

    # Find_next_room takes the current room and finds if any rooms connected have a ?, if they do we will add that direction to our path
    def find_next_room(s, traversal_path, visited_rooms, curr_room):
        while True:
            next_move = s.pop()
            traversal_path.append(next_move)
            next_room = curr_room.get_room_in_direction(next_move)
            if '?' in visited_rooms[next_room.id].values():
                return next_room.id
            curr_room = next_room

    # def double_time(visited_rooms, curr_room, traversal_path):
    #   # Was wanting to add a function that would continue a straight path if open. Then work back


    # Create our stack
    s = Stack()
    # Add our starting room
    v = 0
    # Create a visited dict
    visited_rooms = {0: {}}
    # Create our current room var
    curr_room = world.rooms[v]
    # Backwards dict to reference when backtracking
    backwards = {'n':'s', 'e':'w', 's':'n', 'w':'e'}

    # For loop that adds direction key and ? as a value to our starting room
    for direction in curr_room.get_exits():
        visited_rooms[curr_room.id][direction] = '?'
    # While loop that will check if we have visited the max number of rooms and that there is no ?
    while len(visited_rooms) < len(world.rooms) and question_check(visited_rooms):
        # Update the current room
        curr_room = world.rooms[v]
        # If current room has not been visited yet
        if curr_room not in visited_rooms:
            # Add to visited
            visited_rooms[curr_room.id] = {}
            # Get the direction key and ? as a value 
            for direction in curr_room.get_exits():
                visited_rooms[curr_room.id][direction] = '?'
        # Run our find move function to decide where to go next
        next_move = find_move(visited_rooms, curr_room)
        # If next move == None we path to the next room with ? in it still
        if not next_move:
            v = find_next_room(s, traversal_path, visited_rooms, curr_room)
        # If we have our next move then we will add that move to traversal
        else:
            traversal_path.append(next_move)
            # Update next room
            next_room = curr_room.get_room_in_direction(next_move)
            # Add to visited rooms
            visited_rooms[v][next_move] = next_room.id
            # If the next room is not in visited
            if next_room.id not in visited_rooms:
                # Add to visited
                visited_rooms[next_room.id] = {}
                # Get exits and add direction as key and ? as value
                for direction in next_room.get_exits():
                    visited_rooms[next_room.id][direction] = '?'
            # Traverse back 
            visited_rooms[next_room.id][backwards[next_move]] = curr_room.id
            s.push(backwards[next_move])
            v = next_room.id


adventure_time(world, traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
