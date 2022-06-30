import pygame
import math


# Class for Map cointaing all Tetrominoss Figures
class TetrominosMap:
    def __init__(self):
        # Variables needed for mapped object drowing
        self.map = []
        self.list_y = []
        self.count_y = []

        # Variables needed for map updating and game score
        self.score = 0
        self.step = 0
        self.update_speed = 1

        # Variable needed for creating border for object
        self.border_x = [50, 630]
        self.border_y = [0, 630]

    # Function
    # Drawing all existing elemenst in map
    def draw_map(self, window_display):
        for pos, color in self.map:
            pygame.draw.rect(window_display, color, (pos, (20, 20)))

    # Function
    # Adding new object to map
    def add_to_map(self, mapping_positions, mapping_color):
        # Add every object from input to map array
        for pos_x, pos_y in mapping_positions:
            self.map.append([[pos_x, pos_y], mapping_color])

            # Check if y position exist
            if pos_y in self.list_y:
                # Increment count variable
                for i, arr in enumerate(self.count_y):
                    if pos_y == arr[0]:
                        self.count_y[i][1] += 1
            else:
                # Create new position and counter to arrays
                self.list_y.append(pos_y)
                self.count_y.append([pos_y, 1])

        # Try searching full row
        self.search_full_row()

    # Function
    # Check if row is full of elements
    def search_full_row(self):
        # Create temp arrays for deleting elements in arrays if full row exists
        _temp = self.map.copy()
        _del = []

        # Count amount of full row elements based on borders
        _full_row_count = int((self.border_x[1] - self.border_x[0]) / 25.0)

        # For every element in count array check if row is full
        for i, array in enumerate(self.count_y):
            if array[1] >= _full_row_count:

                # Append temp array with index of full row
                _del.append(i)
                iteration = 0

                # Check if element is in full row and pop
                for map_obj in self.map:
                    if map_obj[0][1] == array[0]:
                        _temp.pop(iteration)

                        # Check if element is in list array and if remove
                        if array[0] in self.list_y:
                            self.list_y.remove(array[0])

                    else:
                        iteration += 1

        # For every deleted element remove elements from arrays and get map down
        for _ in _del:
            self.map_down()
        self.map = _temp

    # Function
    # Get every element in map down
    def map_down(self):
        # Get every element in map down
        for i, arr in enumerate(self.map):
            self.map[i][0][1] = arr[0][1] + 25
        self.update_lists()

        # Increase score and speed if nessesery
        self.score += 20
        self.update_speed = math.ceil((self.score+1)/50)

    # Function
    # Rewrite arrays when elements in map pops
    def update_lists(self):
        # Erese arrays
        self.count_y = []
        self.list_y = []

        # For every element in map if exists in its
        for arr, color in self.map:
            if arr[1] in self.list_y:
                # Increment count variable
                for i, arr2 in enumerate(self.count_y):
                    if arr[1] == arr2[0]:
                        self.count_y[i][1] += 1
            else:
                # Add new position and counter to arrays
                self.list_y.append(arr[1])
                self.count_y.append([arr[1], 1])







