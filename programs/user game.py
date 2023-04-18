import computer game
user_score=0
computer_score=0
no_of_computer_balls_bowled=0
no_of_user_balls_bowled=0
print('Your Batting')
def user_batting():
	global user_score,no_of_balls
	while no_of_balls<20:
		user_batting=int(input('Enter run from 0 to 10'))
		computer_bowling=computer game.computer_prection()
		if computer_bowling==user_batting:
			print(f'Enter Runs for Your Batting Turn: {user_batting}')
			print(f'Your Gess:{user_batting},Computer Guess:{computer_bowling}')
			break
		else:
			user_score=user_score+user_batting
			no_of_balls=no_of_balls+1
			print(f'Enter Runs for Your Batting Turn: {user_batting}')
			print(f'Your Gess:{user_batting},Computer Guess:{computer_bowling}')
			print(f'Your run now are {user_score}')
	print(f'You are out, your score= {user_score}')
user_batting()
print('Computer Batting')
def computer_batting:
	global no_of_user_balls_bowled,computer_score
	while no_of_user_balls_bowled<20:
		computer_batting=computer game.computer_prection()
		user_bowling=int(input('Enter run from 0 to 10'))
		if computer_batting==user_bowling:
			print(f'Enter run of Your Bowling Turn: {user_bowling}')
			print(f'Computer Gess: {computer_batting},Your Gess: {user_bowling}')
			break
		else:
			computer_score=computer_score+computer_batting
			no_of_user_balls_bowled=no_of_user_balls_bowled+1
			print(f'Enter run of Your Bowling Turn: {user_bowling}')
			print(f'Computer Gess: {computer_batting},Your Gess: {user_bowling}')
			print(f'Computer Runs: {computer_score}')
	print('The computer is out, Computer Runs= {computer_score}')
computer_batting()
print('RESULTS:')
def result():
	if computer_score<user_score:
		print('You Won the Game.')
		print(f'Your TOtal Runs= {user_score} [Balls (out of 20): {no_of_computer_balls_bowled}]')
		print(f'Computer Total Runs= {computer_score} [Balls (Out of 20):{no_of_user_balls_bowled}]')
	elif computer_score>user_score:
		print('Computer Won the Game.')
		print(f'Computer Total Runs= {computer_score} [Balls (Out of 20):{no_of_user_balls_bowled}]')
		print(f'Your TOtal Runs= {user_score} [Balls (out of 20): {no_of_computer_balls_bowled}]')
	else:
		print()
result()
	