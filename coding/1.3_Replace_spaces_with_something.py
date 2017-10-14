
def replacespaces(inputstring,pattern):
    return pattern.join(inputstring.split())


print replacespaces('Hello World USA ','%20')



