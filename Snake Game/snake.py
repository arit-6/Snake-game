from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]

    def create_snake(self):
        for t in START_POSITIONS:
            new_segments = Turtle("square")
            new_segments.color("white")
            new_segments.penup()
            new_segments.goto(t)
            self.segment.append(new_segments)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def add_segment(self, t):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(t)
        self.segment.append(new_segments)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]

    def extend(self):
        #add new segment
        self.add_segment(self.segment[-1].position())

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
