from getexpenses import get_expenses

def oh_of_N():
    array_of_expenses = get_expenses()
    TARGET = 2020
    foward = 0
    reverse = len(array_of_expenses)-1

    while(True):
        A = array_of_expenses[foward]
        B = array_of_expenses[reverse]
        SUM = A + B
        if SUM == TARGET:
            print(f"The Answer: {A * B}\nThe numbers: {A, B}")
            return
        elif SUM < TARGET:
            foward+=1
        elif SUM > TARGET:
            reverse-=1

if __name__ == "__main__":
    # Right And proper solution
    oh_of_N()

