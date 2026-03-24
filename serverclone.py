import discord
import aiohttp
from colorama import Fore, init, Style

init()

def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[WARNING]{Style.RESET_ALL} {message}')


def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')


class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
            for role in guild_to.roles:
                try:
                    if role.name != "@everyone":
                        await role.delete()
                        print_delete(f"Deleted Role: {role.name}")
                except discord.Forbidden:
                    print_error(f"Error While Deleting Role: {role.name}")
                except discord.HTTPException:
                    print_error(f"Unable to Delete Role: {role.name}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != "@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Created Role {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Create Role: {role.name}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Channel: {channel.name}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    if role:
                        overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
                print_add(f"Created Category: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Category: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Create Category: {channel.name}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        for channel_text in guild_from.text_channels:
            try:
                category = None
                if channel_text.category:
                    category = discord.utils.get(guild_to.categories, name=channel_text.category.name)

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    if role:
                        overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Created Text Channel: {channel_text.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Text Channel: {channel_text.name}")
            except discord.HTTPException:
                print_error(f"Unable To Create Text Channel: {channel_text.name}")
            except:
                print_error(f"Error While Creating Text Channel: {channel_text.name}")

        for channel_voice in guild_from.voice_channels:
            try:
                category = None
                if channel_voice.category:
                    category = discord.utils.get(guild_to.categories, name=channel_voice.category.name)

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    if role:
                        overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                        )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Created Voice Channel: {channel_voice.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Voice Channel: {channel_voice.name}")
            except discord.HTTPException:
                print_error(f"Unable To Create Voice Channel: {channel_voice.name}")
            except:
                print_error(f"Error While Creating Voice Channel: {channel_voice.name}")


    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Deleted Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Emoji: {emoji.name}")
            except discord.HTTPException:
                print_error(f"Error While Deleting Emoji: {emoji.name}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        emoji: discord.Emoji
        async with aiohttp.ClientSession() as session:
            for emoji in guild_from.emojis:
                try:
                    async with session.get(emoji.url) as resp:
                        if resp.status == 200:
                            emoji_image = await resp.read()
                            await guild_to.create_custom_emoji(
                                name=emoji.name,
                                image=emoji_image)
                            print_add(f"Created Emoji: {emoji.name}")
                        else:
                            print_error(f"Failed to download emoji: {emoji.name}")
                except discord.Forbidden:
                    print_error(f"Error While Creating Emoji: {emoji.name}")
                except discord.HTTPException:
                    print_error(f"Error While Creating Emoji: {emoji.name}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            await guild_to.edit(name=guild_from.name)
            print_add(f"Guild Name Changed to: {guild_to.name}")
            
            if guild_from.icon:
                async with aiohttp.ClientSession() as session:
                    async with session.get(guild_from.icon.url) as resp:
                        if resp.status == 200:
                            icon_image = await resp.read()
                            await guild_to.edit(icon=icon_image)
                            print_add(f"Guild Icon Changed: {guild_to.name}")
                        else:
                            print_error(f"Failed to download icon from {guild_from.name}")
        except discord.Forbidden:
            print_error(f"Error While Changing Guild Settings: {guild_to.name}")
        except Exception as e:
            print_error(f"Error: {e}")