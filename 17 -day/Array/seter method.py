import ctypes
class Array:
      # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

def __len__(self):
    return self._size
def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out oof range"
        return self._elements[index]




def __setitem__(self, index, value):
    assert index >= 0 and index < len(self), "Array subscript out of range"
    self._elements[index] = value

def clear(self, value):
    for i in range(len(self)):
        self._elements[i] = value



def __iter__(self):
    return _ArrayIterator(self._elements)

