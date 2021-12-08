year = int(input("Which year do you want to check ? : "))
if year % 4 == 0 and year % 100 != 0 :
    print(f"Yes , The year {year} is a leap year as it is divisible by 4.")
elif year % 400 == 0:
    print("Yes , The year {year} is a leap year as it is divisible by 400.") 
else :
    print(f"No , The year {year} is not a leap year.")
  