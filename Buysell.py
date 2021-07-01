dict_buy = {"USD": 47.30,"EURO": 56.44,"YEN": .42}
dict_sell = {"USD": 48.10, "EURO": 59.86, "YEN": .44}

def php_exg(x,y):
	fx_amount = x*y
	print(x, " x ", y, "= Amount in Php", float(fx_amount))

choice = input("[B]uy or [S]ell: ")	
amount = float(input("Input amount: "))
curr = input("Input Currency: ")
if choice == "B" or choice == "b":
	print("Buying exchange rates: ", dict_sell)
	php_exg(amount,dict_sell.get(curr.upper()))
elif choice == "S" or choice == "s":
	print("Selling exchange rates: ", dict_buy)
	php_exg(amount,dict_buy.get(curr.upper()))