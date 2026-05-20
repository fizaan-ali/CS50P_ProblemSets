def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not ( 2 <= len(s) <= 6 ):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    for c in s:
        if not(c.isalpha() or c.isdigit()):
            return False

    # now first find middle index
    idx_num = None
    for i in range(2, len(s)):
        if s[i].isdigit():
            idx_num = i
            break

    if idx_num is not None:
        if s[idx_num] == '0':
            return False

        while idx_num < len(s):
            if s[idx_num].isalpha():
                return False
            idx_num += 1

    return True

if __name__ == '__main__':
    main()
