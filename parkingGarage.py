class ParkingGarage():
    """
    ParkingGarage class that assigns tickets for parking spaces
    requires payment before a driver is allowed to leave
    accepts the payment and makes the parking space available again,
    once the driver leaves.
    """
    
    # Constants
    SPACES = 10

    # Initialize variables necessary for instance
    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket

    # Method to assign a ticket and a space when driver enters
    # and marks those unavailable
    def take_ticket_and_a_space(self):
        tickets_assigned = False
        # self.current_ticket = {key : "occupied" tickets_assigned += 1  if self.current_ticket[key] == "unoccupied" and tickets_assigned < 1 else key for key in self.current_ticket.items()}
        for i in range(1, len(self.current_ticket.items()) + 1):
            if tickets_assigned == False and self.current_ticket[i] == 'unoccupied':
                self.current_ticket[i] = "occupied"
                tickets_assigned = True
                self.parking_spaces.pop(i - 1)
                self.tickets.pop(i - 1)
        if tickets_assigned == False:
            print(f"{self.current_ticket} \nSorry, we are all full.")

        print(len(self.current_ticket.items()))
        print(self.current_ticket)
        print(self.tickets)
        print(self.parking_spaces)

    
    # Method to accept payment for drivers leaving
    def pay_for_parking(self):
        pass

    # Method to reassign tickets and spaces to available after driver
    # leaves
    def leave_garage(self):
        pass

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parking_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
current_ticket = {
    1:'unoccupied',
    2:'unoccupied',
    3:'unoccupied',
    4:'unoccupied',
    5:'unoccupied',
    6:'unoccupied',
    7:'unoccupied',
    8:'unoccupied',
    9:'unoccupied',
    10:'unoccupied',
    }

pg = ParkingGarage(tickets, parking_spaces, current_ticket) # instance

pg.take_ticket_and_a_space()