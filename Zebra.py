""" Создайте класс Zebra, внутри которого есть метод which_stripe , 
который поочередно печатает фразы "Полоска белая", "Полоска черная", 
начиная именно с фразы "Полоска белая" """

class Zebra:
    def __init__(self, count=1):
        self.count = count
    def which_stripe(self):
            self.count += 1
            if self.count % 2 == 0:
                print('Полоска белая')
            else:
                print('Полоска черная')

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"