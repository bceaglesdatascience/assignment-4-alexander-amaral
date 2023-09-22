purchase_number = int(input("Number of purchases: "))

tax = float(input("Sales tax: "))

customer_list = []
cost_list = []
new_cost_list = []

while purchase_number > 0:
    customer = input("Customer: ")
    customer_list.append(customer) 
    cost = float(input("Cost: "))
    cost_list.append(cost)
    purchase_number -= 1

def add_tax(cost_list,tax):
    for cost in cost_list:
        new_cost = cost*(1+tax)
        new_cost_list.append(new_cost)
    return new_cost_list
        
add_tax(cost_list, tax)

purchases = {}

for x in range(len(customer_list)):
    customer = customer_list[x]
    new_cost = new_cost_list[x]
    if customer in customer_list:
        new_cost += new_cost
        purchases[customer] = new_cost
    else:
        purchases[customer] = new_cost

print(purchases)
