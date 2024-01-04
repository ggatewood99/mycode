#!/usr/bin/env python3
hostname = input("What value should we set for the hostname?")
## notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The ostname was found to be mtg")
