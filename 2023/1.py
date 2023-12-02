import sys
input = open(("C:\\Users\\9909_03\\input.txt").read().strip()
p1 = 0
p2 = 0
for line in input:
  p1_digits = []
  p2_digits = []
  for i,c in enumerate(line):
    if c.isdigit():
      p1_digits.append(c)
      p2_digits.append(c)
