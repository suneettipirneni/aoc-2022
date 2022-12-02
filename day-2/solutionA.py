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

  sum += reward_matrix[opponent_play][player_play] + player_play + 1

print(sum)
