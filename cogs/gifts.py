import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

import glob, random

from info.ids import guild_ids
guild_ids_list = [guild_ids["blahajgang"]]

class Gifts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name="colors", guild_ids=guild_ids_list, description="gift a pride flag!", 
    options=[create_option(
            name="recipient",
            description="Who do you want to give this to?",
            option_type=6, #corresponds to USER
            required=False),
            create_option(
            name="reason",
            description="Why are you gifting this to them?",
            option_type=3, #corresponds to STRING
            required=False)
            ])
    async def colors(self, ctx, recipient=None, reason=None):
        mention = recipient.id if recipient else None
        myid = ctx.author_id 
        if not reason:
            reason = "no reason, you simply deserve it. yeet"
        if not mention:
            await ctx.send(content="To whom should I send a gift?")
        elif mention == myid:
            await ctx.send(content="Ha! you can't gift yourself.")
        
        else:
            path = ["./images/flags/*.png"]
            random_flag = glob.glob(random.choice(path))
            await ctx.send(
                "<@{mention}> Here's a gift from blahaj:\n".format(
                        mention=mention, reason=reason),
                    file=discord.File(random.choice(random_flag)))

    @cog_ext.cog_slash(name="gift", guild_ids=guild_ids_list, description="gift a friendo a blahaj!", 
    options=[create_option(
            name="recipient",
            description="Who do you want to give this to?",
            option_type=6, #corresponds to USER
            required=False),
            create_option(
            name="reason",
            description="Why are you gifting this to them?",
            option_type=3, #corresponds to STRING
            required=False)
            ])
    async def gift(self, ctx, recipient=None, reason=None):
        mention = recipient.id if recipient else None
        myid = ctx.author_id 
        if not reason:
            reason = "no reason, you simply deserve it. yeet"
        if not mention:
            await ctx.send(content="To whom should I send a gift?")
        elif mention == myid:
            await ctx.send(content="Ha! you can't gift yourself.")
        else:
            await ctx.send(
                content="<@{mention}>, here's a plushie for you!\n reason: {reason}".format(
                    mention=mention, reason=reason),
                file=discord.File('./images/giftBlahaj.png'))

def setup(bot):
    bot.add_cog(Gifts(bot))