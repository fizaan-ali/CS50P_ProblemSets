'''
1. Functions-> actions or verbs or tasks. programming languages have build in functions for some basic tasks.

2. Arguments-> input to functions that influences the behaviour of that function

3. Side effects of functions -> things functions can do like display things, voices, audio, vidoes etc. other things

4. Bugs -> mistakes/errors in our code 

5. CLI and GUI -> command line interface and graphical user interface

6. return values-> things functions return after doing the task

7. variables -> container for some value 

8. = -> assignment operator . copy the things (or return values) in right to the variable in left

9. comments -> notes to yourself in the code with #(singe line),and text insdie three single or double quotes 

10. + -> concatenate two strings just add two strings and then pass the result to function

11. , in print -> it separate two arguments in functions like print 
    e.g. print(name, age) by default, ',' adds space between those two or more argument

12. parameters vs. arguments -> parameters: what we can give to the function like when declaring a function
    argument: what we are giving actually to the function like when calling a function 
13. Two parameters in print() : sep and end.
    sep-> print that thing between the two arguments by default it's sep=' ' a space
    e.g. print("Fizaan","Ali",sep="Haha") it separates the two arguments with that  text
    end-> print that thing at the end of function by default it's new line end='\n'
    e.g. print("Fizaan",end="$") now it's gonna print dollar sign at the end

14. positional parameters and named parameters -> positional: position depends what writes first print first
    named: doesn't depend on position optional maybe
15. now how to print the quotes inside print which is already in quotes
    i. first use different types of quotes like e.g.
    print("My name is 'Fizaan'.")  if double outside then single inside and vice versa
    ii. secondly we can use escape characters \" like this
    print("My name is \"Fizaan\".")

16. f string / Format string -> we can put variables and things inside string and first format then print
    print(f"My name is {name}.")
17. also there are many built in functions for strings
18. Interactice mode of python. run python directly in terminal without use of .py file
19. input functions always return string
20. calculator
21. round function 
22. f string more  formatting 
    e.g. print(f"{z:,}") ?? what's this
         print(f"{z:.2f}") ?? 
23. def keyword
24. provide default values to functions using = after parameter
    def hello(name="Fizaan"):
        # blah blah
25. function definition should be above than function calling 
    or by doing this 
    def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print("Hello,", to)

main() 

wrapping our code in main function but i don't know how itworks?

Reason: claude'  How Python Actually Executes a File
Think of it like this:
Python reads your file top to bottom, line by line.
But def is special — when Python hits a def, it says:

"Okay, I'll remember this function exists, but I won't run what's inside it."

So the contents of a function are frozen until someone actually calls it.

26. scope of variable: 
27. return values of functioons 

'''