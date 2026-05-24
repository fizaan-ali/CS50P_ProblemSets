import re

url = input("URL: ").strip()

# re.sub() substitute

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# print(username)

# if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):

#     print(f"Username: {matches.group(3)}") 


# capturing version -> ( )
# non-capturing version -> (:? )   


if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):

    print(f"Username: {matches.group(1)}") 