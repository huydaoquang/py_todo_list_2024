# "r" - Read - 
# "a" - Append -
# "w" - Write - 
# "x" - Create - 
# "t" - Text -
# "b" - Binary 

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
    f = open("demofile5.txt", "w")
    f.write("test")
    f.close()
    print("The file does not exist")