__author__ = 'vimsree'

def greatest_common_divisor(number1, number2):
    while number1 % number2 != 0:
        old_number1 = number1
        old_number2 = number2
        number1 = old_number2
        number2 = old_number1 % old_number2
    return number2

class Fractions:

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

    def __mul__(self, other_fraction):
        new_numerator = self.numerator*other_fraction.numerator
        new_denominator = self.denominator*other_fraction.denominator
        common_divisor = greatest_common_divisor(new_numerator,new_denominator)
        return str(new_numerator // common_divisor)+'/'+str(new_denominator // common_divisor)

    def __divmod__(self, other_fraction):
        new_numerator = self.numerator*other_fraction.denominator
        new_denominator = self.denominator*other_fraction.numerator
        common_divisor = greatest_common_divisor(new_numerator,new_denominator)
        return str(new_numerator // common_divisor)+'/'+str(new_denominator // common_divisor)

    def __cmp__(self, other_fraction):
        left_numerator = self.numerator*other_fraction.denominator
        right_numerator = self.denominator*other_fraction.numerator
        return self.__str__()+" is greater than "+other_fraction.__str__() if left_numerator > right_numerator else self.__str__()+" is lesser than "+other_fraction.__str__()


# Fraction calls

f1 = Fractions(5,4)
f2 = Fractions(7,3)
print(f1)
print(f2)
print("Addition of two Fractions:", f1.__add__(f2))
print("Subtraction of two Fractions:", f1.__sub__(f2))
print("Multiplication of two Fractions:", f1.__mul__(f2))
print("Division of two Fractions:", f2.__divmod__(f1))
print('Are two Fractions equal:', f2.__eq__(f1))
print("Comparison of two Fractions:", f1.__cmp__(f2))
