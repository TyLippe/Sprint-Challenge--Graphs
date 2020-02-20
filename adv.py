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


def dft(self, starting_vertex, traversal_path):
        # Create an empty Stack
        s = Stack()
        # Add A PATH TO the starting_vertex to the queue
        s.push(starting_vertex)
        # Create an empty set to store visited rooms
        visited_rooms = set()
        # While the queue is not empty...
        while s.size() > 0:
            exits = list()
            # Get all avaible exits of current room
            for door in player.current_room.get_exits():
                exits += list(door)
            print(f'Exits: {exits}')
            # Dequeue, the first PATH
            v = s.pop()
            # Check if it has been visited
            # If not visited...
            if v not in visited_rooms:
                # Add current room to visited_rooms
                visited_rooms.add(v)
                # Move player and add new room to visited
                player.travel('n')
                # visited_rooms.add(player.current_room.id)
                s.push(player.current_room.id)
                print(f'Visited: {visited_rooms}')
                if 'n' in exits:
                    traversal_path.append('n')
        print(traversal_path)
                


dft(player, 0, traversal_path)
print(len(traversal_path))