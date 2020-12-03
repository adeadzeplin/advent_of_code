
def get_input_data():
    input_file = open("input.txt", "r")
    input_data = []
    for data in input_file:
        # print(data)
        input_data.append(data.split(' '))
    input_file.close()
    # input_data.sort()
    return input_data

'1-3 a: abcde'