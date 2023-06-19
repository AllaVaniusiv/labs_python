from printer import Printer

printer1 = Printer()
printer2 = Printer("HP LaserJet", "laser", True, True, 250, 50)
printer3 = Printer.get_instance()
printer4 = Printer.get_instance()

printers = [printer1, printer2, printer3, printer4]

for printer in printers:
    print(printer)
