# Name: Nicholas Vickery
# Date: 9/18/2023
# Program: Leap Year


# This function returns a true or false statement if the year entered is a leap year or not
def leap_year(year):
    # This line makes sure the year is divisible by 400 
    # Or
    # Makes sure its divisible by 4
    # And
    # Makes sure it is not divisble by 100
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# This function takes the users input as a integer and sends it to the leap year function and comes back with a true or false statement based on the users input. 
def main():
    # Get the year from the user
    year = int(input("Enter the year to check: "))

    # Determine if the year is a leap year
    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# This command runs the main function
main()
