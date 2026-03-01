class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        elif amount > 2500:
            print("Amount must be less than 2500")
        else:
            self.balance += amount
            print(f"amount deposited: {amount}")
#aiiii ubralod erti ragaca davwere rogor xvdeba py charmi tviton gamiketa ubralod tabebs vawire lmaooooooooooooooooooo
#vin geniosma gamoigona es

    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough money")
        elif amount <= 0:
            print("amount must be positive")
        else:
            self.balance -= amount
            print(f"amount withdrawn: {amount}")

    def display_balance(self):
        print(self.balance)

accounti1 = BankAccount("ilia", 2000)

accounti1.display_balance()
accounti1.withdraw(100)
accounti1.display_balance()
accounti1.deposit(200)
accounti1.display_balance()
accounti1.withdraw(5000)
accounti1.display_balance()
accounti1.deposit(5000)
accounti1.display_balance()

#mgoni es auto codis dawera unda gamovrto wina davalebebshi ar miketebda eset ragaceebs
import math

class Shape:
    def dscribe(self):
        print("im a shape")

class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
    #hold on saidan icoda aman rom heronis formula unda damewera es ra teqnologiaa

samkutxedi = Triangle(3, 4, 5)
samkutxedi.dscribe()
print(samkutxedi.calculate_area())
#raaris es kods ro miwers da tan icis rasac miwers sadan icis man es ese ar sheizleba iqneb sxval formula mindoda
#thats crazyyyyy





