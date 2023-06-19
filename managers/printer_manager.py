"""
A class PrinterManager
"""
class PrinterManager:
    """
    A class representing PrinterManager.
    """
    def __init__(self):
        """
        Initializes the PrinterManager object.
        Attributes:
            printers (list): A list of printers, initially empty.
        """
        self.printers = []

    def __len__(self):
        """
        Returns the number of printers in the manager.
        """
        return len(self.printers)

    def __getitem__(self, index):
        """
        Returns the printer at the specified index.
        """
        return self.printers[index]

    def __iter__(self):
        """
        Returns an iterator over the printers.
        """
        return iter(self.printers)


    def add_printer(self, printer):
        """
        Add a printer to the manager.
        Args:
            printer (Printer): The printer to be added.
        """
        self.printers.append(printer)

    def find_printer_with_pr_type(self, pr_type):
        """
        Find printers of a specific type.
        Args:
            pr_type (str): The type of printers to find.
        Returns:
            list: A list of printers matching the specified type.
        """
        filtered_printers = list(filter(lambda printer: printer.pr_type == pr_type, self.printers))
        return filtered_printers

    def find_printer_with_more_paper_than(self, paper_count):
        """
        Find printers with more paper than a given count.
        Args:
            paper_count (int): The minimum paper count to filter printers.
        Returns:
            list: A list of printers with more paper than the specified count.
        """
        filtered_printers = list(filter
                                 (lambda printer: printer.paper_count > paper_count, self.printers))
        return filtered_printers

    def get_remaining_pages_count_result(self):
        """
        Returns a list of remaining pages count for all printers in the manager.
        """
        return [printer.get_remaining_pages_count() for printer in self.printers]

    def get_concatenated_objects_with_index(self):
        """
        Returns the concatenation of each object with its index in the list.
        """
        return [f'{index}: {obj}' for index, obj in enumerate(self.printers)]

    def get_concatenated_object_and_result(self):
        """
        Returns the concatenation of each object and the result of the method execution.
        """
        remaining_pages_counts = self.get_remaining_pages_count_result()
        return [f'{obj}: {count}' for obj, count in zip(self.printers, remaining_pages_counts)]

    def check_condition(self, condition):
        """
        Checks if a given condition is satisfied for all or any printers in the manager.
        Args:
        condition (function): A condition function that takes a printer as input and
        returns a boolean value.
        Returns:
             dict: A dictionary with 'all' and 'any' keys indicating if the condition
             is satisfied for all or any printer,
        respectively.
        """
        all_condition = all(condition(printer) for printer in self.printers)
        any_condition = any(condition(printer) for printer in self.printers)
        return {"all": all_condition, "any": any_condition}
