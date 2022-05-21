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

        try: # try statement if the token is correct or not reset it will mas send the message above that you put in the variable
            await f.send(msg) # await function to send message to all friends which in this case is `f` for abbreviation
            print(f"{f.GREEN}Messaged: {f.LIGHTBLUE}[{f.name}] / {f.RESET}{msg}") # tells us if it sent or not because on the await function its own we wouldnt know
            
        except: # except statement if the token is incorrect it states a error message
            print(f'{f.RED}Couldnt message: {f.LIGHTBLUE}[{f.name}] / {f.RESET}{msg}') # error message
            pass # passes the error
            
client.run(token, bot=False) # runs the token, but were not a bot so `bot=False` or we couldve dont `selfbot=True` but yea thats it