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
    # I didn't realize there was a part two to these problems untill after spending 4 hours on the stupid solution.
    # And accidentally left myself 30 min for the second part lol
    oh_N()
