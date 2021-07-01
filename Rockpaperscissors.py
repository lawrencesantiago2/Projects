import random
score_player = 0
score_enemy = 0
rounds = 0
list = ["R","P","S"]
print("Welcome to my Rock Paper and Scissors game!")
print("[R]ock , [P]aper , [S]cisssors")
while rounds != 3:
	rounds = rounds +1
	player = input(" ")
	enemy = random.choice(list)
	if player == enemy:
		print("Its a draw!")
		rounds = rounds -1
	elif enemy == "R" and player == "S":
		print("You Lose Rock beats Scissors")
		score_enemy = score_enemy +1
		print("Score ", score_player , " - " , score_enemy)
	elif enemy == "S" and player == "P":
		print("You Lose Scissors beats Paper")
		score_enemy = score_enemy +1
		print("Score ", score_player , " - " , score_enemy)
	elif enemy == "P" and player  =="R":
		print("You Lose Paper beats Rock")
		score_enemy = score_enemy +1
		print("Score ", score_player , " - " , score_enemy)
	else:
		print("You win!", player , " beats ", enemy)
		score_player = score_player +1
		print("Score ", score_player , " - " , score_enemy)
	
	