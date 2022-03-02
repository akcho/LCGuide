from abc import ABC


class VehicleType(Enum):
    CAR, TRUCK, VAN, MOTORCYCLE = 1,2,3,4


class SpotType(Enum):
    COMPACT, LARGE, HANDICAPPED, MOTORCYCLE, ELECTRIC = 1,2,3,4,5

class Status(Enum):
    ACTIVE, PENDING, INACTIVE = 1,2,3


class ParkingStructure:
    def __init__(self):
        self.__active_tickets = {}
        self.__floors = {}
        self.__payment_portals = {}
        self.__display_boards = {}


class ParkingFloor:
    def __init__(self):
        self.__total_spots = None
        self.__compact_spots= None
        self.__large_spots = None
        self.__handicapped_spots = None
        self.__motorcycle_spots = None
        self.__electric_spots = None
        self.__payment_portal = PaymentPortal()
        self.__display_board = DisplayBoard()


class DisplayBoard:
    def __init__(self):
        self.__floor = None
        self.__spot_to_display = None

    def set_spot_to_display(self, spot_ID):
        self.__spot_to_display = spot_ID

    def get_free_spots(self):
        # do this loop for each vehicle type:
            # first check if there's a free spot on this floor
            # if not, display free spot on an adjacent floor
        None


class PaymentPortal:
    def __init__(self):
        self.__ticket_db = {}

    def process_ticket(self, ticket):
        ticket_id = ticket.get_id()
        if self.__ticket_db[id] == ACTIVE:
            self.__ticket.set_status(INACTIVE)
            self.__ticket_db.update()


class ParkingSpot(ABC):
    def __init__self(type):
        self.__type = SpotType.type
        self.__is_free = True

    def set_free(self, status: Bool): self.__is_free = status
    def is_free(self): return self.__is_free

class Vehicle(ABC):
    def __init__(self, type):
        self.__type = VehicleType.type


class Ticket:
    def __init__(self):
        self.__ID = None
        self.__price = None
        self.__dt = None
        self.__status = INACTIVE

    def get_amount_due(self):
        curr_dt = None
        hours_accrued = curr_dt - self.__dt
        if hours_accroud == 1: return 4
        elif hours_accrued == 2: return 4 + 3.5
        elif hour_accrued == 3: return 4 + 3.5 + 3.5
        else: return 4 + 3.5 + 3.5 + (2.5 * (hours_accrued-3))






class ElectricPanel:
    def __init__(self):
        self.__id = None