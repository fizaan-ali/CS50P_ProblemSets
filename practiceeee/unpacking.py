# *args and **kwargs 
# previously we see * and ** which are for function calling they just spread out size matter should be equal to function parameters
# while *args and **kwargs they help us take variable amount of argumentsin function definition
# *args -> positional ** kwargs -> keywords

def f(*args, **kwargs):
    # print("Positional:", args)
    print("Keyword:", kwargs)

# f(100, 25, 50, 5) # can take variable no. of arguments
f(galleons=100, sickles=25, knuts=50)
