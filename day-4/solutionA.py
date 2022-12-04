file = open("./input.txt")

sum = 0
for line in file.readlines():
  low_a, up_a, low_b, up_b = [x for x in line.strip().split(',') for x in map(int, x.split('-'))]
  
  if (low_b > up_a or low_a > up_b):
    continue # If this passes there's no possible overlap
    
  delta_a = up_a - low_a
  delta_b = up_b - low_b
  lower_g = max(low_a, low_b)
  upper_g = min(up_a, up_b)
  delta_g = upper_g - lower_g
  
  if delta_g >= delta_a or delta_g >= delta_b:
    sum +=1

print(sum)
  