def comp_int (x,y):
	int = x/100*y
	return int
def comp_prin(x,y):
	prin = x+y
	return prin

i= 1
try:
	amount = float(input("Input amount invested: "))
	int_rate = float(input("Input annual interest rate: "))
	years = int(input("Input number of years: "))
	if amount >= 10000 and years >= 10:
		while i != years and amount >= 10000 and years >= 10:
			int = comp_int(amount,int_rate)
			print("Years	Principal Amount	Interest	Total" )
			print(i, "	", amount ,"		" , int , "		" , amount + int)
			amount = comp_prin(amount,int)
			i = i +1
	else:
		print("You entered less than the required minimum input")
except ValueError:
	print("You didnt enter a number.")	

