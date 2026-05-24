import re
import sys

def main():
    time = input("Hours: ")

    
    print(convert(time))

    

def is_valid(time):
    # allowed formats
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM
    match = re.search(r'^([0-9]{1,2}(?::[0-9]{2})?) (?:AM|PM) to ([0-9]{1,2}(?::[0-9]{2})?) (?:AM|PM)$', time)
    if match:
        for part in match.groups():
            if ':' in part:
                hours, minutes = part.split(':')
                if not (1 <= int(hours) <= 12 and 0 <= int(minutes) <= 59):
                    return False
            else:
                if not 1 <= int(part) <= 12:
                    return False
        return True
    else:
        return False


def convert(s):
    try:
        if not is_valid(s):
            raise ValueError
    except ValueError:
        sys.exit("ValueError")
        
    match = re.search(r'^([0-9]{1,2}(?::[0-9]{2})?) (AM|PM) to ([0-9]{1,2}(?::[0-9]{2})?) (AM|PM)$', time)
    first, ft, second, st = match.groups()

    if ft == 'AM':
        if ':' in first:
            hours1, minutes1 = first.split(':')
            if hours1 == '12':
                hours1 = '0'
        else: # if there's not ':'
            hours1 = first
            if hours1 == '12':
                hours1 = '0'
            minutes1 = '0'
    else: # ft == 'PM'
        if ':' in first:
            hours1, minutes1 = first.split(':')
            if hours1 != '12':
                hours1 = str(int(hours1) + 12)
        else: # if there's not ':'
            hours1 = first
            if hours1 != '12':
                hours1 = str(int(hours1) + 12)
            minutes1 = '0'

    if st == 'AM':
        if ':' in second:
            hours2, minutes2 = second.split(':')
            if hours2 == '12':
                hours2 = '0'
        else: # if there's not ':'
            hours2 = second
            if hours2 == '12':
                hours2 = '0'
            minutes2 = '0'
    else: # st == 'PM'
        if ':' in second:
            hours2, minutes2 = second.split(':')
            if hours2 != '12':
                hours2 = str(int(hours2) + 12)
        else: # if there's not ':'
            hours2 = second
            if hours2 != '12':
                hours2 = str(int(hours2) + 12)
            minutes2 = '0'

    return f"{hours1:0>2}:{minutes1:0>2} to {hours2:0>2}:{minutes2:0>2}"


if __name__ == '__main__':
    main()