import random
def randInt(min = 0, max = 100):
    if max > 0 and max > min:
        return round(random.random() * (max-min) + min)
    else: return "Max value has to be greater than zero and minmum value!"

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print(randInt(min=50, max=1))    # should Max value has to be greater than zero and minmum value!
print(randInt(min=-10, max=-1))    # should Max value has to be greater than zero and minmum value!