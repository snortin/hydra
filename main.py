import discord
import os
from colorama import Fore as f
from pystyle import Colors, Colorate

client = discord.Client() # client its using in this case is shitty discord

os.system('cls') # if you're using the terminal and not just running it, it clears the terminal retard.

print(Colorate.Vertical(Colors.blue_to_purple, f'''
            :::    ::: :::   ::: :::::::::  :::::::::      :::     
            :+:    :+: :+:   :+: :+:    :+: :+:    :+:   :+: :+:   
            +:+    +:+  +:+ +:+  +:+    +:+ +:+    +:+  +:+   +:+  
            +#++:++#++   +#++:   +#+    +:+ +#++:++#:  +#++:++#++: 
            +#+    +#+    +#+    +#+    +#+ +#+    +#+ +#+     +#+ 
            #+#    #+#    #+#    #+#    #+# #+#    #+# #+#     #+# 
            ###    ###    ###    #########  ###    ### ###     ### 
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 ''')) #ascii title shit

token = input("token: ") #both of these are just variables with inputs to determine the user token and the message that you want dmed
msg  = input('message: ')

os.system('cls') # same as before

#the actual code
@client.event #this cant be a command but an event
async def on_connect(): # connects to users token as like a selfbot
    for f in client.user.friends: # finds how many friends are in friends list and stores it in db

        try: # try statement if the token is correct or not reset it will mass send the message above that you put in the input
            await f.send(msg) # ratio
            print(f"{f.GREEN}Messaged: {f.LIGHTBLUE}[{f.name}] / {f.RESET}{msg}") # ratio            
        except: # except statement if the token is incorrect it states a error message
            print(f'{f.RED}Couldnt message: {f.LIGHTBLUE}[{f.name}] / {f.RESET}{msg}') # error message
            pass
            
client.run(token, bot=False) # ratio
