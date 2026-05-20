# def main():
#     time = convert(input("Time: "))
#     if 7 <= time <= 8:
#         print("breakfast time")
#     elif 12 <= time <=13:
#         print("lunch time")
#     elif 18 <= time <= 19:
#         print("dinner time")


# def convert(time):
#     hours, minutes = time.split(":")
#     hours = int(hours)
#     minutes = int(minutes)
#     return float(hours + minutes/60)

# if __name__ == "__main__":
#     main()

def main():
    time = convert(input("Time: "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <=13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    if(minutes.endswith('a.m.') or minutes.endswith("p.m.")):
        min, garbage = minutes.split()
        minutes = min
    hours = int(hours)
    minutes = int(minutes)
    if hours!= 12 and time.endswith("p.m."):
        return float(12 + hours + minutes/60)
    elif hours == 12 and time.endswith("a.m."):
        return minutes/60
    else:
        return float(hours + minutes/60)





if __name__ == "__main__":
    main()
