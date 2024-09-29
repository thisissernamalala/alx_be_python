from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    current_date = datetime.now()
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days) + current_date
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
    

display_current_datetime()
calculate_future_date()