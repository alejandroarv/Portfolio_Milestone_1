#Create ItemToPurchase class
class ItemToPurchase:
    #create the attributes
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    #method to calculate prices
    def get_items_cost(self):
        return self.item_price*self.item_quantity
    #output for the class
    def print_item_cost(self):
        print('{0} {1} @ ${2:.2f} = ${3:.2f}'.format(self.item_name,self.item_quantity,self.item_price, self.get_items_cost()))


#Create loops for the main section so the correct data type is  entered

#item1
print('Please enter the following information for the first item.')

while True:
    item_name_1 = input('Enter the name of the first item: ')
    if item_name_1:
        break
    print('Item name cannot be empty, please enter a valid name.')

while True:
    try:
        item_price_1 = float(input('Enter the price of {}: '.format(item_name_1)))
        if item_price_1 >= 0:
            break
        print('Price cannot be negative, please enter a valid price.')
    except ValueError:
        print('Invalid input, please enter a valid number for the price.')

while True:
    try:
        item_quantity_1 = int(input('Enter the amount of {} you need: '.format(item_name_1)))
        if item_quantity_1 >= 0:
            break
        print('Quantity cannot be negative, please enter a valid quantity.')
    except ValueError:
        print('Invalid input, please enter a whole number for the quantity.')



#item2
print('Please enter the following information for the second item.')

while True:
    item_name_2 = input('Enter the name of the second item: ')
    if item_name_2:
        break
    print('Item name cannot be empty, please enter a valid name.')

while True:
    try:
        item_price_2 = float(input('Enter the price of {}: '.format(item_name_2)))
        if item_price_2 >= 0:
            break
        print('Price cannot be negative, please enter a valid price.')
    except ValueError:
        print('Invalid input, please enter a valid number for the price.')

while True:
    try:
        item_quantity_2 = int(input('Enter the amount of {} you need: '.format(item_name_2)))
        if item_quantity_2 >= 0:
            break
        print('Quantity cannot be negative, please enter a valid quantity.')
    except ValueError:
        print('Invalid input, please enter a whole number for the quantity.')


#create two ItemToPurchase objects
item1=ItemToPurchase(item_name_1, item_price_1, item_quantity_1)    
item2=ItemToPurchase(item_name_2, item_price_2, item_quantity_2)

#calculate the total price
total_price = item1.get_items_cost()+item2.get_items_cost()

#output
print('TOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print('Total: ${:.2f}'.format(total_price))
print('Thank you for your purchase!!!')


#exit the program
input('Press enter to close the program')

