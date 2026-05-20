def main():
    line = input("Input: ")
    print("Output:", shorten(line))


def shorten(word):
    vowels = 'aeiouAEIOU'
    out  = ''
    for c in word:
        if c not in vowels:
            out += c
    return out


if __name__ == "__main__":
    main()
