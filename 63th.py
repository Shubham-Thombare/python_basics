# Multithreading (used to perform multiple tasks at once(Multitasking)
# good for I/O bound tasks or fetching data from the APIs threading or internet.
# Thread(target=my_function))

import threading
import time

def walk_dog(first, last="Doo"):
    time.sleep(4)
    print(f"Walking the {first} {last}...")

def cook_food():
    time.sleep(5)
    print("Cooking food...")

def read_book():
    time.sleep(6)
    print("Reading a book...")
 
 # instead of thread, chore has been used
# to make it more relatable to the context of chores.

chore1 = threading.Thread(target=walk_dog, args=("Scooby",)) # comma is used to know the python it is tuple.
chore1.start()

chore2 = threading.Thread(target=cook_food) 
chore2.start()

chore3 = threading.Thread(target=read_book)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")