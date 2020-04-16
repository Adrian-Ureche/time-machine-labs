"Sample module"

import collections

MESSAGE = 'Greetings. {} times!'
counter = 0

print ('hello')

def greet():
    "Don't do this, its considered bad"
    global counter
    
    x = 'foobar'
    
    counter += 1
    print (MESSAGE.format(counter))
    
    def inner():
        print (x)