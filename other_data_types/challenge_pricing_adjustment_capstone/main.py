grocery_inventory={
    "Milk":("Dairy",3.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15),
    "Apples":("Produce",1.50,50)
}

egg_cat,egg_price,egg_stock=grocery_inventory["Eggs"]
if egg_price>5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"]=(egg_cat,egg_price-1,egg_stock)
else:
    print("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)
milk_cat,milk_price,milk_stock=grocery_inventory["Milk"] 
if milk_stock<10:
    print("Milk needs to be restocked. increasing stock by 20 units.")
    grocery_inventory["Milk"]=(milk_cat,milk_price,milk_stock+20)
else:
    print("Milk has sufficient stock.")
apple_cat,apple_price,apple_stock=grocery_inventory["Apples"]
if apple_price>2:
    print("Apples removed from inventory due to high price")
    grocery_inventory.pop("Apples",None)
print("Updated inventory:",grocery_inventory)










