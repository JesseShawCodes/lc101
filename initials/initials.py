def get_initials(val):
    initials = ""
    for i in range(0,len(val)): 
        if(i == 0):
            initials+=val[i]
        if(val[i] == " "):
            initials+=val[i+1]
    initials_output = initials.upper()
    return initials_output

def inititials_one():
    x = raw_input("What is your full name?: ")
    return get_initials(x)
    # some more code here (input and print statements)


print(inititials_one())