import re

def main():
    ip = input("IP: ")
    if validate(ip):
        print("Valid")
    else:
        print("Invalid")

def validate(ip):
    matches = re.fullmatch(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', ip)
    
    if matches:
        for part in matches.groups():
            if not 0 <= int(part) <= 255:
                return False
            if part != str(int(part)):
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    main()

