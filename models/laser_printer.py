"""
A class LaserPrinter
"""
from models.printer import  Printer
class LaserPrinter(Printer):
    """
    A class inheriting from the Printer class.
    """

    def __init__(self, model, pr_type, is_color, is_duplex, paper_tray_capacity,  # pylint: disable=too-many-arguments
                 paper_count, toner_pages_count, printed_pages_count):
        """
        Initialize a LaserPrinter object with the specified attributes.
        Args:
            model (str): The model of the printer.
            pr_type (str): The type of the printer.
            is_color (bool): A flag indicating whether the printer supports color printing.
            is_duplex (bool): A flag indicating whether the printer supports duplex printing.
            paper_tray_capacity (int): The capacity of the paper tray in the printer.
            paper_count (int): The current count of paper in the printer.
            toner_pages_count (int): The total number of pages the toner can print.
            printed_pages_count (int): The count of pages that have been printed.
        """
        super().__init__(model, pr_type, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.toner_pages_count = toner_pages_count
        self.printed_pages_count = printed_pages_count

    def __str__(self):
        """Returns a string that represents the object in a readable format."""
        return f"LaserPrinter: model={self.model}, pr type={self.pr_type},\
color={self.is_color}, duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity},\
paper count={self.paper_count}, toner_pages_count={self.toner_pages_count},\
printed_pages_count={self.printed_pages_count}"

    def __repr__(self):
        """Returns a string that is a valid Python expression for reproducing the object."""
        return f"LaserPrinter(model={self.model}, pr type={self.pr_type}, color={self.is_color},\
duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity},\
paper count={self.paper_count}, toner_pages_count={self.toner_pages_count},\
printed_pages_count={self.printed_pages_count})"

    def get_remaining_pages_count(self):
        """
        Calculate and return the remaining number of pages that can be printed.
        Returns:
            int: The remaining number of pages that can be printed.
        """
        return self.toner_pages_count - self.printed_pages_count
