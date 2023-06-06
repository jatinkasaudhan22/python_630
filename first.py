"""  fac = 1 
n=int(input("Enter n "))
if n>= 0:
for i in range(1,n+1):
 fac = fac*i

  print(fac)
else:
 print("The value of should be n >0")
  """

  info = ""
n = int(input("Enter n = "))
for i in range (n):
   name= input("Enter name = ")
   price = int(input("Enter price "))
   quantity = float (input("Enter quantity = "))
   total = price*quantity
   data = name + " " + str(price) + " " + str(quantity) + " " + str(total) + "\n"
   info = info + data
  print(info)







#Control Statement

  for i in range(10):
  if i == 5:
    break
  print(i)


  for i in range(10):
  if i == 5:
    continue
  print(i)