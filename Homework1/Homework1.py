name = str(input("Нэрээ бичнэ үү: "))
print("Сайн байна уу? ", name+ ".")
# End of question 1
nas = int(input("Насаа оруулна уу: "))
print("Та {} настай.".format(nas))
# End of question 2
food = str(input("Та дуртай хоолоо бичнэ үү: "))
drink = str(input("Та дуртай уух зүйлээ бичнэ үү: "))
print("Таны дурай уух зүйл бол {}, хоол бол {}.".format(drink, food))
#End of question 3
song = str(input("Та дуртай дууны нэрийг бичнэ үү: "))
print("Та {} дуунд дуртай.".format(song))
#End of question 4
bool1 = input("Хэрэв та багш бол 1, сурагч бол 0 гэж бичнэ үү: ")
# bool(input()) гэж бичвэл хоосон биш string-ийг boolean-руу хөрвүүлсэн болох буюу 0 гэж өгсөн ч boolean нь True болдог юм байна. 
if bool1==True:
    print("Та багш байна.")
else:
    print("Та сурагч байна.")
#End of question 5