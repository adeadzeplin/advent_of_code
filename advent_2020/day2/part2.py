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
<<<<<<< HEAD
    return valid_password
=======
    print(valid_password)
>>>>>>> 8112c2319992719e5d73961d04d58d409f9e0a0f




if __name__ == "__main__":
<<<<<<< HEAD
    print(part2())
=======
    part2()
>>>>>>> 8112c2319992719e5d73961d04d58d409f9e0a0f
