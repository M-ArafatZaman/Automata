import discord
from discord.ext import commands

from Plugin import AutomataPlugin

VIBE_IMAGE = "https://s3.gifyu.com/images/catvibe.gif"

class Vibe(AutomataPlugin):
    """Cat Bop"""

    @commands.command()
    async def vibe(self, ctx: commands.Context):
        """Replies with a Cat Bop Gif!"""

        await ctx.send(VIBE_IMAGE)
