import converters

from converters import kg_to_lbs

import utils


print(kg_to_lbs(100))

print(converters.kg_to_lbs(70))


numbers = [10,50,12,84,15,4]
maximum = utils.find_max(numbers)
print(maximum)

print(max) # built in function

print(max(numbers))