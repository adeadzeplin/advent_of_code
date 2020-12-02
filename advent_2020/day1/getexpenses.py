
def get_expenses():
    input_file = open("input.txt", "r")
    expenses = []
    for exp in input_file:
        expenses.append(int(exp.replace('\n','')))
    input_file.close()
    expenses.sort()
    return expenses