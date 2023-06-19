"""
Main module for managing printers.
"""
from managers.printer_manager import PrinterManager
from managers.set_manager import SetManager
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.photo_printer import PhotoPrinter
from models.three_d_printer import ThreeDPrinter
from exception import OutOfPaperException

manager = PrinterManager()
manager.add_printer(InkjetPrinter("Hp", "inkjet", False, True, 50, 100, "Type1", 100,
                                  "Type2", 50, "Type3", 75, "Type4", 80))
manager.add_printer(InkjetPrinter("Canon", "inkjet", False, True, 55, 100, "Type1", 70,
                                  "Type2", 50, "Type3", 105, "Type4", 90))
manager.add_printer(LaserPrinter("Hp", "laser", True, False, 40, 150, 200, 300))
manager.add_printer(LaserPrinter("Canon", "laser", True, True, 60, 100, 250, 350))
manager.add_printer(PhotoPrinter("Hp", "inkjet", True, True, 25, 130, 210, 320))
manager.add_printer(PhotoPrinter("Canon", "laser", True, True, 30, 85, 245, 330))
manager.add_printer(ThreeDPrinter("Hp", "inkjet", True, True, 45, 70, 220))
manager.add_printer(ThreeDPrinter("Canon", "inkjet", True, True, 65, 75, 250))

printers_with_type = manager.find_printer_with_pr_type("laser")
print("Printers with type 'laser':")
for printer in printers_with_type:
    print(printer)

print("\n")

printers_with_more_paper_than = manager.find_printer_with_more_paper_than(100)
print("Printers with paper count greater than 100:")
for printer in printers_with_more_paper_than:
    print(printer)

print("\n")

remaining_pages_count = manager.get_remaining_pages_count_result()
print("\nRemaining Pages Count:", remaining_pages_count)

concatenated_objects_with_index = manager.get_concatenated_objects_with_index()
print("\nConcatenated Objects with Index:")
for item in concatenated_objects_with_index:
    print(item)

concatenated_object_and_result = manager.get_concatenated_object_and_result()
print("\nConcatenated Object and Result:", concatenated_object_and_result)


printer1 = InkjetPrinter("Canon", "inkjet", False, True, 55, 56,
                        "Type1", 0, "Type2", 0, "Type3", 0, "Type4", 0)
printer2 = ThreeDPrinter ("Canon", "inkjet", True, True, 65, 5, 250)
print("\n")
try:
    printer1.get_remaining_pages_count()
    printer2.get_remaining_pages_count()
except OutOfPaperException as e:
    print(e)
attributes = printer.get_attributes_by_value_pr_type(str)
print("\nList of attributes by value type str:")
print(attributes)

def altitude_condition(some_printer):
    """
    Check if a printer's paper count is greater than 130.
    Args:
    some_printer (Printer): The printer object to check.
    Returns:
    bool: True if the printer's paper count is greater than 130, False otherwise.
    """
    return some_printer.paper_count > 130
print("\nCheck condition paper count > 130:")
result = manager.check_condition(altitude_condition)
print("All printers satisfy the altitude condition:", result["all"])
print("At least one printer satisfies the altitude condition:", result["any"])

set_manager = SetManager(manager)

print("\nLength of SetManager:", len(set_manager))
print("\n")
print("Items in sets:")
for item in set_manager:
    print(item)
