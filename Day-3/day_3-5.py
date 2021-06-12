#Multiple If statements in Succession

print("Welcome to the RollerCoster Ride")

height = float(input("Please enter your height in cm: "))
bill_amount = 0

if height >= 120:
    print("You are eligible for the ride")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 10
        print("You require a Child fee of RS 10")
    elif age <=18:
        bill = 20
        print("You require a Teenage fee of RS 20")
    else:
        bill = 30
        print("You require an Adult fee of RS 30")
    
    require_photos = input("Please say 'Y' if you need the photos or else please mention 'N': ")
    if require_photos == "Y":
        bill +=3

    print(f"Your final bill is {bill}")

else:
    print("You are not eligible for the ride")
