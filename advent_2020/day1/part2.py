from getexpenses import get_expenses

def oh_N():
    array_of_expenses = get_expenses()

    TARGET = 2020

    for x in array_of_expenses:
        for y in array_of_expenses:
            for z in array_of_expenses:

                if x + y + z == TARGET:

                    print(f"The Answer: {(x * y * z)}\nThe numbers: {x, y, z}\nSUM {x + y + z}")


if __name__ == "__main__":
    # Right And proper solution
    oh_N()
