from art import logo
import random
def choose_number():
  chosen_number=random.choice(range(1,101))
  return chosen_number
  #choose_number()
print(logo)
choice=input("Enter your choice 'easy' or 'hard'")
chosen_one=choose_number()
if choice=='easy':
  num=10
  while(num>0):
    guess=int(input("Enter the guessed number"))
    if guess>chosen_one:
      print("TOO HIGH")
      num-=1
      print(f"Only {num} chances remaining")
    elif guess<chosen_one:
      print("TOO LOW")
      num-=1
      print(f"Only {num} chances remaining")

    elif guess==chosen_one:
      print("Congo  you choose the right number")
      break
  print(f"Better luck next time the number was{chosen_one}")
elif choice=='hard':
  num=5
  while(num>0):
    guess=int(input("Enter the guessed number"))
    if guess>chosen_one:
      print("TOO HIGH")
      num-=1
      print(f"Only {num} chances remaining")
    elif guess<chosen_one:
      print("TOO LOW")
      num-=1
      print(f"Only {num} chances remaining")

    elif guess==chosen_one:
      print("Congo  you choose the right number")
      break    
  print(f"Better luck next time the number was  {chosen_one}")
