from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
            
    def createsnake(self):
        x = 0
        y = 0
        for i in range(0,3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x,y)
            self.segments.append(new_segment)
            x -= 20
            
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
    
    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
        
    def Right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)
        
    def Left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
            
    def create_new_segment(self) :
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[len(self.segments)- 1].xcor(),self.segments[len(self.segments)- 1].ycor())   
        self.move()
        self.segments.append(new_segment)
        
    def is_collision(self):
        for segments in self.segments[1:]:
            if (self.head.distance(segments) < 10 ) : 
                    return True
        return False
    
    def reset(self):
        for segment in self.segments:
            segment.goto(2000,2000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
        