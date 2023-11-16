import os
from numpy.random import randint
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def sort_the_nested_arrays(array):
    print("Here is an unsorted array:\n\n")
    for i in array:
        print(i)

    question = str(input("What do you want to sort?\n1 - columns\n2 - rows\n\nAnswer: "))
    if question == "1":
        clear_console()
        print("Here is an array with sorted columns:\n")

        start_time = time.time()
        for c in sort_the_columns(array):
            print(c)
        print("--- %s seconds ---" % (time.time() - start_time))

    elif question == "2":
        clear_console()
        print("Here is an array with sorted rows:\n")

        for column in sort_the_rows(array):
            print(column)

    return "\nProgram has ended up..."


def sort_the_columns(array):
    count = 0
    for i in range(len(array)):
        if count >= len(array[i]):
            break

        sorted_numbers = sorted([j[count] for j in array])
        for t in range(len(array)):
            array[t][count] = sorted_numbers[t]

        count += 1

    return array


def sort_the_rows(array):
    for i in range(len(array)):
        array[i] = sorted(array[i])

    return array


print(sort_the_nested_arrays([list(randint(0, 50, 100)) for i in range(1, 50)]))
