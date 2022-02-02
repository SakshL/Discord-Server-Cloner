import platform
import os
import discord
from serverclone import Clone
from colorama import Fore

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(
        "Lua Cloner - Developed by NotSaksh#6969 and igna#0001")
    os.system("cls")
elif platform.system() == "Linux" or "posix":
    os.system(
        "echo -en \"\033]0;Lua Cloner - Developed by NotSaksh#6969 and igna#0001\a\"")
    os.system("clear")

client = discord.Client()

token = input(f'Please enter your token: ')
guild = input('Please enter guild id you want to copy: ')
output = input('Please enter guild id where you want to copy: ')


@client.event
async def on_ready():
    extrem_map = {}
    print(f"""{Fore.LIGHTMAGENTA_EX}
                                            ██╗     ██╗   ██╗ █████╗  ██████╗██╗      ██████╗ ███╗   ██╗███████╗██████╗ 
                                            ██║     ██║   ██║██╔══██╗██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝██╔══██╗
                                            ██║     ██║   ██║███████║██║     ██║     ██║   ██║██╔██╗ ██║█████╗  ██████╔╝
                                            ██║     ██║   ██║██╔══██║██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
                                            ███████╗╚██████╔╝██║  ██║╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗██║  ██║
                                            ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                            
    {Fore.RESET}""")
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_2 = client.get_guild(int(guild))
    guild_1 = client.get_guild(int(output))
    await Clone.guild_edit(guild_1, guild_2)
    await Clone.roles_delete(guild_1)
    await Clone.channels_delete(guild_1)
    await Clone.roles_create(guild_1, guild_2)
    await Clone.categories_create(guild_1, guild_2)
    await Clone.channels_create(guild_1, guild_2)
    print(f"""{Fore.LIGHTGREEN_EX}


                                             ██████╗██╗      ██████╗ ███╗   ██╗███████╗██████╗ 
                                            ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝██╔══██╗
                                            ██║     ██║     ██║   ██║██╔██╗ ██║█████╗  ██║  ██║
                                            ██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║  ██║
                                            ╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗██████╔╝
                                             ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═════╝ 
                                                   
    {Fore.RESET}""")
    input("Press Any Key to exit...")
    exit()


client.run(token, bot=False)
