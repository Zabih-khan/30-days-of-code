class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        mini=self.__elements[0]
        for i in self.__elements:
            if mini>i:
                mini=i
                
        maxi=self.__elements[0]
        for i in self.__elements:
            if maxi<i:
                maxi=i
        self.maximumDifference=abs(mini-maxi)
    
        


# End of Difference class

_ = input("How many number you want to enter:")
a = [int(e) for e in input("Enter Numbers:").split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
