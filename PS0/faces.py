def main():
    result = input()
    print(convert(result))

def convert(line):
    line = line.replace(":)","🙂").replace(":(","🙁")
    return line

main()
