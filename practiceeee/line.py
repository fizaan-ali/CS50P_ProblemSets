import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
if not file_name.endswith('.py'):
    sys.exit("Not a python file")

try:
    with open(file_name) as file:
        # here's the code of counting LOC
        count = 0
        for line in file:
            line = line.lstrip()
            if line.startswith('#') or line == '':
                continue
            count += 1

except  FileNotFoundError:
    sys.exit("File does not exist") 

print("Lines of code:", count)