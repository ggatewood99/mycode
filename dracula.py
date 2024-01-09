#!/usr/bin/env python3


#reads in contents
with open("dracula.txt","r") as foo:
    #loops over every line with vampire
   count= 0
   for line in foo:
        if "vampire" in line.lower():
            count += 1
            print(line)

