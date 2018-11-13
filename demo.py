from typing import List
from datetime import datetime
from random import randint

def collect_runtime(func):
    def timer(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        time = datetime.now() - start
        print(f"{func.__name__} takes {time.total_seconds()} to finish. \n")
    return timer

def generate_big_array_file():
    existed = set()
    with open("random_array", "w+") as file:
        for i in range(100000):
            r = 0
            while (r in existed):
                r = randint(0, 100001)
            else:
                file.write(f"{r} ")
                existed.add(r)

def get_array_from_file(file_name: str) -> List[int]:
    with open(file_name, "r") as file:
        Array = [int(i) for i in file.read().split()]
    return Array if len(Array) > 0 else []

@collect_runtime
def linear_search(A: List[int], key: int)-> None:
    n = len(A)
    for i in range(n):
        if A[i]==key:
            print(f"Key: {key} exists at {i}.\n")
            return
    print(f"Key: {key} doesn't appear in A.\n")

@collect_runtime
def binary_search(A: List[int], key: int)-> int:
    n = float(len(A))
    left = 0
    right = n
    count = 0
    while(left < right):
        pivot = int((left + right) /2)
        count += 1
        if A[pivot] == key:
            print(f"Key: {key} exists at {pivot} after {count} loop.\n")
            return
        elif A[pivot] < key:
            left = pivot + 1
        elif A[pivot] > key:
            right = pivot - 1
    print(f"Key: {key} doesn't appear in A\n")

@collect_runtime
def python_search_is_linear(A: List[int], key: int) -> None:
    if key in A:
        print(f"Key: {key} appears in A.\n")
    else:
        print(f"Key: {key} doesn't appear in A\n")
    return
generate_big_array_file()
array = get_array_from_file("random_array")
key = randint(min(array), max(array)) # Generate a random key
#array = [8, 3, 4, 2, 1, 5 ,6 ,7, 9, 10, 11 ,14, 15]
#key = 7

python_search_is_linear(array, key)
linear_search(sorted(array), key)
binary_search(sorted(array), key)
