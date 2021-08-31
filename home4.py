'''
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return (self.a * self.b) + (other.a * other.b)

    def __sub__(self, other):
        return (self.a * self.b) - (other.a * other.b)

    def __eq__(self, other):
        return (self.a * self.b) == (other.a * other.b)

    def __lt__(self, other):
        return (self.a * self.b) < (other.a * other.b)

    def __gt__(self, other):
        return (self.a * self.b) > (other.a * other.b)


rec = Rectangle(3, 5)
tan = Rectangle(6, 7)
print(rec < tan)

'''

########################################################

'''
class Transport:
    def __init__(self, time):
        self.time = time

    def __sub__(self, other):
        return self.time - other.time


class Fly (Transport):
    def __init__(self, time, ticket_price, on_boarding_time, seat_level):
        super(Fly, self).__init__(time)
        self.ticket_price = ticket_price
        self.on_boarding_time = on_boarding_time
        self.seat_level = seat_level

    def travel_time(self):
        return self.time + self.on_boarding_time


class Car (Transport):
    def __init__(self, time, numb_of_passengers, fuel_price, km):
        super(Car, self).__init__(time)
        self.num_of_passengers = numb_of_passengers
        self.fuel_price = fuel_price
        self.km = km

    def travel_price(self):
        return self.fuel_price * self.km


class Train (Transport):
    def __init__(self, time, ticket_price, seat_type):
        super(Train, self).__init__(time)
        self.ticket_price = ticket_price
        self.seat_type = seat_type

    def info(self):
        return "Your seat_type: {}s.. Travel time: {}. Ticked price: {} ".format(self.seat_type, self.time, self.ticket_price)


lviv_odesa = Train(43200, 225, 'плацкарт')
by_fly = Fly(7200, 1200, 2, 1)
print(lviv_odesa.info())
print(by_fly - lviv_odesa)

'''

########################################################

li = []


class Letter:
    def __init__(self, __text):
        self.__text = __text

    __count = 0

    def _get_text(self):
        return self.__text

    def _set_text(self, new_text):
        self.__text = new_text

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def push_to_list(self, __text):
        li.append(__text)

    new_text = property(fget=_get_text, fset=_set_text)


le = Letter('world')
le.new_text = 'car'
print(le)

