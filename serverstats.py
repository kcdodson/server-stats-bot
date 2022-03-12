# Make Sure that you replace in Line 23 YOUR SERVER ID With your Server ID
# And put at the last line your bot token
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True

client = commands.Bot(command_prefix ='.', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
        print('Bot is ready')
        client.loop.create_task(stats_task())

@client.event
async def stats_task():
   while True:

      guild = client.get_guild(951873373045129246)

      member = guild.members
      boostcount = guild.premium_subscription_count
      botcount = sum(member.bot for member in guild.members)
      vangaurd = guild.get_role(951873373045129250)
      degen = guild.get_role(951873373045129252)

      category = discord.utils.get(guild.categories, name="📊 Server Stats 📊")

      channel1 = category.voice_channels[1]
      await channel1.edit(name=f"Members: {guild.member_count}")
      channel2 = category.voice_channels[2]
      await channel2.edit(name=f"Bots: {botcount}")
      channel3 = category.voice_channels[3]
      await channel3.edit(name=f"Boosts: {boostcount}")
      channel4 = category.voice_channels[4]
      await channel4.edit(name=f"Degen-Team: {len(degen.members)}")
      channel5 = category.voice_channels[5]
      await channel5.edit(name=f"Vangaurd: {len(vangaurd.members)}")
      await asyncio.sleep(60 * 11)

@client.command()
async def help(ctx):
	    embed=discord.Embed(title="Help", description="Help List of Commands")
	    embed.add_field(name=f".statssetup | Install the Server Stats in {ctx.guild}", value=".serverinfo", inline=True)
	    await ctx.send(embed=embed)

@client.command()
async def statssetup(ctx):

        guild = ctx.guild

        if ctx.author.guild_permissions.administrator == False:
            return await ctx.send("You do not have the permission to execute this command.")
        if discord.utils.get(guild.categories, name="Server Stats"):
            return await ctx.send("Server Stats already exist")

        member = guild.members
        boostcount = guild.premium_subscription_count
        botcount = sum(member.bot for member in guild.members)
        vangaurd = guild.get_role(951873373045129250)
        degen = guild.get_role(951873373045129252)
        await ctx.send(len(vangaurd.members))
        await ctx.send(len(degen.members))

        category = await guild.create_category("📊 Server Stats 📊")

        await ctx.guild.create_voice_channel(f"Guild: {guild.name}",category=category)
        await ctx.guild.create_voice_channel(f"Members: {guild.member_count}",category=category)
        await ctx.guild.create_voice_channel(f"Bots: {botcount}",category=category)
        await ctx.guild.create_voice_channel(f"Boosts: {boostcount}",category=category)
        await ctx.guild.create_voice_channel(f"Degen-Team: {len(degen.members)}",category=category)
        await ctx.guild.create_voice_channel(f"Vangaurd: {len(vangaurd.members)}",category=category)

        statsimage = "https://ibb.co/drwnYXX"

        embed=discord.Embed(title="📊```Server Stats successfully installed``` 📊", description=f"{ctx.author.mention}, you have successfully installed the Server Stats in **{ctx.guild}**", color=0x80FF00)
        embed.set_thumbnail(url=statsimage)
        embed.set_footer(text="Information")
        await ctx.send(embed=embed)

client.run("OTUxODg2NDg0NTQwMTI5MzEw.Yit_Xw.8bW6imFH1xXlROFYQ4d5aR17pnI")
