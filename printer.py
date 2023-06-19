class Printer:
    default_printer = None

    def __init__(self, model='', pr_type='', is_color=False, is_duplex=False, paper_tray_capacity=0, paper_count=0):
        self._model = model
        self._pr_type = pr_type
        self._is_color = is_color
        self._is_duplex = is_duplex
        self._paper_tray_capacity = paper_tray_capacity
        self._paper_count = paper_count

    def __str__(self):
        return f"""Model: {self._model}, Pr Type: {self._pr_type}, Color: {self._is_color}, Duplex: {self._is_duplex},Paper Tray Capacity: {self._paper_tray_capacity}, Paper Count: {self._paper_count}"""

    def __repr__(self):
        return f"Printer(model='{self._model}', pr_type='{self._pr_type}', is_color={self._is_color}, is_duplex={self._is_duplex}, paper_tray_capacity={self._paper_tray_capacity}, paper_count={self._paper_count})"

    @property
    def printer_model(self):
        return self._model

    @printer_model.setter
    def printer_model(self, new_model):
        self._model = new_model

    @property
    def printer_pr_type(self):
        return self._pr_type

    @printer_pr_type.setter
    def printer_pr_type(self, new_pr_type):
        self._pr_type = new_pr_type

    @property
    def printer_is_color(self):
        return self._is_color

    @printer_is_color.setter
    def printer_is_color(self, new_is_color):
        self._is_color = new_is_color

    @property
    def printer_is_duplex(self):
        return self._is_duplex

    @printer_is_duplex.setter
    def printer_is_duplex(self, new_is_duplex):
        self._is_duplex = new_is_duplex

    @property
    def printer_paper_tray_capacity(self):
        return self._paper_tray_capacity

    @printer_paper_tray_capacity.setter
    def printer_paper_tray_capacity(self, new_paper_tray_capacity):
        self._paper_tray_capacity = new_paper_tray_capacity

    @property
    def printer_paper_count(self):
        return self._paper_count

    @printer_paper_count.setter
    def printer_paper_count(self, new_paper_count):
        self._paper_count = new_paper_count

    @staticmethod
    def get_instance():
        if not Printer.default_printer:
           Printer.default_printer = Printer()
        return Printer.default_printer

    @classmethod
    def print_pages(cls, pages):
        if pages <= cls.paper_count:
            cls.paper_count -= pages
            print(f"Printing {pages} pages...")
        else:
            print("Not enough paper in the tray!")

    def load_paper(self, count):
        self.printer_paper_count += count
        if self.printer_paper_count > self.printer_paper_tray_capacity:
            self.printer_paper_count = self.printer_paper_tray_capacity
    
