#Version v1.0.0
#Imports
import os
import time
from character import Character 

#Welcome banner
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\
                         _______  _       _________    \n\
                        (  ____ \( \      \__   __/    \n\
                        | (    \/| (         ) (       \n\
                        | |      | |         | | _____ \n\
                        | |      | |         | |(_____)\n\
                        | |      | |         | |       \n\
                        | (____/\| (____/\___) (___    \n\
                        (_______/(_______/\_______/    \n\
                                                       \n\
                                                       \n\
     ______            _        _______  _______  _______  _        _______ \n\
    (  __  \ |\     /|( (    /|(  ____ \(  ____ \(  ___  )( (    /|(  ____ \ \n\
    | (  \  )| )   ( ||  \  ( || (    \/| (    \/| (   ) ||  \  ( || (    \/\n\
    | |   ) || |   | ||   \ | || |      | (__    | |   | ||   \ | || (_____ \n\
    | |   | || |   | || (\ \) || | ____ |  __)   | |   | || (\ \) |(_____  )\n\
    | |   ) || |   | || | \   || | \_  )| (      | |   | || | \   |      ) |\n\
    | (__/  )| (___) || )  \  || (___) || (____/\| (___) || )  \  |/\____) |\n\
    (______/ (_______)|/    )_)(_______)(_______/(_______)|/    )_)\_______)\n\
                                                                            \n\
                                                       ")

time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

#Create character
print ("\n\
> Welcome, adventurer! Choose your class.\n\n\
    [B]arbarian        [D]warf\n\
    [E]lf              [M]age")

role = ''
name = ''

while (role != 'b' and role != 'd' and role != 'e' and role != 'm'):
    role = input().lower()

print ("\n\
> And what is your name?\n", sep=' ', end='', flush=True)

while (not name):
    name = input()

print ("\n\
> Well met, " + name + "\n")

player = Character (name=name,role=role,is_new=True)
