import datetime

current_date = datetime.datetime.now()

def display_current_datetime():
    print(f"Current date and time: {current_date}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.timedelta(number_of_days) + current_date
    print(f"Future date: {future_date}")
    

    
calculate_future_date()