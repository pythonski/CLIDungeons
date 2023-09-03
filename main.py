#Version v1.0.0
#Imports
from character import Character 

#Welcome banner
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

#Create character
print ("\n\
> Welcome, adventurer! Choose your class.\n\n\
    [B]arbarian        [D]warf\n\
    [E]lf              [M]age\n")

role = 'a'
name = ''

while (role != 'b' and role != 'd' and role != 'e' and role != 'm'):
    role = input().lower()

print ("\n\
> And what is your name?\n")

while (not name):
    name = input()

print ("\n\
> Well met, " + name + "\n")

player = Character (name=name,role=role,isNew=True)
