import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("Guess the cities of Kazakhstan!")
image = "kz_cities.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("cities.csv")
all_cities = data.city.to_list()

guessed_cities = 0
users_answer = []
game_on = True


missing_cities = []

while game_on:
    answer_city = screen.textinput(title=f"{guessed_cities}/17 Cities Correct", prompt="What's another city's name?").title()
    if answer_city == "Exit":
        for n in all_cities:
            if n not in users_answer:
                missing_cities.append(n)
        break
    if answer_city in all_cities:
        if answer_city not in users_answer:
            users_answer.append(answer_city)
            guessed_cities += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            city_data = data[data.city == answer_city]
            t.goto(int(city_data.x), int(city_data.y))
            t.write(city_data.city.item())
            if len(users_answer) == 49:
                game_on = False

cities_to_learn = pandas.DataFrame(missing_cities)
cities_to_learn.to_csv("cities_to_learn.csv")

