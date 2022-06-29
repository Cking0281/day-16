from turtle import Turtle, Screen
from prettytable import PrettyTable


def main():
    # timmy = Turtle()
    # print(timmy)
    # timmy.shape("turtle")
    # timmy.color("coral")
    # timmy.forward(100)
    #
    # my_screen = Screen()
    # print(my_screen.canvheight)
    # my_screen.exitonclick()
    table = PrettyTable()
    table.align = "l"
    table.field_names = ["Pokemon Name", "Type"]
    table.add_row(["Pikachu", "Electric"])
    table.add_row(["Squirtle", "Water"])
    table.add_row(["Charmander", "Fire"])
    print(table)


if __name__ == "__main__":
    main()
