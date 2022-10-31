# create a function to get a random port number
import random
def random_port(lower_limit=21, upper_limit=443):
    return random.randint(lower_limit,upper_limit)



# invocation
port_number = random_port() # default range
print(port_number)

# port_number = random_port(0,10) # default range
# print(port_number)
#
# port_number = random_port(400) # default range
# print(port_number)
#

