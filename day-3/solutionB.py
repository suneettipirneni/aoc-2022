file = open('./input.txt')

sum = 0
lines = file.readlines()
for i in range(0, len(lines), 3):
  radix = [0] * 52
  val = lambda ch: (ord(ch) - ord('A')) + 27 if ord(ch) < ord('a') else (ord(ch) - ord('a')) + 1

  for group_member in map(lambda x: set(x.strip()), lines[i:i+3]):
    for ch in group_member:
      radix[val(ch) - 1] += 1   

  sum += radix.index(3) + 1

print(sum)

