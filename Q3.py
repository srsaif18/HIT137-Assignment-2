# Group Members:
# Mou Rani Biswas - 398778
# MD Saifur Rahman - 398921
# Nahid Hasan Sangram - 395231
# Mohammed Rifatul Alam - 399533
#
# HIT137 Assignment 2
# Question 3 – Part 3 (Final): Recursive indentation applied to all polygon edges

import turtle


def get_positive_int(prompt):
    while True:
        try:
            v = int(input(prompt).strip())
            if v > 0:
                return v
            print("Enter a positive integer.")
        except ValueError:
            print("Enter a valid integer.")


def get_positive_float(prompt):
    while True:
        try:
            v = float(input(prompt).strip())
            if v > 0:
                return v
            print("Enter a positive number.")
        except ValueError:
            print("Enter a valid number.")


def indent_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    third = length / 3.0

    indent_edge(t, third, depth - 1)
    t.right(60)                # inward turn
    indent_edge(t, third, depth - 1)
    t.left(120)
    indent_edge(t, third, depth - 1)
    t.right(60)
    indent_edge(t, third, depth - 1)


def draw_recursive_polygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        indent_edge(t, length, depth)
        t.left(angle)


def main():
    sides = get_positive_int("Enter number of sides (e.g., 3, 4, 5): ")
    length = get_positive_float("Enter side length (pixels): ")
    depth = get_positive_int("Enter recursion depth (e.g., 0-5): ")

    screen = turtle.Screen()
    screen.title("Q3 - Recursive Polygon Indentation (Final)")

    t = turtle.Turtle()
    t.speed(0)

    # optional: center the drawing a bit (not required, just looks nicer)
    t.penup()
    t.goto(-length / 2, length / 2)
    t.pendown()

    draw_recursive_polygon(t, sides, length, depth)

    turtle.done()


if __name__ == "__main__":
    main()
