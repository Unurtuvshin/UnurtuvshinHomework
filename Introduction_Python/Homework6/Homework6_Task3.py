# my module

#f1 = SUM
def f1(*var):
    i = 0
    for a in var:
        i+=a
    return i

#f2 = substract
def f2(a, b):
    a-=b
    return a

#f3 = urjver
def f3(*var):
    i=1
    for a in var:
        i*=a
    return i

def main(a):
    b = a*2
    b = f1(a, b)
    a = f2(b, a)
    a = f3(a, b)
    return a

if __name__ == '__main__':
    print(main(3))

#Step 4 үр дүнг фолдерт Screenshot1.png хэлбэрээр хадгалав.
