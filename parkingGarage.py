from IPython.display import clear_output

class ParkingGarage():
    """
    ParkingGarage class that assigns tickets for parking spaces
    requires payment before a driver is allowed to leave
    accepts the payment and makes the parking space available again,
    once the driver leaves.
    """

    # Initialize variables necessary for instance
    def __init__(self, tickets, parking_spaces, current_ticket, ticket_payments={}):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        self.ticket_payments = ticket_payments

    # Method to assign a ticket and a space when driver enters
    # and marks those unavailable
    def take_ticket_and_a_space(self):
        tickets_assigned = False
        
        # self.current_ticket = {key : "occupied" tickets_assigned += 1  if self.current_ticket[key] == "unoccupied" and tickets_assigned < 1 else key for key in self.current_ticket.items()}
        for i in range(1, len(self.current_ticket.items()) + 1):
            if tickets_assigned == False and self.current_ticket[i] == 'unoccupied':
                self.current_ticket[i] = "occupied"
                self.ticket_payments[i] = "unpaid"
                tickets_assigned = True
                self.parking_spaces.pop(0)
                self.tickets.pop(0)
                print(f"You have been assigned to parking space {i}.")
                print(f"There are {10 - len(self.ticket_payments.items())} spaces left.")
        if tickets_assigned == False:
            print(f"{self.current_ticket} \nSorry, we are all full.")

        

    
    # Method to accept payment for drivers leaving
    def pay_for_parking(self):
        ct = {key:value for key,value in self.current_ticket.items() if value == 'occupied'}
        ticket_num = input(f"{ct} \nPlease select your ticket: ")
        while True:
            if int(ticket_num) in ct.keys():
                if self.ticket_payments[int(ticket_num)] == "paid":
                    print("You've already paid.")
                    break
                payment = input("Please pay $1 (enter '$1') ")
                if payment == "$1" and self.ticket_payments[int(ticket_num)] != "paid":
                    self.ticket_payments[int(ticket_num)] = "paid"
                    print("Payment accepted. You have 15 minutes to leave.")
                    break
                else:
                    print("Payment not accepted (Please type '$1' exactly next time.)")
            else:
                print("That's not your ticket. Please try again.")
                break
    
    # Method to reassign tickets and spaces to available after driver
    # leaves
    def leave_garage(self):
        get_ticket = input(f"Please present your ticket to leave. \n{self.ticket_payments} \n Please select your ticket: ")
        if int(get_ticket) in self.ticket_payments.keys():
            if self.ticket_payments[int(get_ticket)] == 'paid':
                print("Thank You! Have a nice day!")
                self.tickets.append(int(get_ticket))
                self.parking_spaces.append(int(get_ticket))
                self.ticket_payments.pop(int(get_ticket))
                self.current_ticket[int(get_ticket)] = 'unoccupied'
            else: 
                print("Please pay before leaving.")
                pg.pay_for_parking()
        else:
            print("That's not your ticket. Please try again.")

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

while True:
    response = input("What would you like to do? 'enter'/'pay'/'leave' or type 'quit' to quit: ")
    if response == 'enter':
        clear_output()
        pg.take_ticket_and_a_space()
    elif response == 'pay':
        clear_output()
        pg.pay_for_parking()
    elif response == 'leave':
        clear_output()
        pg.leave_garage()
    elif response == 'quit':
        break
    else:
        clear_output()
        print("Invalid response. \n")