import time
from part1 import *
from part2 import *
import numpy as np

def main():
    times_list = []
    for i in range(10):
        start_time = time.time()
        part1()
        part2()
        times_list.append(time.time() - start_time)
        print(i)
    print(f"Average Time: {np.average(times_list)} \nMedian Time: {np.median(times_list)}" )

if __name__ == "__main__":
   main()