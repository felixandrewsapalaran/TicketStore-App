#Create a new constant for the 2 dollar service charge
SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100  


def calculate_price (number_of_tickets):
  #add the service charge with the total due 
  return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE
  

while tickets_remaining >= 1:
  print("There are {} tickets remaining!!!".format(tickets_remaining))
  name = input("What is your name? ")
  num_ticket = input("{} how many tickets would you like to buy? ".format(name))
  try:
    num_ticket = int(num_ticket)
    if num_ticket > tickets_remaining:     
      raise ValueError("There are only {} tickets remainig".format(tickets_remaining))
  except ValueError as err:
    print("Oh no, we ran into an issue. {}. Please try again.".format(err))
  else:
    #assign function and pass number of tickets
    totalPrice = calculate_price(num_ticket)
    print("Total due is $",totalPrice)
    should_proceed = input("Do you want to proceed Y/N? ")
    if should_proceed.lower() == "y":
      print("SOLD!")
      tickets_remaining -=  num_ticket
    else:
      print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are all sold out!!! :(")