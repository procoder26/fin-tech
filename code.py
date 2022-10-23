print("Welcome to the FIN Tech Bank! \nPlease create your account.")
username = input("Username: ")
password = input("Password: ")
amount = 0
print("Welcome "+ str (username) + "! You curently have $" + str (amount) + " in your bank account. What would you like to do?")
task = set()
while True:
  print("1. Make a deposit.")
  print("2. Make a withdraw.")
  print("3. Change your password.")
  print("4. Log out.")
  q1 = int (input("Type in a number here: "))
  if q1 == 1:
      amount = amount + int (input("Please type in the amount you'd like to deposit: "))
      print("Welcome "+ str (username) + "! You curently have $" + str (amount) + " in your bank account. What would you like to do?")
  elif q1 == 2:
    amount = amount - int (input("Please type in the amount you'd like to withdraw: "))
    print("Welcome "+ str (username) + "! You curently have $" + str (amount) + " in your bank account. What would you like to do?")
  elif q1 == 3:
      password1 = input("Please enter your old password: ")
      if password1 == password:
        password = input("Please enter your new password: ")
        print("Your new password is: "+ password)
      else:
        print("Incorrect! Logging you out.")
        break
  else:
      print("Bye!")
      break
