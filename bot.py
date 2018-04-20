import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time
import random
import datetime
import sqlite3

client = commands.Bot(command_prefix = "+")

chat_filter = ["NIG", "NIGGER", "NIGGA", "N1GG3R", "JEW", "JEWS"]
bypass_list = [" "]

@client.event
async def on_ready():
  print("Management || Bot is Online and ready.")
  await client.change_presence(game=discord.Game(name="The Royale Island | +cmds"))

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name="Members")
  await client.add_roles(member, role)
  emb = (discord.Embed(description=None, colour=0x3DF270))
  welcome = client.get_channel("432671080382201857")
  emb.add_field(name="New Member", value="<@%s>! Welcome to The Royale IslandIn the Rules channel you can see the rules." % (member.id), inline=False)
  emb.add_field(name="**HELP** ", value= "In the Looking for partner(s) category you can find people to play with.", inline=False)
  emb.add_field(name="**HELP** ", value= "In the fortnite-stats-check you can use !ftn (Username) to see your Fortnite stats. ", inline=False)
  emb.add_field(name="**HELP** ", value= "To Get your Fortnite Rank, ask staff to use +rank (Rank) Bronze,Silver,Gold,Platnium,Diamond,Ruby,Master. ", inline=False)
  emb.add_field(name="**HELP** ", value= "If you have any Questions Contact a '@Staff' Member. ", inline=False)
  emb.add_field(name="**HELP** ", value= "If you want help, do +help. ", inline=False)
  emb.add_field(name="**HELP** ", value= "Enjoy your Stay! ", inline=False)
  await client.send_message(welcome, embed=emb)

@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**HEY DONT SAY THAT!!**")
                except discord.errors.NotFound:
                    return
    if message.content.upper().startswith('+INFO'):
                                                    embed = discord.Embed(name="The Royale Isnald's info".format(message.server.name), description="Here's what I could find.", color=0x00ff00)
                                                    embed.set_author(name="Info")
                                                    embed.add_field(name="Name", value=message.server.name, inline=True)
                                                    embed.add_field(name="ID", value=message.server.id, inline=True)
                                                    embed.add_field(name="Roles", value=len(message.server.roles), inline=True)
                                                    embed.add_field(name="Members", value=len(message.server.members))
                                                    await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('+ANNOUNCE'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
                                                                             args = message.content.split(" ")
                                                                             chan = client.get_channel("421679943546568704")
                                                                             embed = (discord.Embed(description=None, colour=0x00ff00))
                                                                             embed.add_field(name="Admin Announcement By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                                             embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                                             embed2.add_field(name="You Have Successfully Announced Your Words!", value="You Have Made An Announcement! You Have Announced The Following: %s" % (" ".join(args[1:])), inline=False)
                                                                             await client.send_message(message.channel, embed=embed2)
                                                                             await client.send_message(chan, embed=embed)
                                                                             chann = client.get_channel("421679943546568704")
                                                                             await client.send_message(chann, "@everyone")
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
    if message.content.upper().startswith('+RULES'):
                                                   emb = (discord.Embed(description=None, colour=0x00ff00))
                                                   emb.set_author(name="**RULES**")
                                                   emb.add_field(name="1.", value="Respect All Staff And The Members.", inline=True)
                                                   emb.add_field(name="2.", value= "No Punishment Evasion. ", inline=True)
                                                   emb.add_field(name="3. ", value= "No Toxic Behaviour. ", inline=True)
                                                   emb.add_field(name="4. ", value= "No spamming. ", inline=True)
                                                   emb.add_field(name="5. ", value= "English Only. ", inline=True)
                                                   emb.add_field(name="6. ", value= "No NSFW (inappropriate) Posts in text chat. ", inline=True)
                                                   emb.add_field(name="7.", value= "Use Channels Appropriately. ", inline=True)
                                                   emb.add_field(name="8. ", value= "Do not bully or troll anyone on the server. ", inline=True)
                                                   emb.add_field(name="9. ", value= "No Scamming. ", inline=True)
                                                   emb.add_field(name="10. ", value= "No Advertiseing Any YT Channels or Twitch Channels without permission From the Owner. ", inline=True)
                                                   emb.add_field(name="11. ", value= "Do not  impersonate a Staff Member. ", inline=True)
                                                   emb.add_field(name="12. ", value= "Do not DM anyone on the server to advertise. ", inline=True)
                                                   emb.add_field(name="13. ", value= "No Swearing. ", inline=True)
                                                   emb.add_field(name="14. ", value= "Use common sense. ", inline=True)
                                                   await client.send_message(message.channel, embed=emb)         
    if message.content == "cookies and milk":
        await client.send_message(message.channel, "Here's your cookie :cookie: . Almost forgot your milk :milk:!")
    if message.content.upper().startswith('+PING'):
        userID = message.author.id
        await client.send_message(message.channel, ":ping_pong: pong!")
    if message.content.upper().startswith('+WARN'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
                                                                              args = message.content.split(" ")
                                                                              chan = client.get_channel("432653112700829706")
                                                                              embed = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed.add_field(name="Someone Has Been Warned By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                                              embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed2.add_field(name="You Have Successfully Warned Somebody!", value="You Have Warned Someone! You Have Warned Them For The Following: %s" % (" ".join(args[1:])), inline=False)
                                                                              await client.send_message(message.channel, embed=embed2)
                                                                              await client.send_message(chan, embed=embed)
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
    if message.content.upper().startswith('+MUTE'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           muted = discord.utils.get(message.server.roles, name="Muted")
           await client.add_roles(message.mentions[0], muted)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You have muted <@%s>! Run `?unmute @user` to unmute this user!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))

    if message.content.upper().startswith('+UNMUTE'):
       if "421682342206242836" in [role.id for role in message.author.roles]:
           muted = discord.utils.get(message.server.roles, name="Muted")
           await client.remove_roles(message.mentions[0], muted)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You have unmuted <@%s>! Made a mistake? Use `?mute @user`" % (message.author.id, message.mentions[0].id))
       else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "In the #rules channel you can see the rules. In the Looking for partner(s) category you can find people to play with. In the #fortnite-stats-check you can use !ftn (Username) to see your Fortnite stats. To Get your Fortnite Rank, ask staff to use +rank (Rank) Bronze,Silver,Gold,Platnium,Diamond,Ruby,Master. If you have any Questions Contact a '@Staff' Member")
    if message.content.upper().startswith('+RANK MASTER'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           master = discord.utils.get(message.server.roles, name="Master")
           await client.add_roles(message.mentions[0], master)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Master rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+RANK RUBY'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           ruby = discord.utils.get(message.server.roles, name="Ruby")
           await client.add_roles(message.mentions[0], ruby)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Ruby rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+RANK SILVER'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           silver = discord.utils.get(message.server.roles, name="Silver")
           await client.add_roles(message.mentions[0], silver)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Silver rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+RANK GOLD'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           gold = discord.utils.get(message.server.roles, name="Gold")
           await client.add_roles(message.mentions[0], gold)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Gold rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+RANK BRONZE'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           bronze = discord.utils.get(message.server.roles, name="Bronze")
           await client.add_roles(message.mentions[0], bronze)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Bronze rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+RANK PLATINUM'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           platinum = discord.utils.get(message.server.roles, name="Platinum")
           await client.add_roles(message.mentions[0], platinum)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Platinum rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+RANK DIAMOND'):
        if "421682342206242836" in [role.id for role in message.author.roles]:
           diamond = discord.utils.get(message.server.roles, name="Diamond")
           await client.add_roles(message.mentions[0], diamond)
           await client.send_message(message.channel, "<@%s> :white_check_mark: You given the Diamond rank to <@%s>!" % (message.author.id, message.mentions[0].id))
        else:
           await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('+LOCATION'):
        userID = message.author.id
        randnum = random.randint(1,11)
        if randnum == 1:
            await client.send_message(message.channel,"<@%s> :8ball: Lucky Landing :8ball:" % (userID))
        if randnum == 2:
            await client.send_message(message.channel, "<@%s> :8ball: Salty Springs :8ball:" % (userID))
        if randnum == 3:
            await client.send_message(message.channel, "<@%s> :8ball: Tilted Towers :8ball:" % (userID))
        if randnum == 4:
            await client.send_message(message.channel, "<@%s> :8ball: Pleasent Park :8ball:" % (userID))
        if randnum == 5:
            await client.send_message(message.channel, "<@%s> :8ball: Flush Factory :8ball:" % (userID))
        if randnum == 6:
            await client.send_message(message.channel, "<@%s> :8ball: Snobby Shores :8ball:" % (userID))
        if randnum == 7:
            await client.send_message(message.channel, "<@%s> :8ball: Dusty Depot :8ball:" % (userID))
        if randnum == 8:
            await client.send_message(message.channel, "<@%s> :8ball: Wailing Woods :8ball:" % (userID))
        if randnum == 9:
            await client.send_message(message.channel, "<@%s> :8ball: Retail Row :8ball:" % (userID))
        if randnum == 10:
            await client.send_message(message.channel, "<@%s> :8ball: Tomato Town :8ball:" % (userID))
        if randnum == 11:
            await client.send_message(message.channel, "<@%s> :8ball: Greasy Grove :8ball:" % (userID))
        if randnum == 12:
            await client.send_message(message.channel, "<@%s> :8ball: Loot Lake :8ball:" % (userID))
        if randnum == 13:
            await client.send_message(message.channel, "<@%s> :8ball: Haunted Hills :8ball:" % (userID))
        if randnum == 14:
            await client.send_message(message.channel, "<@%s> :8ball: Moisty Mire :8ball:" % (userID))
        if randnum == 15:
            await client.send_message(message.channel, "<@%s> :8ball: Anarchy Acress :8ball:" % (userID))
        if randnum == 16:
            await client.send_message(message.channel, "<@%s> :8ball: Lonely Lodge :8ball:" % (userID))
        if randnum == 17:
            await client.send_message(message.channel, "<@%s> :8ball: Fatal Fields :8ball:" % (userID))
        if randnum == 18:
            await client.send_message(message.channel, "<@%s> :8ball: Junk Junction :8ball:" % (userID))
        if randnum == 19:
            await client.send_message(message.channel, "<@%s> :8ball: No Where :8ball:" % (userID))
    if message.content.upper().startswith('+CMDS'):
                                                   args = message.content.split(" ")
                                                   emb = (discord.Embed(description=None, colour=0x00ff00))
                                                   emb.set_author(name="**COMMANDS**")
                                                   emb.add_field(name="+cmds", value="gives you commands", inline=True)
                                                   emb.add_field(name="+location", value="gives you a place to land", inline=True)
                                                   emb.add_field(name="+ping", value="plays ping pong", inline=True)
                                                   emb.add_field(name="cookies and milk", value="gives you cookies and milk", inline=True)
                                                   emb.add_field(name="+info", value="gives you server info", inline=True)
                                                   emb.add_field(name="+rules", value="gives you the rules", inline=True)
                                                   emb.add_field(name="+invite", value="N/A", inline=True)
                                                   await client.send_message(message.channel, embed=emb)

    if message.content.upper().startswith('+INVITE'):
        await client.send_message(message.channel, " Here's your invite code! https://discord.gg/jthWPwc")
client.run("NDMyNjU3MjQ5MzM3NDc1MDky.Dawe_Q.o-3ScxXYvzvE9Rt8RuV5A4b0E7k")
