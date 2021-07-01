import random
i = 0
roll = input("Roll dice? [Y]es or [N]o: ")
while roll == "Y" or roll == "y":
	dice = random.randint(1,6)
	if dice == 1:
		print("•")
	elif dice == 2:
		print("••")
	elif dice == 3:
		print("•••")
	elif dice == 4:
		print("••")
		print("••")
	elif dice == 5:
		print("• • •")
		print(" • •")
	elif dice == 6:
		print("•••")
		print("•••")
	roll = input("Roll dice again? [Y]es or [N]o: ")
print("Thank you for using Dice")
		
		
