#This program is for addition
math1 = [[1, 2], [3, 4]]
math2 = [[1, 2], [3, 4]]
math3 = [[0, 0], [0, 0]]

for i in range(0, 2):
    
   for j in range(0, 2):
       
       math3[i][j] = math1[i][j] + math2[i][j]
       print("Addition of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
       print(math3[i][j], end = "")
       print()



#This program is for subtraction

math1 = [[9, 2], [5, 3]]
math2 = [[8, 1], [4, 2]]
math3 = [[0, 0], [0, 0]]

for i in range(0, 2):
    
   for j in range(0, 2):
       
       math3[i][j] = math1[i][j] - math2[i][j]
       print("Subtraction of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
       print(math3[i][j], end = "")
       print()




#This  program is  to multiply two matrices

math1 = [[9, 2], [5, 3]]
math2 = [[8, 1], [4, 2]]
math3 = [[0, 0], [0, 0]]

for i in range(0, 2):
    
   for j in range(0, 2):
       
       math3[i][j] = math1[i][j] * math2[i][j]
       print("Multiplication of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
       print(math3[i][j], end = "")
       print()