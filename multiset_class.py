import ctypes

class Array:
    def __init__(self, size):
        """
        Produces a newly constructed empty array.
        :param size: size of array.
        """
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    def __str__(self):
        """
        Converts structure to a string.

        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print +")"

    def __len__(self):
        """
        Return length of array.
        :return:
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the data item with given index.
        Requires: 0 <= index < self.size

        :param index: index of the item.
        :return: the data item with given index.
        """
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__(self, index, value):
        """
        Sets the data item with given index.
        Requires: 0 <= index < self.size

        :param index: index of the item.
        :param value: value of the item.
        """
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__( self ):
        return _ArrayIterator( self._elements )

# An iterator for the Array ADT.
class _ArrayIterator :
    def __init__( self, the_array ):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._cur_index < len( self._array_ref ) :
            entry = self._array_ref[ self._cur_index ]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


class Multiset:
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        """
        self.data = Array(100)
        self.firstempty = 0

    def empty(self):
        """
        Checks emptiness of Multiset.

        :return: True if Multiset is empty and False otherwise.
        """
        for index in range(self.firstempty):
            if self.data[index] != None:
                return False
        return True

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.

        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        for index in range(self.firstempty):
            if self.data[index] == value:
                return True
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added..
        """
        self.data[self.firstempty] = value
        self.firstempty = self.firstempty + 1

    def delete(self, value):
        """
        Deletes value from multiset.

        :param value: value firs occurrence of which should be deleted.
        """
        position = -1
        current = 0
        while position == -1 and current < self.firstempty:
            if self.data[current] == value:
                position = current
            else:
                current = current + 1
        if current < self.firstempty:
            for updated in range(position, self.firstempty):
                self.data[updated] = self.data[updated + 1]
            self.data[self.firstempty] = None
            self.firstempty = self.firstempty - 1

