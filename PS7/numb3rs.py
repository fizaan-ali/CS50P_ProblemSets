import re

def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if match:
        for part in match.groups():
            if not 0 <= int(part) <= 255:
                return False

            if part != str(int(part)):
                return False
        return True

    else:
        return False

if __name__ == "__main__":
    main()
