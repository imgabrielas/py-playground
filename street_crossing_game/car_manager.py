from turtle import Turtle
import random

CAR_COLORS = [
    "#FFB3BA",  # pastel pink
    "#FFDFBA",  # pastel peach
    "#FFFFBA",  # pastel yellow
    "#BAFFC9",  # pastel mint
    "#BAE1FF",  # pastel blue
    "#D7BAFF",  # pastel lavender
    "#C9F7E8",  # pastel aqua
    "#FFD6E8",  # blush pink
    "#E6E6FA",  # lavender
    "#B8F2E6",  # mint turquoise
    "#F9C5D1",  # rose
    "#CDE7BE",  # sage green
]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(CAR_COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 2