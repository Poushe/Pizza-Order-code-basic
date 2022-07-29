print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size=='S':
  sbill= 15
  if add_pepperoni=='Y':
    sbill+=2
  if extra_cheese =='Y':
    sbill+=1
    print(f'Your final bill is : {sbill}.')
  else:
    print(f'Your final bill is : ${sbill}.')
elif size=='M':
  sbill= 20
  if add_pepperoni=='Y':
    sbill+=3
  if extra_cheese =='Y':
    sbill+=1
    print(f'Your final bill is : {sbill}.')
  else:
    print(f'Your final bill is : ${sbill}.')
elif size=='L':
  sbill= 25
  if add_pepperoni=='Y':
    sbill+=3
  if extra_cheese =='Y':
    sbill+=1
    print(f'Your final bill is : {sbill}.')
  else:
    print(f'Your final bill is: ${sbill}.')
else:
    print(f'Your final bill is: ${sbill}.')
