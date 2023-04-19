class Flight :
    def fly(self):
        print('날다, fly 원형메서드')

class Airplane(Flight) :
    def fly(self):
        print('비행기가 날다')

class Bird(Flight):
    def fly(self):
        print('새가 날다.')

class PaperAirplane(Flight) :
    def fly(self):
        print('종이 비행기가 날다.')

flight = Flight()
air = Airplane()
bird = Bird()
paper = PaperAirplane()

flight.fly()

flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()

