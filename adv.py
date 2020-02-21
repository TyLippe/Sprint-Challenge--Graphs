from room import Room
from player import Player
from world import World
from utils import Stack
from utils import Queue

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


# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError('That vertex does not exist')

#     def get_neighbors(self, vertex_id):
#         return self.vertices[vertex_id]

#     def get_all_social_paths(self, starting_vertex):
#         # Create an empty queue
#         q = Queue()
#         # Add a PATH to the starting_vertex_id to the queue
#         q.enqueue([starting_vertex])
#         # Create an empty dictionary to store visited users and social paths
#         visited = {}
#         # While the queue is not empty..
#         while q.size() > 0:
#             # Dequeue the first path
#             path = q.dequeue()
#             # Grab the last vertex from the path
#             v = path[-1]
#             # Check if it has been visited
#             if v not in visited:
#                 # Mark it as visited
#                 visited[v] = path
#                 # Then add the Friends to the back of the queue
#                 for room_id in self.vertices[v]:
#                     if room_id not in visited:
#                         # Copy the path
#                         copy_path = path.copy()
#                         # Add Friend to the path
#                         copy_path.append(room_id)
#                         q.enqueue(copy_path)
#         return visited

# g = Graph()
# g.get_all_social_paths(0)
# print(f'Length of Traversal Path: {len(traversal_path)}\n\n')

def adventure(world, traversal_path):
    def unknown_path(graph):
        for k in graph:
            if '?' in graph[k].values():
                return True
        return False

    def find_move(visited, current_room):
        curr_room = current_room.id
        room_exits = visited[curr_room]
        for direction in room_exits:
            if room_exits[direction] == '?' and current_room.get_room_in_direction(direction).id not in visited:
                return direction
        return None

    def find_room(traversal_path, visited, curr_room, stack, reverse):
        while True:
            next_move = stack.pop()
            traversal_path.append(next_move)
            next_room = curr_room.get_room_in_direction(next_move)
            if '?' in visited[next_room.id].values():
                return next_room.id
            curr_room = next_room

    s = Stack()
    curr = 0
    visited = {0: {}}
    curr_room = world.rooms[curr]
    backwords = {'n':'s', 'e':'w', 's':'n', 'w':'e'}
    for direction in curr_room.get_exits():
        visited[curr_room.id][direction] = '?'
    while len(visited) < len(world.rooms) and unknown_path(visited):
        curr_room = world.rooms[curr]
        if curr_room not in visited:
            visited[curr_room.id] = {}
            for direction in curr_room.get_exits():
                visited[curr_room.id][direction] = '?'
        next_move = find_move(visited, curr_room)
        if not next_move:
            curr = find_room(traversal_path, visited, curr_room, s, backwords)
        else:
            traversal_path.append(next_move)
            next_room = curr_room.get_room_in_direction(next_move)
            visited[curr][next_move] = next_room.id
            if next_room.id not in visited:
                visited[next_room.id] = {}
                for direction in next_room.get_exits():
                    visited[next_room.id][direction] = '?'
            visited[next_room.id][backwords[next_move]] = curr_room.id
            s.push(backwords[next_move])
            curr = next_room.id

print(adventure(world, traversal_path))
print(traversal_path)

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
