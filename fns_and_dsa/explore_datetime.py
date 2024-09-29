import datetime

current_date = datetime.datetime.now()

def display_current_datetime():
    print(f"Current date and time: {current_date}")

future_date = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future = datetime.timedelta(future_date) + current_date
    print(f"Future date: {future}")
    

