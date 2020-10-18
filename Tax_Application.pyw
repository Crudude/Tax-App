import sys
from PyQt5 import QtWidgets                                 
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from module1 import TaxRates

#Tax Data
TR2021 = TaxRates([0,205900,321600,445100,584200,744800,1577300,999999999],[0,0,37062,67144,105429,155505,218139,559464],[0,0.18,0.26,0.31,0.36,0.39,0.41,0.45],14958)
TR2020 = TaxRates([0,195850,305850,423300,555600,708310,1500000,999999999],[0,0,35253,63853,100263,147891,207448,532041],[0,0.18,0.26,0.31,0.36,0.39,0.41,0.45],14220)
TR2019 = TaxRates([0,195850,305850,423300,555600,708310,1500000,999999999],[0,0,35253,63853,100263,147891,207448,532041],[0,0.18,0.26,0.31,0.36,0.39,0.41,0.45],14067)

#Main App
class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()  
        self.ui.pushButton.clicked.connect(self.taxfunction)

    def taxfunction(self):
        amount = self.ui.incometext.toPlainText()
        
        if (self.ui.yeartext.toPlainText() == 2021):
            tax = TR2021.calculateTax(float(amount))
        elif (self.ui.yeartext.toPlainText() == str(2020)):
            tax = TR2020.calculateTax(float(amount))
        elif (self.ui.yeartext.toPlainText() == 2019):
            tax = TR2019.calculateTax(float(amount))
        else:
            tax = 69.69

        self.ui.label_6.setText("Tax Payable: R{:,.2f}" .format(float(tax)))


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
