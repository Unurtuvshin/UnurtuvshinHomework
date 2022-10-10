import Homework6_Task3 as mod
import site
import sys  # system parameters
import os  # operating system functionality is contained
print(os.getcwd())  # current working directory will be printed

print(sys.path)  # all folders in path

sys.path.append(
    r'C:\\Users\\unur0\\Desktop\\projects\\Python\\UnurtuvshinHomework\\Introduction_Python\\Homework6')

if __name__ == '__main__':
    print(mod.main(3))
print(mod.main(2))
print(mod.f1(1, 2))

#Step5 -ийн үр дүнг Screenshot2-оор хадгалав.
#Өмнөх хэсгийн үр дүнгүүд харагдахгүй байгаа шалтгаан нь module ба import хийж буй файлууд
#тусдаа хувьсагчуудтай тул өмнөх үр дүнг хадгалах боломжгүй.