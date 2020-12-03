from getinputdata import get_input_data

def part2():

    valid_password = 0
    for password in get_input_data():
        p_range = password[0]
        index_a, index_b = p_range.split('-')
        p_critera = password[1].replace(':','')
        passw = password[2].replace('\n','')

        if (passw[int(index_a)-1] == p_critera) ^ (passw[int(index_b)-1] == p_critera):
            valid_password += 1

        # for p in passw:
        #     if p == p_critera:
        #         p_count += 1
        # if int(min_p) <= p_count and p_count <= int(max_p):
        #     valid_password += 1
    print(valid_password)




if __name__ == "__main__":
    part2()