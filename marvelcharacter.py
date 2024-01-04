#!usr/bin/python3

#dictionary chontaining characters attributes
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
#asking user input
char_name =input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n")
char_stat =input("What statistic do you want to know about? (real name, powers, archenemy)\n")

#
value = marvelchars.get(char_name, {}).get(char_stat)

print(f"{char_name} {char_stat} is: {value}")


 
