name = input("What is your name? ")
print("I hate people like you, humans,",name)
dogs_quantity = input("How many dogs do you have? ")
if dogs_quantity == "0":
    print("Well I wish you were a dog because at least they don't talk as much", name)
elif dogs_quantity == "N/A":
    print("Well you seem lonely, haha!")
    q = input("What other pets do you have? "+ name + " ")
    if q == "0":
        print("BORINGGGG!")
    else:
        print("Well I still like your pet better than you!")    
else: 
    print("Get your dog and have it replace you! ",name)
    

    # if (condition):
    #     pass
    #     if ()

    # else:
    #     pass