from datetime import date
import inflect 
import sys
import re


def main():

    birth_date = input("Date of Birth: ")
    print(minutes_to_words(convert_to_minutes(validate_date(birth_date))))

def validate_date(birth_date):
    
    match = re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', birth_date)
    if not match:
        sys.exit("Invalid date format!!")
    return birth_date                                                                                                                   
    
def convert_to_minutes(birth_date):
    birth_date = date.fromisoformat(birth_date) # convert to date.. format
    difference = date.today() - birth_date # by use or op overloading btw two date objects~
    return difference.days * 24 * 60   # minutes
   

def minutes_to_words(minutes):
    p = inflect.engine()
    sing = p.number_to_words(minutes, andword='').capitalize()
    return sing + " minutes"

if __name__ == "__main__":
    main()