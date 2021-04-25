# Randomisation
# Visit https://www.askpython.com/ and search for random modules. 
# Here you will get the different methods implemented by python to generate Random Numbers/Sequences

# Here we need to use random module i.e import random in code
# Modules are piece of code that does a particular task. 
# Like here random is a module created by python so that we do no need to implement the login behind that andcan just call the required function which is needed in our code. 

import random

rand_int = random.randint(1, 10)
print(rand_int)

#random.random() always give floating point output but from 0.0000... to 0.99999.. range only
rand_float = random.random()
print(rand_float)

#Suppose we want to get random floating point numbers say from 0 - 5 range
#Just multiply that number with random(). This will produce output from 0.0000... to  4.9999...
rand_float_range = random.random() * 5 
print(rand_float_range)
