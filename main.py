import random

begin = input("Welcome to the command module to continue please press y. ")
if begin != "y":
  print("ERROR, PLEASE RESTART CODE. CODE IS TERMINATED")
  sys.exit()
help = input("Beggining module, for a list of commands please type, Help, If wishing to continue please input, y ")
if help == "Help":
  print("--------------------")
  print("COMMANDS:::"
       + "TERMINATE, forces system termination, LINK, gives links for Khan Academy, " 
        + "IMAGE, provides link to 1 of 10 images, " 
       + "LIST, creates list for 5 items, " 
        + "INSTALL, access to google play:::   ")
  print("--------------------")
  print("Loading command terminal")
  print("--------------------")
elif help == "y":
  print("--------------------")
else:
  print("Command not recognised. Please check spelling and cases: ***MODULE TERMINATED PLEASE RESTART***")
  sys.exit()
print("Command max: 10 : Before auto TERMINATION...:")
for command in range(10):
  DING = input()
  if DING == "TERMINATE":
    sys.exit()
  else:
    print("Command not recognised, -1")
  