class Complex():

    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm
    

    def mul(self,other):
        result = Complex(None,None)
        result.s = self.s * other.s - self.m + other.m
        result.m = self.s * other.m + other.s + self.m
        return result
        #(a + bi)(c + di) = (ac – bd) + (ad + bc)i


    def sum(self , other):
        result = Complex(None,None)
        result.s = self.s + other.s
        result.m = self.m + other.m
        return result


    def sub(self , other):
        result = Complex(None,None)
        result.s = self.s - other.s
        result.m = self.m - other.m
        return result

    def div(self , other):
        result = Complex(None/None)

        result.s = (self.s + other.s * self.m - other.m) / (other.s ** 2 + other.m ** 2)
        result.m = (self.m + other.m * self.m - other.m) / (other.s ** 2 + other.m ** 2)
        return result

    #a+bi/c+di = a+bi/c+di⋅c−di/c−di =ac+bd / c2+d2 + bc−ad /c2+d2i


    def show(self):
        print(self.s,'+',self.m,'i')


num = int(input('Please enter num :'))
mohomi = int(input('Please Enter mohomi :'))
num2 = int(input('Please enter num2 :'))
mohomi2 = int(input('Please Enter mohomi2 :'))

a = Complex(num,mohomi)
b = Complex(num2,mohomi2)
while True:
    print('Choose your operator : \n1 - sum \n2 - sub \n3 - mul \n4 - div\n0 - Exit')
    choice = int(input())
    if choice == 1:
        a.sum(b).show()
    elif choice == 2 :
        a.sub(b).show()
    elif choice == 3 :
        a.mul(b).show()
    elif choice == 4 :
        a.div(b).show()
    elif choice == 0:
        exit()
