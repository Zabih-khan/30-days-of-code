class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
    
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        x=[]
        for i in range(1,n+1):
            if n%i==0:
                x.append(i)
        return(sum(x))
            

n = int(input("Enter number:"))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
