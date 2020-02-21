from room import Room
from player import Player
from world import World
from stack import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
backwords = {'n':'s', 'e':'w', 's':'n', 'w':'e'}

def dft(self, starting_vertex, traversal_path, v = 0):
        # Create an empty Stack
        s = Stack()
        # Add A PATH TO the starting_vertex to the queue
        s.push(starting_vertex)
        # Create an empty set to store visited rooms
        visited_rooms = set()
        # While the stack is not empty...
        while s.size() > 0:
            exits = list()
            # Get all avaible exits of current room
            for door in player.current_room.get_exits():
                exits += list(door)
            # Hold the prev room
            prev_v = v
            # Pop the last in stack
            v = s.pop()
            print(f'Current Room: {player.current_room.id}')
            # Check if it has been visited
            # If not visited...
            if v not in visited_rooms:
                # Add current room to visited_rooms
                visited_rooms.add(v)
                #Check to see if we visited all the rooms!
                if len(visited_rooms) == 12:
                    print(f'You have visited every room! {len(visited_rooms)}')
                    print(f'Traversal Path: {traversal_path}')
                    return traversal_path
                else:
                    # If the exit exists and is not visited we will go that direction
                    if 'n' in exits and player.current_room.get_room_in_direction('n').id not in visited_rooms:
                        player.travel('n')
                        traversal_path.append('n')
                        s.push(player.current_room.id)
                    elif 'e' in exits and player.current_room.get_room_in_direction('e').id not in visited_rooms:
                        player.travel('e')
                        traversal_path.append('e')
                        s.push(player.current_room.id)
                    elif 's' in exits and player.current_room.get_room_in_direction('s').id not in visited_rooms:
                        player.travel('s')
                        traversal_path.append('s')
                        s.push(player.current_room.id)
                    elif 'w' in exits and player.current_room.get_room_in_direction('w').id not in visited_rooms:
                        player.travel('w')
                        traversal_path.append('w')
                        s.push(player.current_room.id)
                    # If all exits are visited then we need to backtrack
                    else:
                        last_move = traversal_path[-1]
                        if backwords[last_move] == 'n':
                            player.travel('n')
                            traversal_path.append('n')
                        elif backwords[last_move] == 'e':
                            player.travel('e')
                            traversal_path.append('e')
                        elif backwords[last_move] == 's':
                            player.travel('s')
                            traversal_path.append('s')
                            print(traversal_path)
                        elif backwords[last_move] == 'w':
                            player.travel('w')
                            traversal_path.append('w')
                        s.push(prev_v)
            # If room has already been visited
            else:
                # If the exit exists and is not visited we will go that direction
                if 'n' in exits and player.current_room.get_room_in_direction('n').id not in visited_rooms:
                     player.travel('n')
                     traversal_path.append('n')
                     s.push(player.current_room.id)
                elif 'e' in exits and player.current_room.get_room_in_direction('e').id not in visited_rooms:
                    player.travel('e')
                    traversal_path.append('e')
                    s.push(player.current_room.id)
                elif 's' in exits and player.current_room.get_room_in_direction('s').id not in visited_rooms:
                    player.travel('s')
                    traversal_path.append('s')
                    s.push(player.current_room.id)
                elif 'w' in exits and player.current_room.get_room_in_direction('w').id not in visited_rooms:
                        player.travel('w')
                        traversal_path.append('w')
                        s.push(player.current_room.id)
                # If all exits have been visited then we need to backtrack
                else:
                    last_move = traversal_path[-1]
                    if backwords[last_move] == 'n':
                        player.travel('n')
                        traversal_path.append('n')
                    elif backwords[last_move] == 'e':
                        player.travel('e')
                        traversal_path.append('e')
                    elif backwords[last_move] == 's':
                        player.travel('s')
                        traversal_path.append('s')
                    elif backwords[last_move] == 'w':
                        player.travel('w')
                        traversal_path.append('w')
                    s.push(prev_v)

        print(f'Visited: {visited_rooms}')
        print(f'Traversal Path: {traversal_path}')
        return traversal_path
        
        
dft(player, 0, traversal_path)
print(f'Length of Traversal Path: {len(traversal_path)}\n\n')


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
