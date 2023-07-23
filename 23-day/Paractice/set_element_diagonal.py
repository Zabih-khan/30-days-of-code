import numpy
class Array2D:
    def __init__(self,numRows, numCols):
        self.array = numpy.zeros((numRows, numCols), dtype=int)

    def display(self):
        print(self.array)

    def numRows(self):
        return len(self.array)
    def numCols(self):
        return  len(self.array[0])

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2 , "Invalid number of array subscript "
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols() , "Array subscript out of range"
        theidArray = self.array[row]
        print(theidArray)


    def __setitem__(self, ndxTuble, value):
        assert len(ndxTuble) == 2, "Invalid number of array subscript"
        row = ndxTuble[0]
        col = ndxTuble[1]
        assert  row >= 0 and row < self.numRows()and\
                col >= 0 and col < self.numCols(), "Array subcript out of range"
        theidArray = self.array[row]
        theidArray[col] = value

if __name__ == '__main__':
    obj = Array2D(5, 5)
    obj.__setitem__((0,0), 1)
    obj.__setitem__((1, 1), 6)
    obj.__setitem__((2, 2), 6)
    obj.__setitem__((3, 3), 6)
    obj.__setitem__((4, 4), 6)
    obj.display()


