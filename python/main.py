fruits = ["apple","orange","banana"]
for fruit in fruits:
 print(fruit)
 for item in range(10):
  print(item)
  for count in range(10):
   if count >5:
     
     break
   elif count  %2 == 0:
     continue
   print(count)
  count=0
  while count <= 5:
   print(count)
   
