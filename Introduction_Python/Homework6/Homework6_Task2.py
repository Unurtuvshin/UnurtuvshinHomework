class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Сайн байна уу? Та манай цахим банкны үйлчилгээнд тавтай морил!")

    def deposit(self):
        amount = float(input("Оруулах мөнгөн дүн хэмжээ: "))
        self.balance += amount
        print("\n Оруулсан хэмжээ: ", amount)

    def withdraw(self):
        amount = float(input("Гаргах мөнгөн дүн хэмжээ: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Гаргасан хэмжээ:", amount)
        else:
            print("\n Үлдэгдэл хүрэлцэхгүй байна.  ")

    def display(self):
        print("\n Нийт дансны үлдэгдэл=", self.balance)
