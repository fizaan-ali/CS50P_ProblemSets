import re


def main():
    print(count(input("Text: ")))


def count(s):
    
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    count = 0
    for _ in matches:
        count += 1
    return count

if __name__ == "__main__":
    main()