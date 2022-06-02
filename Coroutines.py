"""
                                            Coroutines
It executes half of the function(which takes longer time) ones and saves it and every time it is called
it will run from the other half hence reducing the execution time
"""

import time


def searcher():
    f = open("Book.txt", "a")
    f.write("Hello All!! I am Puja. I work in MetricStream as a developer\n")
    f.close()
    f = open("Book.txt")
    book = f.read()
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
            print("Text is present")
        else:
            print("Text is not present")


search = searcher()
next(search)
while True:
    n = input("Enter the word You want to search: ")
    search.send(n)
    c = input("Press q to quit or other keys to continue: ")
    if c == 'q':
        print("Exiting!!")
        exit()
    else:
        print("Search continues")
        continue
