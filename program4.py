cp =int(input("Enter cost price:"))
sp =int(input("Enter selling price:"))

profit = sp-cp
print("Profit is:",profit)

#increased profit by 5%
new_profit = profit+0.05*profit

new_sp = new_profit+cp
print("Required new selling price is:",new_sp)
