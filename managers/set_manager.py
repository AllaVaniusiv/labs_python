"""
This is Set Manager class
"""
class SetManager:
    """
    A class representing a Set Manager.
    """

    def __init__(self, printer_manager):
        """
        Initializes a new instance of the SetManager class.
        :param printer_manager: The Printer Manager containing the printers.
        """
        self.printer_manager = printer_manager

    def __iter__(self):
        """
        Returns an iterator that iterates over the objects in sets.
        :return: iterator: An iterator over the objects in the sets.
        """
        return iter(self.printer_manager)

    def __len__(self):
        """
        Returns the total length of all sets combined.
        :return: int: The total length of all sets combined.
        """
        total_len = 0
        for _ in self.printer_manager:
            total_len += 1
        return total_len

    def __getitem__(self, index):
        """
        Returns the item at the specified index in the combined sets.
        :param index: The index of the item to retrieve.
        :return: object: The item at the specified index in the combined sets.
        :raises: IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        return self.printer_manager[index]

    def __next__(self):
        """
        Raises a StopIteration exception.
        This method is required for iterator compatibility but is not used in SetManager.
        :raises: StopIteration: Always raised to indicate the end of iteration.
        """
        raise StopIteration()
