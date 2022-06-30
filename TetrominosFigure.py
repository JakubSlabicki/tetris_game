from pygame import draw
from math import sin, cos, radians


# Class for Tetrominoss Figure
class TetrominossFigure:
    def __init__(self, ini_map, start_x=315, start_y=75, ini_type=1):
        # Input variables
        self.global_map = ini_map
        self.x = start_x
        self.y = start_y
        self.type = ini_type

        # Variables needed for object drowing
        self.color = None
        self.positions = []
        self.x2, self.y2 = None, None
        self.x3, self.y3 = None, None
        self.x4, self.y4 = None, None
        self.angle = 0
        self.size = 20

        # Variable needed for updating position
        self.speed_x = 25.0
        self.speed_y = 25.0
        self.default_angle = 90

        # Variable needed for defining object state
        self.mapped = False

    # Function
    # Updating object Y position
    def update_y_pos(self):
        # Temp variable for checking if move or rotation is not outside borders
        _out_of_box = False

        # For every y positions check border
        for pos_x, pos_y in self.positions:
            _y_attempt = pos_y + self.speed_y

            # Check if y attempt is in global map of all objects
            if len(self.global_map.map) > 0:
                for pos, color in self.global_map.map:
                    if pos[1] == _y_attempt and pos[0] == pos_x:
                        _out_of_box = True

            # Check if y attempt is outside border set temp variable
            if not self.global_map.border_y[0] < _y_attempt < self.global_map.border_y[1]:
                _out_of_box = True

        # Check if attempt in global map or outside border stop and map object
        if _out_of_box:
            self.mapped = True
            self.global_map.add_to_map(self.positions, self.color)
        else:
            self.y += self.speed_y

    # Function
    # Updating object X position and angle
    def update_x_angle_pos(self, dir_move, dir_angle):
        # Temp variable for checking if move or rotation is not outside borders
        _out_of_box = False

        # Check rotation and update all positions for border checking
        if dir_angle:
            self.angle += self.default_angle * dir_angle
            self.types()

        # For every x positions check border
        for pos_x, pos_y in self.positions:
            _x_attempt = pos_x + self.speed_x * dir_move
            # Check if x attempt is outside border set temp variable
            if not self.global_map.border_x[0] < _x_attempt < self.global_map.border_x[1]:
                _out_of_box = True

        # Check if temp variable is set then update move and/or rotation
        if not _out_of_box:
            self.x += self.speed_x * dir_move
        else:
            if dir_angle:
                self.angle -= self.default_angle * dir_angle

    # Function
    # Defining object shape and color
    def types(self):
        # Calc sin and cos for current angle using math lib
        _sin = sin(radians(self.angle))
        _cos = cos(radians(self.angle))

        # Calc all x,y positions based on current angle
        # Type 1:       X
        #           X X X
        if self.type == 1:
            self.color = (0, 0, 255)
            self.x2 = self.x + 25 * _cos
            self.y2 = self.y + 25 * _sin
            self.x3 = self.x + 25 * _cos - 25 * _sin
            self.y3 = self.y - 25 * _sin + 25 * _cos
            self.x4 = self.x - 25 * _cos
            self.y4 = self.y - 25 * _sin
        # Type 2:
        #           X X X X
        if self.type == 2:
            self.color = (255, 0, 0)
            self.x2 = self.x + 25 * _cos
            self.y2 = self.y + 25 * _sin
            self.x3 = self.x + 50 * _cos
            self.y3 = self.y + 50 * _sin
            self.x4 = self.x + 75 * _cos
            self.y4 = self.y + 75 * _sin
        # Type 3:     X
        #           X X X
        if self.type == 3:
            self.color = (0, 255, 0)
            self.x2 = self.x + 25 * _cos
            self.y2 = self.y + 25 * _sin
            self.x3 = self.x - 25 * _sin
            self.y3 = self.y + 25 * _cos
            self.x4 = self.x - 25 * _cos
            self.y4 = self.y - 25 * _sin
        # Type 4:     X X
        #           X X
        if self.type == 4:
            self.color = (200, 100, 0)
            self.x2 = self.x + 25 * _sin
            self.y2 = self.y - 25 * _cos
            self.x3 = self.x + 25 * _cos
            self.y3 = self.y + 25 * _sin
            self.x4 = self.x + 25 * _cos - 25 * _sin
            self.y4 = self.y + 25 * _cos + 25 * _sin
        # Type 5:   X X
        #           X X
        if self.type == 5:
            self.color = (10, 10, 10)
            self.x2 = self.x + 25 * _cos
            self.y2 = self.y + 25 * _sin
            self.x3 = self.x + 25 * _sin
            self.y3 = self.y + 25 * _cos
            self.x4 = self.x + 25 * _cos + 25 * _sin
            self.y4 = self.y + 25 * _cos + 25 * _sin

        # Update positions based on calculated x,y pars
        self.positions = [[self.x, self.y],
                          [self.x2, self.y2],
                          [self.x3, self.y3],
                          [self.x4, self.y4]]

    # Function
    # Drowing object with udpated angle
    def draw(self, window_display):
        # Update all object positions based on current angle
        self.types()

        # Draw all 4 rectangles using pygame lib
        for pos_x, pos_y in self.positions:
            draw.rect(window_display, self.color, ((pos_x, pos_y), (self.size, self.size)))
