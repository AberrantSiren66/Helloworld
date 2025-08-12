from datetime import date

def say_hello(name):
    print("hello, "+ name)

say_hello("VS Code")

def say_day_of_week(date_str):
    print("Today is " + date_str)

def call_with_today(say_day_of_week):
    say_day_of_week(date.today().isoformat())

call_with_today(say_day_of_week)