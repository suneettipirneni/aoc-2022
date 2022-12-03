file = open('./input.txt')

sum = 0
lines = file.readlines()
for line in lines:
  radix = [0] * 52
  compartments = line[:len(line) // 2], line[len(line) // 2:].strip()
  val = lambda ch: (ord(ch) - ord('A')) + 27 if ord(ch) < ord('a') else (ord(ch) - ord('a')) + 1

  for group_member in map(lambda x: set(x.strip()), compartments):
    for ch in group_member:
      radix[val(ch) - 1] += 1   

  sum += radix.index(2) + 1

print(sum)
