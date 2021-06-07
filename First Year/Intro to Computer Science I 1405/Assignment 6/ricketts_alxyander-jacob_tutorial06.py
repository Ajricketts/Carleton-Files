blank = ""
store_name = input("What should the name of this store be?: ")
blank += store_name + "\n"
while True:
	try:
		categories = int(input("How many categories of merchandise will you be selling?: "))
  	
	except ValueError:
		print("Whoops, I could not convert your input into an integer....")
	if categories < 0:
		print("The number of categories you inputed was less than or equal to zero: ")
	else:
		break
for i in range(categories):
	print("This is category #", i + 1, end="")	
	cat_name = input("\nWhat is the name of this category?: ")	
	while True:
		try:	
			num_products = int(input("How many products will you have in this category?: "))
		except ValueError:
			print("Whoops, I could not convert your input into an integer....")	
		if num_products <= 0:
			print("The number of categories you inputed was less than or equal to zero: ")
		else:
			break
	blank += cat_name
	for j in range(num_products):
		print("This is product #", j + 1, end="")		
		product_name = input("\nWhat is the name of the product?: ")
		stock = int(input("How many of this item do you have in stock?: "))
		price = float(input("What is the price of this product?: "))
		
		blank += "\n" + product_name + "\n" + str(stock) + "\n" + str(price) + "\n" + "\n"

print(blank)

