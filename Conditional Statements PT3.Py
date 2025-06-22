RealCost = float(input("Enter the real cost of the item:"))
SaleAmount = float(input("Enter the sale amount of the item"))

if (SaleAmount > RealCost):
 amount = SaleAmount - RealCost
 print("Totsl profit = {0}".format(amount))
else: 
 print("No profit made")