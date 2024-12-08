from turtledemo.penrose import start







if __name__  == "__main__":
    numbers = [1,0,4,2,6,2,4, 0]
    target = 11
    ind = binary_search(numbers, target)
    print(f"{target}: {ind}")