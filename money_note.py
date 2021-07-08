def notes(num):
  money = [2000,500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(7):
    q = money[i]
    x += int(num / q)
    num = int(num % q)
  if num > 0:
    x = -1
  return x

num = int(input("Enter amount : "))

print("Number of notes : ",notes(num))	
