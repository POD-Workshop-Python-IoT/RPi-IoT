def hello(firstname, lastname):
    print("Hello function from Greeting.py!")
    
    myname = " ".join([lastname, firstname]) 
    print("5. Hello {displayname}, welcome to POD workshop!".format(displayname=myname[::-1]))

    #return the first word and count number of words
    return myname.split()[0].capitalize(), len(myname.split())
    
