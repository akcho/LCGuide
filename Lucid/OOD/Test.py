from abc import ABC
'''
Enums and constants
'''
class VehicleType(Enum):
    SUV, ELECTRIC, COMPACT = 1,2,3

class ParkingSpotType(Enum):
    HANDICAP, COMPACT, LARGE, MOTORBIKE: 1,2,3,4

class AccountStatus(Enum):
    ACTIVE, BLOCKED, ARCHIVED = 1,2,3

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, PENDING = 1,2,3

class Person:
    def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone


'''
Users
'''
class Account:
    def __init__(self, username, pw, person, is_active):
        self.__username = username
        self.__password = pw
        self.__account_status = is_active

class Admin(Account):
    def __init__(self, username, pw, person, is_active):
        super().__init(username, pw, person, is_active)

    def add_parking_floor(self, floor_num): None
    def add_parking_spot(self, floor_num, spot_num): None
    def add_parking_display_hub(self, floor_num, ID): None
    def add_customer_info_p

