from printer import Printer

printer1 = Printer()
printer2 = Printer("HP LaserJet", "laser", True, True, 250, 50)
printer3 = Printer.get_instance()
printer4 = Printer.get_instance()
printer5 = Printer("HP", "laser", False, False, 5, 10)
printer6 = Printer("Canon", "laser", False, True, 3, 5)

printers = [printer1, printer2, printer3, printer4, printer5, printer6]

for printer in printers:
    print(printer)
