import random
score = 0
maxn = 10
guess = None
n = random.randint(1,maxn)
print("Greetings guess the secret number from 1 to 10")
while guess != n:
	guess = int(input("Enter your guess: "))
	if guess > n:
		print("Your guess is too high try again :D")
		score += 1
	elif guess < n:
		print("Your guess is too low try again :D")
		score += 1
if score < 3:
	print("You won with ", score , "tries! Good job")
elif score > 3:
	print("You won with ", score , "tries! ooh that took a while better luck next time :D")