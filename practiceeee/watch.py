import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # it gives us the youtube link specifically
    if match := re.search(r'^.+src="(.+?)".+$', s):
        link = match.group(1)
        # now extract the last url part
        if match := re.search(r'^https?://(?:www\.)?youtube\.com/embed/(.+)$', link):
        
            return "https://youtu.be/" + match.group(1)

if __name__ == "__main__":
    main()