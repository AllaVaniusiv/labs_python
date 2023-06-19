"""
Main module for managing printers.
"""
from managers.printer_manager import PrinterManager
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.photo_printer import PhotoPrinter
from models.three_d_printer import ThreeDPrinter

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
