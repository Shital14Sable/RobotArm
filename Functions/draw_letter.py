#!/usr/bin/env python3

import numpy as np
import user_input
import pickle
import os.path
from os import path


class Draw:
    """
    This class draws the letters provided by the user input,
    taking into account workspace area and spacing between letters
    """
    def __init__(self, list_of_chars, boundary_limits, letter_limits, gap, start_spacing):
        """
        Saves the input into a class attribute
        :param list_of_chars: Ex: ['a', 'p', 'p', 'l', 'e']
        :param boundary_limits: [(x1, y1), (x2, y2)] Boundary inside which user input has to fit .
        (x1, y1): bottom left coordinates, (x2, y2): Upper right coordinates
        boundary_limits values should be in terms of robots coordinate system, in cms
                 _______________.(x2, y2)
                |                |
                |                |
                |._______________|
        (x1, y1)

        :param  letter_limits: (breadth, ratio, (x, y, z) Bounding box inside which every letter will be written.
        breadth = breadth of box (cms), ratio = length:breadth, (x, y, z): Origin coordinates of bounding box (in terms of
        world coordinates)
        :param gap: gap we want to leave between letters (in cms).
        :param start_spacing: (r, u) What space we want to maintain from the right and upper boundary (in cms) (we are writing
        upside-down). NO NEGATIVE VALUES. JUST A MEASURE OF LENGTH
        """
        self.list_of_chars = list_of_chars
        self.num_of_chars = len(list_of_chars)
        self.boundary_limits = boundary_limits
        self.x1 = boundary_limits[0][0]
        self.y1 = boundary_limits[0][1]
        self.x2 = boundary_limits[1][0]
        self.y2 = boundary_limits[1][1]

        # left is towards x1, right is towards x2, upper is towards y2, lower is towards y1
        self.mid_upper = (self.x1 + (self.x2 - self.x1)/2, self.y2)
        self.mid_lower = (self.mid_upper[0], self.y1)
        self.mid_left = (self.x1, self.y1 + (self.y2 - self.y1)/2)
        self.mid_right = (self.x2, self.y1 + (self.y2 - self.y1)/2)
        self.start_coords = (10, 20)

        self.letter_width = letter_limits[0]
        self.letter_len = letter_limits[1]*self.letter_width
        self.letter_origin = letter_limits[2]

        self.all_coords_dict = {}

        self.gap = gap

        self.start_spacing = start_spacing

        self.local_coords_dict = {}

    def _det_start_coords(self):
        """
        This method decides where to start drawing based on the mid points
        :return: self.start_coords : Coords to start writing from
        """
        self.start_spacing = (abs(self.start_spacing[0]), abs(self.start_spacing[1]))
        space_r = self.start_spacing[0]
        space_up = self.start_spacing[1]
        x_start = self.x2 - space_r
        y_start = self.y2 - space_up
        self.start_coords = (x_start, y_start)

        return self.start_coords

    def det_coords_all_letters(self):
        """
        This function returns a dict which is of the same length as the number of characters.
        The list consists of starting coordinates of every letter that needs to be drawn, with the correct spacing
        :return: self.all_coords_dict: Dictionary of starting coords of each letter
        """
        self.all_coords_dict = {}
        for i in range(0, self.num_of_chars):
            if i == 0:
                (x_start, y_start) = self._det_start_coords()
                (x, y) = (x_start, y_start)

            else:
                y = y_start
                x = x - self.letter_width - self.gap
            if x <= self.x1:
                print("Going out of boundary for {}th letter! Please change conditions and restart".format(i+1))
                raise ValueError
            self.all_coords_dict.update({i: [self.list_of_chars[i], (x,y)]})

        return self.all_coords_dict

    def transform_coords_to_start_pos(self):
        """
        This method takes in the letter path and tranforms the coordinates  in the  path in to the location they should
        start from
        :return: new_array: New numpy array of coordinates in terms of start coordinates
        """
        self.make_input_coords_dict()
        self.det_coords_all_letters()
        for i in range(0, self.num_of_chars):
            start_coords = [self.all_coords_dict[i][1][0], self.all_coords_dict[i][1][1], 0]
            add_to_array = np.asarray(start_coords) - np.asarray(self.letter_origin)
            new_array = np.asarray(self.local_coords_dict[self.list_of_chars[i]]) + add_to_array
            # new_array = letter_array[i] + add_to_array
            self.all_coords_dict[i].append(new_array)

        return self.all_coords_dict

    def make_input_coords_dict(self):
        for letter in self.list_of_chars:
            print("LETTER: ", letter)
            fname = "/Users/asar/Desktop/ROB521/Project/ROB521-ArmWrite/Letters/letter_{}.npy".format(letter)
            if path.exists(fname):
                char_coords = np.load(fname)
                print("CHAR LOADED IN:", letter, fname)
                self.local_coords_dict.update({letter: char_coords})
            else:
                print("WTH?", fname)


if __name__ == '__main__':
    word_to_draw = user_input.take_user_input()
    workspace_limits = [(-15, 12), (15, 28)]
    letter_bounding_box = (3, 5/3, (0, 20, 8))
    gap_btw_letters = 1
    distance_from_boundaries = (3, 5)

    trial_draw = Draw(word_to_draw, workspace_limits, letter_bounding_box, gap_btw_letters, distance_from_boundaries)

    # start_at = trial_draw.det_coords_all_letters()
    # print("START", start_at)

    # trial_draw.make_input_coords_dict()
    # print("LOCAL", trial_draw.list_of_chars, trial_draw.local_coords_dict)

    final_dict = trial_draw.transform_coords_to_start_pos()
    print("REPAIRED:", final_dict)
