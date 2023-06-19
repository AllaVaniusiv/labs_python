"""
Abstract class
"""
from abc import ABC, abstractmethod

class Printer(ABC):
    """
    Abstract base class representing a printer.
    """

    default_printer = None

    def __init__(self, model='', pr_type='', is_color=False, is_duplex=False,# pylint: disable=too-many-arguments
                 paper_tray_capacity=0, paper_count=0):
        """
        Initialize a Printer object.
        Args:
            model (str): The model of the printer.
            pr_type (str): The type of the printer.
            is_color (bool): True if the printer supports color printing, False otherwise.
            is_duplex (bool): True if the printer supports duplex printing, False otherwise.
            paper_tray_capacity (int): The capacity of the paper tray.
            paper_count (int): The current count of paper in the tray.
        """
        self.model = model
        self.pr_type = pr_type
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count

    def __str__(self):
        """Returns a string that represents the object in a readable format."""
        return f"""Model: {self.model}, Pr Type: {self.pr_type}, Color: {self.is_color},\
        Duplex: {self.is_duplex},Paper Tray Capacity: {self.paper_tray_capacity},
        Paper Count: {self.paper_count}"""

    def __repr__(self):
        """Returns a string that is a valid Python expression for reproducing the object."""
        return f"Printer(model='{self.model}', pr_type='{self.pr_type}', is_color={self.is_color},\
        is_duplex={self.is_duplex}, paper_tray_capacity={self.paper_tray_capacity},\
        paper_count={self.paper_count})"

    def print_pages(self, pages):
        """
        Print the specified number of pages.
        Args:
            pages (int): The number of pages to print.
        """
        if pages <= self.paper_count:
            self.paper_count -= pages
            print(f"Printing {pages} pages...")
        else:
            print("Not enough paper in the tray!")

    def load_paper(self, count):
        """
        Load the specified number of paper sheets into the printer.
        Args:
            count (int): The number of paper sheets to load.
        """
        self.paper_count += count
        if self.paper_count > self.paper_tray_capacity:
            self.paper_count = self.paper_tray_capacity

    @abstractmethod
    def get_remaining_pages_count(self):
        """
        Abstract method to get the remaining number of pages for printing.
        This method should be implemented by the concrete printer classes.
        Returns:
            int: The remaining number of pages.
        """
