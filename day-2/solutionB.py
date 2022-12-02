file = open("./input.txt")

# X corresponds to player input, Y corresponds to opponent input
reward_matrix = [[3, 6, 0],
                 [0, 3, 6],
                 [6, 0, 3]]

sum = 0
for line in file.readlines():
  opponent_char, player_char = line.strip().split(' ')
  opponent_play = ord(opponent_char) - ord('A')
  player_play = ord(player_char) - ord('X')

  player_choices = reward_matrix[opponent_play]
  if player_play == 0:
    player_choice = player_choices.index(0)
  elif player_play == 1:
    player_choice = player_choices.index(3)
  else:
    player_choice = player_choices.index(6)

  sum += player_choices[player_choice] + player_choice + 1

print(sum)