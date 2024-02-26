from datetime import datetime
# Function that takes name of a user and returns Hello <Username>
def welcome_user(name):
    return f"Hello {name}"


# Function that takes the date of birth of a user and returns age
def calculate_age(date_of_birth):
    today = datetime.now()
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age



"""
Use the above functions to make the Command line app to simply take Name 
and Date of birth as input and print ***
"Hello <Username>, your age is <calculated age> years"
"""
 
def main():
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    
    greeting = welcome_user(name)
    age = calculate_age(dob)
    
    print(f"{greeting}, your age is {age} years.")

if __name__ == "__main__":
    main()
    


