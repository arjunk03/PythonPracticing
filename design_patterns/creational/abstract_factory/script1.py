import abc
import re


class Toy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass


class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show_color(self):
        pass


class Car(Toy):
    def show(self):
        print("Remote controlled Car")


class ActionFigure(Toy):
    def show(self):
        print("Action Figure")


class ConstructionToy(Toy):
    def show(self):
        print("Construction Toy")


class Red(Color):
    def show_color(self):
        print("Red Color")


class Blue(Color):
    def show_color(self):
        print("Blue Color")


class Green(Color):
    def show_color(self):
        print("Green Color")


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_toy(self):
        pass

    @abc.abstractmethod
    def get_color(self):
        pass


class ColorfulToyFactory(AbstractFactory):
    def get_toy(self, toy_type):
        if toy_type == None:
            return None

        if toy_type == "Car":
            return Car()
        elif toy_type == "ActionFigure":
            return ActionFigure()
        elif toy_type == "ConstructionToy":
            return ConstructionToy()
        return None

    def get_color(self, color_type):
        if color_type == None:
            return None

        if color_type == "Red":
            return Red()
        elif color_type == "Blue":
            return Blue()
        elif color_type == "Green":
            return Green()

        return None


car = Car()
red = Red()

car.show()
red.show_color()


RED_CAR = "red_car"
BLUE_LEGO = "blue_lego"
GREEN_ACTION_FIGURE = "green_action_figure"


class ColorfulToyProducer:
    __colorful_toy_factory = ColorfulToyFactory()

    @classmethod
    def get_toy_and_color(cls, choice):
        toy = None
        color = None

        if choice == RED_CAR:
            toy = cls.__colorful_toy_factory.get_toy("Car")
            color = cls.__colorful_toy_factory.get_color("Red")
        elif choice == BLUE_LEGO:
            toy = cls.__colorful_toy_factory.get_toy("ActionFigure")
            color = cls.__colorful_toy_factory.get_color("Blue")
        elif choice == GREEN_ACTION_FIGURE:
            toy = cls.__colorful_toy_factory.get_toy("ConstructionToy")
            color = cls.__colorful_toy_factory.get_color("Green")

        return toy, color


toy, color = ColorfulToyProducer.get_toy_and_color(RED_CAR)
print(toy, color)

toy, color = ColorfulToyProducer.get_toy_and_color(BLUE_LEGO)
print(toy, color)
toy, color = ColorfulToyProducer.get_toy_and_color(GREEN_ACTION_FIGURE)
print(toy, color)
