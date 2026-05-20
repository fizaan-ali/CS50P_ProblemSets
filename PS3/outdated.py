# 9/8/1636 or September 8, 1636  ==> 1636-09-08

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if '/' in date: # 1st format
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
        else: # 2nd format
            month, day, year = date.split()
            month = months.index(month.title()) + 1
            day = int(day[:-1]) # use string slicing to remove the last comma
            year = int(year)

        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError()

    except ValueError:
        continue
    else:
        break

print(f"{year}-{month:02}-{day:02}")
