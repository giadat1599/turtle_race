import turtle as T
from random import randint

end_race = False
screen = T.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, len(colors)):
    turtle = T.Turtle("turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle)

while not end_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            end_race = True
        turtle.forward(randint(0, 10))


screen.exitonclick()
