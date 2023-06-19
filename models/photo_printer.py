"""
A class PhotoPrinter
"""
from models.printer import Printer
class PhotoPrinter(Printer):
    """
    A class inheriting from the Printer class.
    """

    def __init__(self, model, pr_type, is_color, is_duplex, paper_tray_capacity,# pylint: disable=too-many-arguments
                 paper_count, print_quality, ink_level):
        """
        Initialize a PhotoPrinter object.
        Args:
           model (str): The model of the printer.
           pr_type (str): The type of the printer.
           is_color (bool): Indicates if the printer supports color printing.
           is_duplex (bool): Indicates if the printer supports duplex printing.
           paper_tray_capacity (int): The capacity of the paper tray.
           paper_count (int): The current count of paper in the printer.
           print_quality (str): The quality of photo printing.
           ink_level (float): The current ink level of the printer.
        """
        super().__init__(model, pr_type, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.print_quality = print_quality
        self.ink_level = ink_level

    def __str__(self):
        """Returns a string that represents the object in a readable format."""
        return f"PhotoPrinter: model={self.model}, pr type={self.pr_type}, color={self.is_color},\
duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity},\
paper count={self.paper_count}, print quality={self.print_quality},\
inkLevel={self.ink_level}"

    def __repr__(self):
        """Returns a string that is a valid Python expression for reproducing the object."""
        return f"PhotoPrinter(model={self.model}, pr type={self.pr_type}, color={self.is_color},\
duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity}, paper count={self.paper_count},\
print quality={self.print_quality}, inkLevel={self.ink_level })"

    def get_remaining_pages_count(self):
        """
        Calculate the remaining number of pages that can be printed.
        Returns:
            int: The remaining number of pages that can be printed.
        """
        remaining_pages = self.paper_tray_capacity - self.paper_count
        return remaining_pages
