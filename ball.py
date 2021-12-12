from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.incrz_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # when boll touch wall
    def bounce_y(self):
        self.y_move *= -1

    # when boll touch right paddle
    def bounce_x(self):
        self.x_move *= -1
        # every time when the ball hit the paddle it Increases its speed
        self.incrz_speed *= 0.9

    # when the ball miss the paddle
    def reset_position(self):
        self.goto(0, 0)
        # when the paddle miss the ball the increased speed will come to the normal
        self.incrz_speed = 0.1
        self.bounce_x()
