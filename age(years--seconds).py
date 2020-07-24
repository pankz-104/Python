
# changing age from years to seconds and vice-versa


def age_program():
    seconds_or_years = input("Enter age in years (y) or seconds (s) ")
    if seconds_or_years == "s":
        user_value = input("Enter age in seconds: ")    
        print("the age in years is {}".format(int(user_value)/365/24/60/60))
    elif seconds_or_years == "y":
        user_value = input("Enter age in years: ")
        print("the age in seconds is {}".format(int(user_value))*365*24*60*60))
    
