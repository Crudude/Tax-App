class TaxRates:
    def __init__(self,tb, pb, tr, rb):
        self.taxbracket = tb
        self.taxpb = pb
        self.rebate = rb
        self.taxrate = tr
        
    def calculateTax(self, amount):
        for i in range(8):
            if (amount < self.taxbracket[i]):
                return round(max((amount-self.taxbracket[i-1])*self.taxrate[i] - self.rebate + self.taxpb[i], 0),2)
                
