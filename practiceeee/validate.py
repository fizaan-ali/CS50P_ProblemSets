# email = input("What's your email? ").strip()

# # if "@" in email and '.' in email:
# #     print("Valid")
# # else:
# #     print("Invalid")

# username, domain = email.split("@") 

# if username and domain.endswith('.edu'):
#     print("Valid")
# else:
#     print("Invalid")

import re

email = input("What's your email? ").strip()
# now we are using \ to escape the . chracter and with r -> we are telling  python to treat it as raw string and don't interpet it like escape characcters
# if re.search(r"^.+@.+\.edu$", email): # .+ -> ..*
#     print("Valid")
# else:
#     print("Invalid")

# r"" -> raw string it means in python to not interpret any escape characters in it
# ^ -> start of string $ -> end of string

# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# [] -> set of characters
# [^] -> complementing the set e.g. [^@] -> every character except @

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# [a-zA-Z0-9_] -> set of characters to include from
# a to z, A to Z, 0 to 9, and the _ (underscore) char

# it also equals to w (word) it is a set of this w = [a-zA-Z0-9_]

# if re.search(r"^\w+@\w+\.(edu|com|net)$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")
# (edu|com|net) -> means either edu, com, or net grouping things

# A|B either A or B
# ? -> optional either there or not there

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# (\w+\.)? this one means either this (\w\.) either characters with end with dot may be there or not if it's there treat them othewise not