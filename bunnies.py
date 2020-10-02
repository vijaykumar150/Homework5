import time
start_time = time.time()



def bunnyEars2(bunnies):
  if (bunnies == 0):
    return 0
  else:
    if (bunnies % 2 == 0):
      return 3 + bunnyEars2 (bunnies - 1)
      sleep(3)
    else:
      return 2 + bunnyEars2 (bunnies - 1)
      sleep(3)

t=bunnyEars2(0)
print(t)

s=bunnyEars2(1)
print(s)

v=bunnyEars2(2)
print(v)

