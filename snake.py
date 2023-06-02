from turtle import Turtle
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.wall_segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.build_border_wall()

    def create_snake(self):
        xstart = 0
        for i in range(1,4):
            if i > 1:
                xstart -= 20
            t1 = Turtle("square")
            if i == 1:
                t1.color("green")
            else:
                t1.color("white")
            t1.penup()
            t1.setposition(xstart, 0)
            self.segments.append(t1)


    def move_snake(self, direction):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        
        if direction == "right":
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)
        elif direction == "up":
            if self.head.heading() != DOWN:
                self.head.setheading(UP)
        elif direction == "left":
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)
        elif direction == "down":
            if self.head.heading() != UP:
                self.head.setheading(DOWN)
        
        if direction == "forward":
            self.head.forward(MOVE_DISTANCE)
        
        if self.wall_check(new_x, new_y):
            # Hitting a wall, Snake Game Ends.
            # Snake is no longer moving.
            return False
        else:
            return True


    def wall_check(self, xcor, ycor):
        # print(f"x,y: {xcor},{ycor}")
        # Returning True says, I hit a wall.
       
        # Wall segments
        if xcor >= 280 or xcor <= -300:
            return True
        if ycor >= 300 or ycor <= -280:
            return True
            
        # Snake segments
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
    

    def add_segment(self):
        t1 = Turtle("square")
        t1.color("white")
        t1.penup()
        t1.speed("fastest")
        self.segments.append(t1)

    
    def build_border_wall(self):
        # Top Border Wall
        xcor = -310
        ycor = 310
        for wall_segment in range(-320, 320, 20):
            t1 = Turtle("square")
            t1.color("red")
            t1.penup()
            t1.speed()
            t1.goto(xcor, ycor)
            xcor += 20
            self.wall_segments.append(t1)

        # Bottom Border Wall
        xcor = -310
        ycor = -300
        for wall_segment in range(-320, 320, 20):
            t2 = Turtle("square")
            t2.color("red")
            t2.penup()
            t2.speed()
            t2.goto(xcor, ycor)
            xcor += 20
            self.wall_segments.append(t2)

        # Left Border Wall
        xcor = -310
        ycor = 310
        for wall_segment in range(-320, 320, 20):
            t3 = Turtle("square")
            t3.color("red")
            t3.penup()
            t3.speed()
            t3.goto(xcor, ycor)
            ycor -= 20
            self.wall_segments.append(t3)

        # Right Border Wall
        xcor = 300
        ycor = 310
        for wall_segment in range(-320, 320, 20):
            t4 = Turtle("square")
            t4.color("red")
            t4.penup()
            t4.speed()
            t4.goto(xcor, ycor)
            ycor -= 20
            self.wall_segments.append(t4)


