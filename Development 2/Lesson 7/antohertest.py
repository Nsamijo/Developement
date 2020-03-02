class Cow():
    def __init__(self, name):
        self.AmountOfLegs = 4
        self.Weight = 500
        self.Color = 'Green'
        self.Name = name
        self.tup = ('Hi', 'There', 'Human')

    def Moo(self):
        print(self.Name + ' says Moo!')

Betsy = Cow('Betsy')
try:
    Betsy.tup[0] = 'Hello'
except:
    print('Oops! Hit a brick wall!')
print(Betsy.Color)