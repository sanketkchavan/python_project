# part1

custName = "Mary Smith"
itemDesc = "Shirt"
message = custName +  " wants to purchase a " + itemDesc
print(message)


# part2

price = 24
tax = 1.78
quantity = 1
message = custName + " wants to purchase " + str(quantity) + " " + itemDesc
print(message)
total_price = price * quantity * tax
print(f"Total cost with tax is: {total_price}")

