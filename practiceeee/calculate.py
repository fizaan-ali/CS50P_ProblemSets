def main():
    print(calculate_gpa(get_input()))
    

def get_input():
    n = int(input("How many subjects you've got? "))
    courses = []
    for i in range(n):
        course = {}
        course['grade'] = float(input(f"Enter grade for subject {i+1}: "))
        course['ch'] = float(input("Enter its credit hours: "))
        courses.append(course)
    return courses

def calculate_gpa(courses):
    total_qp = 0
    total_ch = 0
    for course in courses:
        total_qp += course['grade'] * course['ch']
        total_ch += course['ch']
    return total_qp / total_ch



if __name__ == '__main__':
    main()