import numpy as np

def exec_first():
    x = np.random.randint(20, size=100)
    print(x)

def exec_second():
    second_array = []
    print("Enter number or e to exit: ")
    while(True):
        key=input()
        if key.lower=="e":
            break
        else:
            try:
                value = int(key)
            except:
                print("Not a number")
        second_array.append(value)
    second_arraynp = np.array(second_array)
    second_arraynpodd = second_arraynp[second_arraynp%2==1]
    second_arraynpeven = second_arraynp[second_arraynp%2==0]
    print(second_arraynpodd)
    print(second_arraynpeven)
