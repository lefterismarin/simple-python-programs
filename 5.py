def isHarshad(num):
  num_string = str(num)
  num_list = list(num_string)
  num_int_list = []
  num_sum = 0
  for x in num_list:
    num_sum += int(x)
  num_result = num/num_sum
  if num_result == round(num_result): 
    return True
  else:
    return False

harshad_numbers = []  

for num in range(1, 1001):
  if isHarshad(num) == True:
    harshad_numbers.append(num)

print("Οι αριθμοί Harshad είναι: " , harshad_numbers)

def Harshad(num):
  num_string = str(num) 
  num_list= list(num_string)
  num_int_list = []
  num_prod = 1
  for i in num_list:
    num_prod = num_prod * int(i)
  if num_prod == 0:
      return False
  else:
      num_result=num/num_prod
      if num_result == round(num_result): 
          return True
      else:
          return False
    
harshad__numbers = []

for num in range(1, 1001):
    if Harshad(num) == True:
        harshad__numbers.append(num)

print("Οι αριθμοί οι οποίοι διαιρούνται με το γινόμενο των ψηφίων τους είναι : " , harshad__numbers)






