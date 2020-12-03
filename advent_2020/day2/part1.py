from getinputdata import get_input_data
<<<<<<< HEAD
import time
=======

>>>>>>> 8112c2319992719e5d73961d04d58d409f9e0a0f
def part1():

    valid_password = 0
    for password in get_input_data():
        p_range = password[0]
        min_p, max_p = p_range.split('-')
        p_critera = password[1].replace(':','')
        passw = password[2].replace('\n','')
        p_count = 0
        for p in passw:
<<<<<<< HEAD
            # print(p)
=======
>>>>>>> 8112c2319992719e5d73961d04d58d409f9e0a0f
            if p == p_critera:
                p_count += 1
        if int(min_p) <= p_count and p_count <= int(max_p):
            valid_password += 1
<<<<<<< HEAD
    return valid_password
    # print(valid_password)
=======
    print(valid_password)
>>>>>>> 8112c2319992719e5d73961d04d58d409f9e0a0f




if __name__ == "__main__":
<<<<<<< HEAD
    start_time = time.time()
    print(part1())
    print("--- %s seconds ---" % (time.time() - start_time))
=======
    part1()
>>>>>>> 8112c2319992719e5d73961d04d58d409f9e0a0f
