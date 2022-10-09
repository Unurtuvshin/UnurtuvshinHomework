import numpy as np

my_list = np.random.random_integers(50, 60, 20)
my_list = my_list.tolist()

# Step 1 - odd


def func(x): return (x % 2 == 1)


list_1 = list(filter(func, my_list))

# Step 2 - even


def func(x): return (x % 2 == 0)


list_2 = list(filter(func, my_list))

# Step 3 - multiply by 10

list_3 = [i*10 for i in my_list]

# Step 4 - '-1' from odd


def func(x): return (x % 2 == 1)


list_4 = [i-1 if np.mod(i, 2) == 1 else i for i in my_list]

# Step 5 - <52; 53-55; 56-58; >59

for i in my_list:
    if i < 52:
        print('<52')
    elif i < 55:
        print('53-55')
    elif i < 58:
        print('56-58')
    else:
        print('>59')

# Step 6 - until above 58

i = 0
while my_list[i] <= 58:
    print(my_list[i])
    i += 1

# Step 7 - print first 5

i = 0
while i < 5:
    print(my_list[i])
    i += 1
