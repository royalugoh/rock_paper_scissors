from random import choice

options = ['rock', 'paper', 'scissors']
loses = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
player_name = input('Enter your name: ')
player_score = 0
print(f'Hello, {player_name}')
rating_file = open('rating.txt', encoding='utf-8')
user_options = input('Enter list of options')
user_options_list = user_options.split(',')
rating_list = []
for line in rating_file:
    rating_list.append(line.split())
for rating in rating_list:
    if player_name in rating:
        player_score = int(rating[1])

print('Okay, let\'s start')
while True:
    user = input()
    if user == '!exit':
        print('Bye!')
        break
    elif user == '!rating':
        print(f'Your rating: {player_score}')
    elif user not in user_options_list and user not in options:
        print('Invalid input')
    else:
        if user_options == '':
            computer = choice(options)
            if user == computer:
                player_score += 50
                print(f'There is a draw ({computer})')
            elif loses[user] == computer:
                print(f'Sorry, but computer chose {computer}')
            else:
                player_score += 100
                print(f'Well done. Computer chose {computer} and failed')
        else:
            user_choice_index = user_options_list.index(user)
            new_options = user_options_list[user_choice_index + 1:] + user_options_list[: user_choice_index]
            index_slice = int(len(new_options) / 2)
            winning_list = new_options[:index_slice]  # Computer won
            user_winning_list = new_options[index_slice:]  # User won
            user_option = [user]
            combined_list = winning_list + user_option + user_winning_list
            computer = choice(user_options_list)
            if user == computer:
                player_score += 50
                print(f'There is a draw ({computer})')
            elif combined_list.index(user) < combined_list.index(computer):
                player_score += 100
                print(f'Well done. Computer chose {computer} and failed')
            else:
                print(f'Sorry, but computer chose {computer}')
