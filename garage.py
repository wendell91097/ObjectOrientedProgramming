class ParkingGarage():
    """
    The parking garage class that allows you to create a parking garage in which cars can come and go.
    The class expects two equivalent lists for parkingSpaces and for tickets

    .takeTicket uses the pop() function to remove the last item from both lists and designates that to the current ticket's dictionary.

    .payForParking is a loop function that asks for an input which is the payment. 
     if the payment is empty, the user is prompted indefinitely for a payment.

    .leaveGarage is a conditional function, where if the 'paid' value in the 
    currentTicket dictionary has the key true, the user can leave. Otherwise, they are 
    prompted for their payment
    """

    def __init__(self, parkingSpaces, tickets, currentTicket = {'paid' : False, 'ticketNumber' : "null", 'spaceNumber' : "null" }):
        self.parkingSpaces = parkingSpaces
        self.tickets = tickets
        self.currentTicket = currentTicket

    def takeTicket(self):
        if len(self.parkingSpaces) <= 0:
            print("There's no more room here. Sorry!")
        else:
            self.currentTicket['ticketNumber'] = self.tickets.pop()
            self.currentTicket['spaceNumber'] = self.parkingSpaces.pop()
            print(f"Thank you, your ticket number is {self.currentTicket['ticketNumber']} and your space number is {self.currentTicket['spaceNumber']}.")
            
    def payForParking(self):
        while True:
            payment = input("Please pay for your ticket.")
            if payment:
                print("Thank you. You have 15 minutes to leave. Have a nice day!")
                self.tickets.append(self.currentTicket['ticketNumber'])
                self.parkingSpaces.append(self.currentTicket['spaceNumber'])
                self.currentTicket['paid'] = True
#                 print(self.currentTicket['paid'])
                break
            else: 
                print("You didn't pay.")

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank you, have a nice day!")
        else: 
            while True:
                payment = input("Please pay for your ticket.")
                if payment:
                    print("Thank you, have a nice day!")
                    self.tickets.append(self.currentTicket['ticketNumber'])
                    self.parkingSpaces.append(self.currentTicket['spaceNumber'])
                    self.currentTicket['paid'] = True
                    break
                else: 
                    print("You didn't pay.") 
    
my_garage = ParkingGarage([x for x in range(0,50)],[x for x in range(0,50)])

my_garage.takeTicket()

my_garage.payForParking()

my_garage.leaveGarage()



    