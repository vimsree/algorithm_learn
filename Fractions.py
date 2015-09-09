__author__ = 'vimsree'

def greatest_common_divisor(number1, number2):
    while number1 % number2 != 0:
        old_number1 = number1
        old_number2 = number2
        number1 = old_number2
        number2 = old_number1 % old_number2
    return number2

class Function:

    def __init__(self,top,bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, other_fraction):
        new_numerator = (self.numerator*other_fraction.denominator)+(other_fraction.numerator*self.denominator)
        new_denominator = self.denominator*other_fraction.denominator
        common_divisor = greatest_common_divisor(new_numerator,new_denominator)
        return str(new_numerator // common_divisor)+'/'+str(new_denominator // common_divisor)

    def __eq__(self, other_fraction):
        left_product = self.numerator*other_fraction.denominator
        right_product = other_fraction.numerator*self.denominator
        return left_product == right_product

    def __sub__(self, other_fraction):
        new_numerator = (self.numerator*other_fraction.denominator)-(other_fraction.numerator*self.denominator)
        new_denominator = self.denominator*other_fraction.denominator
        common_divisor = greatest_common_divisor(new_numerator,new_denominator)
        return str(new_numerator // common_divisor)+'/'+str(new_denominator // common_divisor)

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

f1 = Function(3,4)
f2 = Function(1,3)
print(f1)
print(f2)
print(f1.__add__(f2))
print(f2.__eq__(f1))
print(f1.__sub__(f2))
