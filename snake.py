from turtle import Turtle
move_distance=20
starting_position=[(0,0),(-20,0),(-40,0)]


up=90
down=270
left=180
right=0


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for position in starting_position:
            new_segment=Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)
    
    def up(self):
        if self.head.heading()==down:
             self.head.setheading(down)
        self.head.setheading(up)

    
    def left(self):
        self.head.setheading(left)
    
    def right(self):
        self.head.setheading(right)
    
    def down(self):
        if self.head.heading()==up:
            self.head.setheading(up)
        self.head.setheading(down)
