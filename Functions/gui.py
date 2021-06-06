#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSlider, \
    QLineEdit, QComboBox, QTextEdit, QCheckBox, QRadioButton, QButtonGroup, QDialog
from PyQt5.QtCore import Qt
import json

ws_point1 = (-15, 12)
ws_point2 = (15, 28)

font_width = 3
font_len_wid_ratio = 1.667 #5/3
database_start_coords = (0, 20, 8)

start_right = 3
start_up = 5

gap = 1

from draw_letter import Draw
import user_input


class GUI(QMainWindow):
    def __init__(self):
        """
        """
        self.ws_point1 = (-15, 12)
        self.ws_point2 = (15, 28)

        self.font_width = 3
        self.font_len_wid_ratio = 1.667  # 5/3
        self.database_start_coords = (0, 20, 8)

        self.start_right = 3
        self.start_up = 5

        self.gap = 1
        """
        Initial Setup
        Create Window
        Set Title
        """
        super(GUI, self).__init__()
        self.setWindowTitle('Set Values')

        """
        Central Widget
        layouts
        Add Widget
        # shape and size
        # sub windows   
        """
        widget = QWidget()
        self.setCentralWidget(widget)

        outside_layout = QVBoxLayout()
        widget.setLayout(outside_layout)

        layout = QVBoxLayout()
        outside_layout.addLayout(layout)

        # workspace
        ws_layout = QVBoxLayout()
        ws_heading = QVBoxLayout()
        ws_options = QVBoxLayout()

        ws_layout.addLayout(ws_heading)
        ws_layout.addLayout(ws_options)
        layout.addLayout(ws_layout)

        # Font layout
        font_layout = QVBoxLayout()
        font_heading = QVBoxLayout()
        font_options = QVBoxLayout()

        font_layout.addLayout(font_heading)
        font_layout.addLayout(font_options)
        layout.addLayout(font_layout)

        # Start space
        starting_layout = QVBoxLayout()
        starting_heading = QVBoxLayout()
        starting_options = QVBoxLayout()
        #
        starting_layout.addLayout(starting_heading)
        starting_layout.addLayout(starting_options)
        layout.addLayout(starting_layout)

        # Gap between letters space
        gap_layout = QVBoxLayout()
        gap_heading = QVBoxLayout()
        gap_options = QVBoxLayout()

        gap_layout.addLayout(gap_heading)
        gap_layout.addLayout(gap_options)
        layout.addLayout(gap_layout)

        # Radio Button Groups
        ws_group = QButtonGroup(widget)
        font_group = QButtonGroup(widget)
        starting_group = QButtonGroup(widget)
        gap_group = QButtonGroup(widget)

        """
        Vertical separations of all options
        """
        self.ws_label = QLabel('Select workspace size:')
        ws_heading.addWidget(self.ws_label)

        self.font_label = QLabel('Select font size:')
        font_heading.addWidget(self.font_label)

        self.starting_label = QLabel('Select start spacing:')
        starting_heading.addWidget(self.starting_label)

        self.gap_label = QLabel('Select spacing between letters:')
        gap_heading.addWidget(self.gap_label)

        """
        WorkSpace layout
        """
        self.ws_user_input = QRadioButton('Input in cms:')
        ws_group.addButton(self.ws_user_input)
        ws_options.addWidget(self.ws_user_input)

        self.ws_user_input_text = QLineEdit("")
        ws_options.addWidget(self.ws_user_input_text)

        self.ws_or_label = QLabel("OR")
        ws_options.addWidget(self.ws_or_label)

        self.ws_default = QRadioButton('Default:')
        ws_group.addButton(self.ws_default)
        ws_options.addWidget(self.ws_default)

        self.ws_default_text = QLineEdit("Corner 1: {} Corner 2: {}".format(self.ws_point1, self.ws_point2))
        self.ws_default_text.setReadOnly(True)
        ws_options.addWidget(self.ws_default_text)

        """
        Font layout
        """
        self.font_user_input = QRadioButton('Input in cms: Width, Ratio of length/width')
        font_group.addButton(self.font_user_input)
        font_options.addWidget(self.font_user_input)

        self.font_user_input_text = QLineEdit("")
        font_options.addWidget(self.font_user_input_text)

        self.font_or_label = QLabel("OR")
        font_options.addWidget(self.font_or_label)

        self.font_default = QRadioButton('Default:')
        font_group.addButton(self.font_default)
        font_options.addWidget(self.font_default)

        self.font_default_text = QLineEdit("Width: {} Ratio: {}".format(self.font_width, self.font_len_wid_ratio))
        self.font_default_text.setReadOnly(True)
        font_options.addWidget(self.font_default_text)

        """
        Start layout
        """
        self.starting_user_input = QRadioButton('Input in cms: Distance from Right boundary, Upper boundary')
        starting_group.addButton(self.starting_user_input)
        starting_options.addWidget(self.starting_user_input)

        self.starting_user_input_text = QLineEdit("")
        starting_options.addWidget(self.starting_user_input_text)

        self.starting_or_label = QLabel("OR")
        starting_options.addWidget(self.starting_or_label)

        self.starting_default = QRadioButton('Default:')
        starting_group.addButton(self.starting_default)
        starting_options.addWidget(self.starting_default)

        self.starting_default_text = QLineEdit("Distance from Right boundary: {} Upper boundary: {}".format(self.start_right, self.start_up))
        self.starting_default_text.setReadOnly(True)
        starting_options.addWidget(self.starting_default_text)

        """
        Gap layout
        """
        self.gap_user_input = QRadioButton('Input in cms: Gap')
        gap_group.addButton(self.gap_user_input)
        gap_options.addWidget(self.gap_user_input)

        self.gap_user_input_text = QLineEdit("")
        gap_options.addWidget(self.gap_user_input_text)

        self.gap_or_label = QLabel("OR")
        gap_options.addWidget(self.gap_or_label)

        self.gap_default = QRadioButton('Default:')
        gap_group.addButton(self.gap_default)
        gap_options.addWidget(self.gap_default)

        self.gap_default_text = QLineEdit("{}".format(self.gap))
        self.gap_default_text.setReadOnly(True)
        gap_options.addWidget(self.gap_default_text)

        """
        Connect
        """
        self.ws_user_input.toggled.connect(lambda: self.connect_text_box(self.ws_user_input_text, 'WS'))
        self.font_user_input.toggled.connect(lambda: self.connect_text_box(self.font_user_input_text, 'FONT'))
        self.starting_user_input.toggled.connect(lambda: self.connect_text_box(self.starting_user_input_text, 'START'))
        self.gap_user_input.toggled.connect(lambda: self.connect_text_box(self.gap_user_input_text, 'GAP'))

        # self.ws_user_input_text.editingFinished(lambda: self.parse_text('WS'))
        # self.font_user_input_text.editingFinished(lambda: self.parse_text('FONT'))
        # self.starting_user_input_text.editingFinished(lambda: self.parse_text('START'))
        # self.gap_user_input_text.editingFinished(lambda: self.parse_text('GAP'))

        self.name_to_draw_lab = QLabel('Enter Word to Draw')
        outside_layout.addWidget(self.name_to_draw_lab)

        self.name_to_draw = QLineEdit('')
        outside_layout.addWidget(self.name_to_draw)
        self.name_to_draw.editingFinished.connect(self.save_word)

        """
        Done Button
        """
        self.done_button = QPushButton('OK')
        outside_layout.addWidget(self.done_button)
        self.done_button.clicked.connect(self.update_options)

    def save_word(self):
        self.save_text = list(self.sender().text())

    def connect_text_box(self, text_box_with_it, string_to_tell_what_it_is):
        option = self.sender()
        if option.isChecked():
            print("HELLO {}".format(text_box_with_it))
            text_box_with_it.editingFinished.connect(lambda: self.parse_text(string_to_tell_what_it_is))

    def parse_text(self, string_with_it):
        if string_with_it == 'WS':
            text_box = self.sender()
            text = text_box.text().split(',')
            print(text)
            self.ws_point1 = (float(text[0]), float(text[1]))
            self.ws_point2 = (float(text[2]), float(text[3]))
        elif string_with_it == 'FONT':
            text_box = self.sender()
            text = text_box.text().split(',')
            print(text)
            self.font_width = float(text[0])
            self.font_len_wid_ratio = float(text[1])
        elif string_with_it == 'START':
            text_box = self.sender()
            text = text_box.text().split(',')
            print(text)
            self.start_right = float(text[0])
            self.start_up = float(text[1])
        else:
            text_box = self.sender()
            text = text_box.text()
            print(text)
            self.gap = float(text)

    def update_options(self):
        pass

    def convert_to_dict(self, text_to_add):
        new_dict = {}
        print("FULL TEXT:", text_to_add)
        for text in text_to_add:
            new_text = text.split(":")
            print("NEW TEXT:", new_text)
            new_text[1] = new_text[1].replace('[','')
            new_text[1] = new_text[1].replace(']', '')
            float_vals = new_text[1].split(",")
            print("FLOAT VALS:", float_vals)
            for vals in range(0, len(float_vals)):
                float_vals[vals] = float(float_vals[vals])
            new_dict.update({new_text[0]: float_vals})
        # print("Text to add: {} \nKey value split: {} \nfloats: {}\n".format(text_to_add, new_text, float_vals))
        return new_dict

if __name__ == '__main__':
    app = QApplication([])

    interface = GUI()

    interface.show()

    app.exec_()

    word_to_draw = interface.save_text #user_input.take_user_input()
    workspace_limits = [interface.ws_point1,  interface.ws_point2]
    letter_bounding_box = (interface.font_width, interface.font_len_wid_ratio, (0, 20, 8))
    gap_btw_letters = interface.gap
    distance_from_boundaries = (interface.start_right, interface.start_up)

    trial_draw = Draw(word_to_draw, workspace_limits, letter_bounding_box, gap_btw_letters, distance_from_boundaries)

    # start_at = trial_draw.det_coords_all_letters()
    # print("START", start_at)

    # trial_draw.make_input_coords_dict()
    # print("LOCAL", trial_draw.list_of_chars, trial_draw.local_coords_dict)

    final_dict = trial_draw.transform_coords_to_start_pos()
    print("REPAIRED:", final_dict)
