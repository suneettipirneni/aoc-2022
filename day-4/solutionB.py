file = open("./input.txt")

sum = 0
for line in file.readlines():
  low_a, up_a, low_b, up_b = [x for x in line.strip().split(',') for x in map(int, x.split('-'))]

  if not (low_b > up_a or low_a > up_b):
    sum += 1

print(sum)