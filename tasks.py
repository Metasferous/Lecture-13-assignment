"""
 1. Create add method to add two countries together.
 This method should create another country object with the name of the two
 countries combined and the population of the two countries added together.

    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)
    bosnia_herzegovina = bosnia.add(herzegovina)
    bosnia_herzegovina.population -> 15_000_000
    bosnia_herzegovina.name -> 'Bosnia Herzegovina'
"""


class Country_1:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        if type(other) != Country_1:
            return TypeError('other must be a Country_1 instance too!')

        return Country_1(self.name + ' ' + other.name,
                         self.population + other.population)


def check_1():
    bosnia = Country_1('Bosnia', 10_000_000)
    herzegovina = Country_1('Herzegovina', 5_000_000)
    bosnia_herezegovina = bosnia.add(herzegovina)
    expected_name = 'Bosnia Herzegovina'
    expected_population = 15_000_000

    assert bosnia_herezegovina.name == expected_name
    assert bosnia_herezegovina.population == expected_population
    pass


check_1()


"""
 2. Implement the previous method with a magic method

    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)
    bosnia_herzegovina = bosnia + herzegovina
    bosnia_herzegovina.population -> 15_000_000
    bosnia_herzegovina.name -> 'Bosnia Herzegovina'
"""


class Country_2:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        if type(other) != Country_2:
            return TypeError('other must be a Country_2 instance too!')

        return Country_2(self.name + ' ' + other.name,
                         self.population + other.population)


def check_2():
    bosnia = Country_2('Bosnia', 10_000_000)
    herzegovina = Country_2('Herzegovina', 5_000_000)
    bosnia_herezegovina = bosnia + herzegovina
    expected_name = 'Bosnia Herzegovina'
    expected_population = 15_000_000

    assert bosnia_herezegovina.name == expected_name
    assert bosnia_herezegovina.population == expected_population
    pass


check_2()


"""
 3. Create a Car class with the following attributes:
 brand, model, year, and speed.

 The Car class should have the following methods:
 accelerate, brake and display_speed.

 The accelerate method should increase the speed by 5,
 and the brake method should decrease the speed by 5.
 Remember that the speed cannot be negative.
"""


class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def display_speed(self):
        print(self.speed)


def check_3():
    car = Car('Range Rover', 'Velar S', 2023, 210)
    assert car.speed == 210

    car.accelerate()
    assert car.speed == 215

    car.brake()
    assert car.speed == 210
    car.display_speed()


check_3()


"""
 4. Create a Robot class with the following attributes:
 orientation (left, right, up, down),
 position_x,
 position_y.

 The Robot class should have the following methods:
 move,
 turn,
 and display_position.

 The move method should take a number of steps
 and move the robot in the direction it is currently facing.

 The turn method should take a direction (left or right)
 and turn the robot in that direction.

 The display_position method should print the current position of the robot.

    I assume x axis is horizontal and points to right,
    and y axis is vertical and points upwards.
"""

# x and y values representing unit vectors,
# left/right for orientations after turns
# it could also be calculated by using rotation matrices
# but there are pretty limited amount of states
# so I've decided just to hardcode them for a better readability
DIRECTIONS = {
    'left': {
        'x': -1,
        'y': 0,
        'left': 'down',
        'right': 'up'},
    'right': {
        'x': 1,
        'y': 0,
        'left': 'up',
        'right': 'down'},
    'up': {
        'x': 0,
        'y': 1,
        'left': 'left',
        'right': 'right'},
    'down': {
        'x': 0,
        'y': -1,
        'left': 'right',
        'right': 'left'}
}

TURNS = ['left', 'right']


class Robot:
    def __init__(self, orientation, position_x, position_y):
        if orientation in DIRECTIONS:
            self.orientation = orientation
        else:
            self.orientation = 'up'
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps=1):
        self.position_x += DIRECTIONS[self.orientation]['x'] * steps
        self.position_y += DIRECTIONS[self.orientation]['y'] * steps

    def turn(self, turn: str):
        if turn in TURNS:
            self.orientation = DIRECTIONS[self.orientation][turn]
        else:
            return ValueError('Incorrect turn direction')

    @property
    def position(self):
        return (self.position_x, self.position_y)

    def display_position(self):
        print(self.position)


def check_4():
    robot = Robot('right', 0, 0)

    robot.move()
    assert robot.position == (1, 0)

    robot.turn('left')
    assert robot.orientation == 'up'

    robot.move(5)
    assert robot.position == (1, 5)
    robot.display_position()


check_4()
