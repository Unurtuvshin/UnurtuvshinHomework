import numpy as np


class myStrangeError1(Exception):
    print("Error here1")
class myStrangeError2(Exception):
    print("Error here2")


# Step 1 generate random 1000 integers
array = np.random.randint(-100, 100, size=1000)

subarr = []
# Step 2 look one by one
for i in array:
    try:
        if i < 0 and np.mod(i, 2) == 1:
            # Step 3 if negative odd, raise odd error
            raise myStrangeError1()
    except myStrangeError1:
        print("Odd error occured")
    try:
        if i >= 0:
            # Step 4 if positive, raise sign error
            raise myStrangeError2()
    except myStrangeError2:
        print("Sign error occured")
    if i < 0 and np.mod(i, 2) == 0:
        # Step 5 if negative even, append
        subarr.append(i)
print(subarr)
