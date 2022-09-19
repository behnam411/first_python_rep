class converter:
    def __init__(self, data_from,data_to,Value):
        self.data_from = data_from
        self.data_to = data_to
        self.Value = Value
    
    def convert_gr (self):
        res = 0
        if self.data_to == 'gr':
            res = self.Value
        elif self.data_to == 'kg':
            res = self.Value / 1000
        elif self.data_to == 'ton':
            res = self.Value /1000 /1000
        return res
    def convert(self) :
        if self.data_from == 'gr':
            return self.convert_gr()
        