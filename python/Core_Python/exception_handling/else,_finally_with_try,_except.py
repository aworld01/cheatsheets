while True:
  try:
    num1=int(input("Please enter 1st number: "))
    num2=int(input("Please enter 2nd number: "))
  except ValueError:
    print("Please enter a number")
  except:
    print("Unexpected error...")
  else:
    print("The sum of the numbers is:", num1+num2)
    break
  finally:
      print("This is the finally block...")
  