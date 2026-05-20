# 1. Max 6 chars and Min 2 chars
# 2. Start with atleast 2 letters
# 3. No periods or spaces or punctutation marks
# 4. Numbers can't be in middle e.g. AAA222 ✔️ AAA22A ❌
#    and first number can't be '0'

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if length(s) and start(s) and punct(s) and middle_ans(s):
        return True
    else:
        return False

def length(s):
    return True if 2<= len(s) <= 6 else False

def start(s):
    return s[0].isalpha() and s[1].isalpha()

def punct(s):
    for c in s:
        if not c.isalpha() and not c.isdigit():
            return False
    return True

def middle_ans(s):
    # first we find the first index where there is number
    idx_num = None
    for i in range(2, len(s)):
        if s[i].isdigit():
            idx_num = i
            break
    if idx_num == None:
        return True

    middle = True

    if s[idx_num] == '0':
        middle = False

    while idx_num+1 < len(s):
        if s[idx_num+1].isalpha():
            middle = False
            break
        idx_num += 1
    return middle

main()
