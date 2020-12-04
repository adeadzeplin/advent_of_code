def get_data():
    input_file = open("input.txt", "r")
    data = []
    for dat in input_file:
        data.append(dat.replace('\n',''))
    input_file.close()
    return data