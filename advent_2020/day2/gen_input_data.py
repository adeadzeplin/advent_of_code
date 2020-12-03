ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','o','m','n','p','q','r','s','t','u','v','w','x','y','z']
NUM_OF_PASSWORDS = 10000
import numpy as np
import random
def gen_input_data():
    input_data = ''
    for data in range(NUM_OF_PASSWORDS):
        critera_c = ALPHABET[np.random.randint(0,25)]
        letter_count = np.random.randint(2, 200)
        
        count_of_crit = np.random.randint(0, letter_count)
        word = ''
        for c in range(count_of_crit):
            word += critera_c
        for l in range(letter_count-count_of_crit):
            word += ALPHABET[np.random.randint(0,25)]
        dorw = ''.join(random.sample(word, len(word)))

        if len(dorw)==2:
            first_index = 1
            secon_index = 2

        else:
            first_index = (np.random.randint(1, len(dorw) - 1))
            secon_index = np.random.randint(first_index+1, len(dorw))

        # print()


        input_data += f"{first_index}-{secon_index} {critera_c}: {dorw}\n"
        

    input_file = open("input.txt", "w")
    input_file.write(input_data)
    input_file.close()
    # return input_data

if __name__ == "__main__":
    gen_input_data()
'1-3 a: abcde\n'
