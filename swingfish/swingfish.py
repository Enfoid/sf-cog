import asyncio
import json
from datetime import datetime
from random import choice
from time import time

import discord
from discord.ext.commands import Bot, guild_only
from pip._vendor import requests
from redbot.core import checks
from redbot.core.commands import commands, Context

BaseCog = getattr(commands, "Cog", object)

class SwingFish(BaseCog):
    """SwingFish Server Commands"""

    def __init__(self, bot: Bot):
        self.bot = bot

        self.guild_id = 292323550990172170
        self.mario = "292321992269496320"

        self.channel_hodlmybeer = "392963982073528333"
        self.channel_tradingroom = "292323550990172170"
        self.channel_cabincrew = "342571048463499265"
        self.channel_log = "517175223557029909"

        self.role_permRookie = "510711778263564288"
        self.role_rookie = "Rookie"
        self.role_investor = "Investor"
        self.role_slowpoke = "SlowPoke"
        self.role_addict = "505419585122467860"
        self.role_prop = "440806300641918977"
        self.role_wallstreet = "WallStreet"
        self.role_crypro = "Crypto"
        self.role_quant = "Quant"

    def fetch_joined_at(self, user, server):
        """Just a special case for someone special :^)"""
        if user.id == "96130341705637888" and server.id == "133049272517001216":
            return datetime(2016, 1, 10, 6, 8, 4, 443000)
        else:
            return user.joined_at

    @commands.command()
    @checks.admin_or_permissions(kick_members=True)
    async def webaccess(self, ctx: Context):
        self._update_users(292344451295215616)  # cabincrew
        self._update_users(459701647489105943)  # firstmate
        self._update_users(440806300641918977)  # enfoid
        self._update_users(752105907621593098)  # prop
        self._update_users(368615195343585310)  # addicts
        self._update_users(368741515750801409)  # Investor
        self._update_users(368615284203847681)  #  Slowpoke
        self._update_users(418734714527023129)  #  Rookie
        self._update_users(510711778263564288)  # branagain
        self._update_users(492623184957407243)  # fanboy/alcoholic
        self._update_users(510359728392503307)  # 8 ball (for prop access)
        await ctx.send("Updating Permissions for Web access.")

    def _update_users(self, role_id):
        guild: discord.Guild = self.bot.get_guild(self.guild_id)
        if not guild:
            return
        role = guild.get_role(role_id)
        if not role:
            return
        fname = f'data/swingfish/user_data_{role_id}.json'
        a = []
        for m in guild.members:
            if role in m.roles:
                a.append(m.id)
        try:
            with open(fname) as f:
                data = json.load(f)
        except:
            data = {}

        data[role.id] = a
        with open(f'/var/www/swingfish.trade/html/assets/cache/discord_members_{role_id}.json', 'w') as f:
            json.dump(data, f)

    @commands.command()
    async def help(self, ctx: Context):
        """Need Help .. huh ?"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description="SwingFish Discord Commands at your disposal",
            colour=discord.Colour(value=colour))
        data.add_field(name="more details", value="https://www.swingfish.trade/discord#bots")
        #        data.set_footer(text="Updated: moments ago",icon_url="https://www.swingfish.trade/assets/images/chat/Hermes.png")

        try:
            await ctx.send(embed=data)
        except discord.Forbidden:
            await ctx.send("I need the `Embed links` permission "
                           "to send this")

    @commands.command()
    async def rules(self, ctx: Context):
        """our Laws"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        embed = discord.Embed(
            colour=discord.Colour(value=colour), url="https://www.swingfish.trade/discord",
            description="SwingFish is Provided and maintained by "
                        "[EnFoid Pte. Ltd.](https://www.enfoid.com/project/swingfish) as a free community Service, "
                        "to bring Traders and Peoples Interested in Trading together."
        )

        embed.set_thumbnail(url="https://www.swingfish.trade/assets/images/swingfish-bg-logo-square-cycle_320.png")
        embed.set_author(name="SwingFish.Trade Community Rules",
                         url="https://swingfish.trade/discord",
                         icon_url="https://www.swingfish.trade/assets/images/swingfish-bg-logo-square-cycle_320.png")

        embed.add_field(
            name="Cost",
            value="this Service is Free of Monetary charges,\n"
                  "payment in the form of constructive contributions, help & support towards other Members is "
                  "however mandatory."
        )
        embed.add_field(
            name="Common Sense",
            value="it's always open season for Spam, Troll, and other Garbage Users.\n"
                  "lack of mutual respect will result in lack of your presence here."
        )
        embed.add_field(
            name="who said this is a Democracy?",
            value="You have NO RIGHT of being here!\n"
                  "Using the Chat is a Privilege, not a Right!\n.\n"
                  "Decisions of our Moderators are final!\n"
                  "Not subject to appeal, discussion\n"
                  "or any other form of Quality and/or Performance review."
        )
        embed.add_field(
            name="this is not everything!",
            value="the full set of the Terms and Conditions can be found on our Website "
                  "[https://www.swingfish.trade](https://www.swingfish.trade/discord)"
        )

        try:
            await ctx.send(embed=embed)
            await ctx.send("use **!rulest** for #tradingroom specific rules")
        except discord.Forbidden:
            await ctx.send("I need the `Embed links` permission to send this")

    @commands.command()
    async def rulest(self, ctx: Context):
        """our Tradingroom Rules"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(
            colour=discord.Colour(value=colour),
            url="https://www.swingfish.trade/discord",
            description="in addition to common sense, here are some rules for all Trading Related Channels"
        )

        embed.set_author(name="Special rules for #tradingroom and TradingTalk (Voice)",
                         url="https://swingfish.trade/discord",
                         icon_url="https://www.swingfish.trade/assets/images/swingfish-bg-logo-square-cycle_320.png")

        embed.add_field(
            name="Privacy",
            value="by joining you agree and permit that your Username, Messages written in #tradingroom, "
                  "spoken words in #TradingTalk may or may not show on the Website and/or Livestream(s)."
        )
        embed.add_field(
            name="There shall be no:",
            value="- memes, Emoji's or other nonsense for no reason, [are you 5?]\n"
                  "- profit/loss Posts (unless they are in Percentages), [nobody cares how rich you are]\n"
                  "- Market cheering, [it's not the Super-ball]\n"
                  "- Calls without proper analysis,[be credible]\n"
                  "- discussions about the obvious. [we do NOT breed Trolls here]\n"
                  "in short: **Keep it professional**"
        )
        embed.add_field(
            name="Voice Chats",
            value="- no discrimination, hate speech, drunk, or brainless conversation of any kind, "
                  "[it's not your Trailer park]\n"
                  "- no Music or any other form of Copyrighted content, [this will NOT be Tolerated even a second!]\n"
                  "- keep your hardware in check, make sure you can be heard properly and we not hear your dishwasher."
        )
        embed.add_field(
            name="more ?",
            value="the full set of the Terms and Conditions can be found on our Website "
                  "[https://www.swingfish.trade](https://www.swingfish.trade/discord)"
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I need the `Embed links` permission to send this")

    @commands.command(aliases=["rebate"])
    @guild_only()
    async def ib(self, ctx: Context):
        """SwingFish IB Links"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        guild = ctx.message.guild

        data = discord.Embed(
            description="[SwingFish's Brokers](https://www.swingfish.trade/brokers) with Cash-back Rewards",
            colour=discord.Colour(value=colour)
        )

        data.add_field(
            name="cTrader",
            value="[IC Markets](https://www.swingfish.trade/lib/ib/icmarkets)\n"
                  "[RoboForex](https://my.roboforex.com/en/?a=lhft) | "
                  "[Tradersway](https://www.swingfish.trade/lib/ib/tradersway)",
            inline=False
        )
        data.add_field(
            name="mt4/mt5",
            value="[usgFX](https://www.swingfish.trade/lib/ib/usgfx) | "
                  "[AVATrade](https://www.swingfish.trade/lib/ib/avatrade) | "
                  "[BlackBull](https://www.swingfish.trade/lib/ib/blackbull)\n"
                  "[Tradersway](https://www.swingfish.trade/lib/ib/tradersway) (accepts US Clients)",
            inline=False
        )

        try:
            await ctx.send(embed=data)
        except discord.Forbidden:
            await ctx.send("I need the `Embed links` permission to send this")

    @commands.command()
    @guild_only()
    async def calc(self, ctx: Context, num1, action, num2):
        """do some basic math (+ - * /) Example: !calc 17 + 4"""
        int(num1)
        int(num2)
        #        await ctx.send('thinking...')
        if action == "+":
            final = int(num1) + int(num2)
            await ctx.send(str(num1) + str(action) + str(num2) + '= **' + str(final) + '**')
        elif action == "-":
            final = int(num1) - int(num2)
            await ctx.send(str(num1) + str(action) + str(num2) + '= **' + str(final) + '**')
        elif action == "*":
            final = int(num1) * int(num2)
            await ctx.send(str(num1) + str(action) + str(num2) + '= **' + str(final) + '**')
        elif action == "/":
            final = int(num1) / int(num2)
            await ctx.send(str(num1) + str(action) + str(num2) + '= **' + str(final) + '**')
        else:
            await ctx.send('sorry i didn\'t get that, please use !calc Number +-*/ Number')

    @commands.command(aliases=["streams"])
    @guild_only()
    async def liveo(self, ctx: Context):
        """Livestream Status"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        r = requests.get("http://www.swingfish.trade/lib/3rd/discord/youtubejson.php")
        youtube = r.json()
        if youtube:
            data = discord.Embed(
                description="SwingFish's [Youtube Channel](https://www.youtube.com/SwingFish/)",
                colour=discord.Colour(value=colour))
            #            data.add_field(name="Videos", value=str(youtube['videocount']), inline=True)
            #            data.add_field(name="Traded Equity", value=str(int(round(enfdata['equity'],-2)))+"$", inline=True)
            #            data.add_field(name="Equity Swap", value=str(int(round(enfdata['swap'],-2)))+"$", inline=True)
            #            data.add_field(name="Lenders Backing", value=str(round(enfdata['backedby'],1))+ "%", inline=True)
            #            data.add_field(name="Transferable (this week)", value=str(int(round(enfdata['newsize'],-2)))+"$", inline=True)

            #            data.add_field(name="EnFoid Fund", value="[Detailed Informations about EnFoid Investor Relations](https://www.enfoid.com/investors/dv&discord=true)", inline=False)
            data.add_field(name='Status', value="Streaming Live NOW", inline=True)
            #            data.add_field(name="via", value="[YouTube](https://youtu.be/"+youtube['videoId']+") | [ Twitch ](https://www.twitch.tv/swingfish12) | [ FaceBook ](https://facebook.com/swingfish12/live) | [ Twitter / Periscope ](https://www.pscp.tv/nullx8) | [ Mixer ](https://mixer.com/SwingFish)\n", inline=False)
            data.add_field(
                name="via",
                value=f"[YouTube](https://youtu.be/{youtube['videoId']}) | "
                      f"[ Twitch ](https://www.twitch.tv/swingfish12) | "
                      f"[ FaceBook ](https://facebook.com/swingfish12/live) | "
                      f"[ Twitter / Periscope ](https://www.pscp.tv/nullx8) | "
                      f"[ Smashcast ](https://www.smashcast.tv/SwingFish)\n",
                inline=False
            )
            data.add_field(name="LIVE NOW!!", value=str(youtube['title']), inline=False)

            #            data.set_footer(text="Updated: moments ago",icon_url="https://www.swingfish.trade/assets/images/chat/Hermes.png")
            #            data.set_image(url="https://img.youtube.com/vi/"+youtube['videoId']+"/hqdefault.jpg")
            #            data.set_thumbnail(url="https://image.flaticon.com/icons/png/128/890/890779.png")
            data.set_thumbnail(url=f"https://img.youtube.com/vi/{youtube['videoId']}/hqdefault.jpg")

            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                await ctx.send("I need the `Embed links` permission to send this")

        else:
            await ctx.send("could not get Youtube Data")

    @commands.command(aliases=["swingfish"])
    @guild_only()
    async def swingfishinfo(self, ctx: Context):
        """SwingFish Trade Stats"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        r = requests.get("http://enfoid.com/api/c/fundstats.json")
        enfdata = r.json()
        if enfdata:
            data = discord.Embed(
                description="SwingFish Trade Stats (last 30 days)",
                colour=discord.Colour(value=colour)
            )
            data.add_field(
                name="Fund Allocation",
                value=f"{enfdata['visuals']['swingfish1000']['fundcoverage']}% "
                      f"[details](https://www.enfoid.com/investors/trade?dv=true)",
                inline=True
            )
            data.add_field(name="Gain", value=f"{enfdata['visuals']['swingfish1000']['gain']}%", inline=True)
            #            data.add_field(name="Capital", value="$"+str(enfdata['visuals']['swingfish1000']['allocated']), inline=True)
            data.add_field(name="Lots Traded", value=str(int((enfdata['visuals']['swingfish1000']['volume'] / 100000))),
                           inline=True)

            data.add_field(name="Total Trades", value=str(enfdata['visuals']['swingfish1000']['TradesTotal']),
                           inline=True)
            data.add_field(name="Trades Won", value=str(enfdata['visuals']['swingfish1000']['TradesWon']),
                           inline=True)
            data.add_field(name="Profit Days", value=f"{enfdata['visuals']['swingfish1000']['DaysWon']} out of 30",
                           inline=True)
            data.add_field(name="Profit Factor", value=str(enfdata['visuals']['swingfish1000']['Profitfactor']),
                           inline=True)
            data.add_field(name="Sharpe Ratio", value=str(enfdata['visuals']['swingfish1000']['Sharperatio']),
                           inline=True)

            data.add_field(
                name="Profit-Share",
                value="[Detailed Informations about SwingFish Profit-Share]"
                      "(https://www.enfoid.com/investors/profit-share?dv=true)",
                inline=False
            )
            data.add_field(name="Tradingroom",
                           value="[where the magic happens](https://www.swingfish.trade/tradingroom)",
                           inline=False)
            data.set_footer(text=f"Updated: {enfdata['visuals']['swingfish1000']['updatedAgo']}",
                            icon_url="https://www.swingfish.trade/assets/images/chat/Hermes.png")
            data.set_thumbnail(url="https://www.swingfish.trade/assets/images/swingfish/square_360.png")

            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                await ctx.send("I need the `Embed links` permission to send this")

        else:
            await ctx.send("could not get stats from EnFoid")

    @commands.command(aliases=["enfoid"])
    @guild_only()
    async def enfoidinfo(self, ctx: Context):
        """EnFoid Fund Status"""

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        guild = ctx.message.guild
        count_el = 0
        for member in guild.members:
            for role in member.roles:
                if role.name == "EnFoid Member":
                    count_el += 1

        r = requests.get("http://enfoid.com/api/c/fundstats.json")
        enfdata = r.json()
        if enfdata:
            data = discord.Embed(
                description="EnFoid Lender Stats",
                colour=discord.Colour(value=colour))
            data.add_field(name="Total Accounts", value=str(enfdata['totals']['lenders']['count']), inline=True)
            data.add_field(name="in this Discord",
                           value=f"{count_el} [Link your Discord](https://www.enfoid.com/inc/ajax/linkdiscord.php)",
                           inline=True)
            data.add_field(name="Traded Equity", value=f"{int(round(enfdata['totals']['equity'], -2))}$", inline=True)
            data.add_field(name="Equity Swap", value=f"{int(round(enfdata['totals']['swap'], -2))}$", inline=True)
            data.add_field(name="Lenders Backing", value=f"{round(enfdata['totals']['lenders']['backed'], 1)}%",
                           inline=True)
            data.add_field(name="Transferable (this week)", value=f"{int(round(enfdata['totals']['newsize'], -2))}$",
                           inline=True)

            data.add_field(
                name="Paid to SwingFish Members (last 30 days)",
                value=f"{int(round(enfdata['stats']['iblink']['m'], 0))}$ "
                      f"[it\'s Free Money, Get It!](https://www.enfoid.com/blog/free-money-has-a-name-enfoid-iblink)",
                inline=True
            )

            data.add_field(
                name="EnFoid Fund",
                value="[Detailed Informations about EnFoid Investor Relations]"
                      "(https://www.enfoid.com/investors/dv&discord=true)",
                inline=False
            )
            data.set_footer(text="Updated: moments ago",
                            icon_url="https://www.swingfish.trade/assets/images/chat/Hermes.png")
            data.set_thumbnail(url="https://www.enfoid.com/assets/images/enfoid-lenders-logo.png")

            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                await ctx.send("I need the `Embed links` permission to send this")

        else:
            await ctx.send("could not get stats from EnFoid")

    @commands.command()
    @guild_only()
    async def serverinfo(self, ctx: Context):
        """Shows server's informations"""
        guild = ctx.message.guild
        online = len([m.status for m in guild.members if m.status != discord.Status.offline])
        total_users = len(guild.members)
        text_channels = len([x for x in guild.channels if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in guild.channels if x.type == discord.ChannelType.voice])
        passed = (ctx.message.created_at - guild.created_at).days
        created_at = f"Since {guild.created_at.strftime('%d %b %Y %H:%M')} (about {passed} days ago)"

        # get member roles count (Slowpokes and Addicts
        count_sp = 0
        count_ad = 0
        count_ws = 0
        count_pt = 0
        for member in guild.members:
            for role in member.roles:
                if role.name == "SlowPoke":
                    count_sp += 1
                if role.name == "Addict":
                    count_ad += 1
                if role.name == "WallStreet":
                    count_ws += 1
                if role.name == "EnFoid Gang":
                    count_pt += 1

        list_mods = guild.owner.name
        role = discord.utils.get(ctx.message.guild.roles, name="CabinCrew")
        for member in ctx.message.guild.members:
            if role in member.roles:
                list_mods = f"{list_mods}, {member.name}"
        #                await self.bot.say("{0.name}: {0.id}".format(member))

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Users", value=f"{online}/{total_users}")
        data.add_field(name="Voice Region", value=str(guild.region))
        data.add_field(name="Channels", value=f"{text_channels}/{voice_channels}")
        #        data.add_field(name="Voice Channels", value=voice_channels)
        #        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="EnFoid Traders", value=str(count_pt))
        data.add_field(name="SlowPokes", value=str(count_sp))
        data.add_field(name="Addicts", value=str(count_ad))
        data.add_field(name="the God's", value=list_mods)
        data.add_field(
            name="More info",
            value="check [www.swingfish.trade](https://www.swingfish.trade/discord) for details, Signals, "
                  "Videos and more"
        )
        #        data.set_footer(text="more info [Click HERE](https://www.swingfish.trade/discord)")

        if guild.icon_url:
            data.set_author(name=guild.name, url="https://www.swingfish.trade/discord")
            data.set_thumbnail(url=guild.icon_url)
        else:
            data.set_author(name=guild.name)

        try:
            await ctx.send(embed=data)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")

    @commands.command(aliases=["ui"])
    @guild_only()
    async def userinfo(self, ctx: Context, *, user: discord.Member = None):
        """Shows users's informations"""
        author = ctx.message.author
        guild = ctx.message.guild

        if not user:
            user = author

        roles = [x.name for x in user.roles if x.name != "@everyone" and x.name != "."]

        joined_at = self.fetch_joined_at(user, guild)
        since_created = (ctx.message.created_at - user.created_at).days
        since_joined = (ctx.message.created_at - joined_at).days
        member_number = sorted(guild.members, key=lambda m: m.joined_at).index(user) + 1

        created_on = f"{since_created} days"
        joined_on = f"{since_joined} days (No {member_number})"

        game = "Chilling in {user.status} status"

        if isinstance(user.activity, discord.Game):
            game = f"Playing {user.activity.name}"
        elif isinstance(user.activity, discord.Streaming):
            game = f"Streaming: [{user.activity.game}]({user.activity.url})"

        if len(roles) > 0:
            roles = ", ".join(roles)
        else:
            roles = "None"

        data = discord.Embed(description=game, colour=user.colour)
        data.add_field(name="on Discord", value=created_on)
        data.add_field(name="with SwingFish", value=joined_on)
        data.add_field(name="Roles", value=roles, inline=True)
        #        data.add_field(name="Rank", value=member_number, inline=True)

        name = str(user)
        name = " ~ ".join((name, user.nick)) if user.nick else name

        r = requests.get("http://enfoid.com/inc/ajax/lenderstats.php?uid=" + str(user.id))
        enfdata = r.json()
        if enfdata:
            if enfdata['cycles'] > 0:
                role = user.guild.get_role(440806300641918977)
                await user.add_roles(role)
                data.add_field(
                    name="EnFoid Lender Stats",
                    value=f"{enfdata['gain']}% Absolute Gain\n"
                      f"in {enfdata['cycles']} Weeks [[what is this?](https://www.enfoid.com/investors/dv?r=discord)]",
                    inline=True
                )
            #            data.add_field(name="Lender Gain", value=str(enfdata['gain'])+"%", inline=True)

            else:
                role = user.guild.get_role(440806300641918977)
                await user.remove_roles(role)
                           
            if enfdata['propstatus']:
                if enfdata['propstatus'] == 'Live' or \
                        enfdata['proplive'] == 'true':
                    role = user.guild.get_role(752105907621593098)
                    await user.add_roles(role)
                else:
                    role = user.guild.get_role(752105907621593098)
                    await user.remove_roles(role)
                if enfdata['propstatus'] == 'Evaluation' or \
                        enfdata['propstatus'] == 'Verification' or \
                        enfdata['propstatus'] == 'Live':
                    role = user.guild.get_role(440806300641918977)
                    await user.add_roles(role)
                    # data.add_field(name="Prop Trader Stats", value="Capital: "+str(enfdata['propbalance'])+" USD\nStatus: "+str(enfdata['propstatus'])+" [[see Statistics]("+str(enfdata['proplink'])+")]", inline=True)
                    data.add_field(
                        name="Prop Trader Stats",
                        value=f"Capital: {enfdata['propbalance']} USD\n"
                              f"Status: {enfdata['propstatus']} [[Metrics]({enfdata['proplink']})]",
                        inline=True
                    )
        #                    data.add_field(name="Lender Gain", value=str(enfdata['gain'])+"%", inline=True)
        #                else:
        #                    role = discord.utils.get(user.server.roles, name="EnFoid Prop-Trader")
        #                    await self.bot.remove_roles(user, role)

        else:
            role = user.guild.get_role(752105907621593098)
            await user.remove_roles(role)
                           
        if user.avatar_url:
            data.set_author(name=name, url=user.avatar_url)
            data.set_thumbnail(url=user.avatar_url)
        else:
            data.set_author(name=name)

        try:
            await ctx.send(embed=data)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission "
                           "to send this")

    #    @commands.command(aliases=["price"], pass_context=True, no_pm=False)
    #    async def chart(self, ctx, *asset):
    #        """shows a default chart"""
    #
    #        updated_at = ("shortly")
    #
    #        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
    #        colour = int(colour, 16)
    #
    #        data = discord.Embed(
    #            description="Daily Chart of "+ asset[0].upper(),
    #            colour=discord.Colour(value=colour))
    #        data.set_image(url="https://swingfish.trade/go/stockcharts/?s=" + asset[0].upper() + "&dm={}" . format(int(time.time())))
    #        data.set_footer(text="Updated this just moments ago",icon_url="https://www.swingfish.trade/assets/images/chat/Hermes.png")
    #
    #        try:
    #            await ctx.send(embed=data)
    #        except discord.HTTPException:
    #            await ctx.send("I need the `Embed links` permission "
    #                               "to send this")

    @commands.command()
    @guild_only()
    async def div(self, ctx, timeframe: int = 6):
        """Shows Currency Divergences
        default 6 hours
        timeframe 1, 4, 6, 12, 36, 96, 1050"""

        updated_at = ("shortly")
        image = ""
        ftext = ""
        ficon = ""

        if timeframe == 1:
            des = f"Currency Divergences ({timeframe} hour)"
            image = f"http://xscalp.com/data/CS-FastDeltaDivergeRaw.png?n={int(time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        elif timeframe == 4:
            des = f"Currency Divergences ({timeframe} hours)"
            image = f"http://xscalp.com/data/CS-FastDeltaDiverge.png?n={int(time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        elif timeframe == 6:
            des = f"Currency Divergences ({timeframe} hours)"
            image = f"http://xscalp.com/data/CS-6hours.png?n={int(time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        elif timeframe == 12:
            des = f"Currency Divergences ({timeframe} hours)"
            image = f"http://xscalp.com/data/CS-12hours.png?n={int(time.time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        elif timeframe == 36:
            des = f"Currency Divergences ({timeframe} hours)"
            image = f"http://xscalp.com/data/CS-36hoursDiverge.png?n={int(time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        elif timeframe == 96:
            des = f"Currency Divergences ({timeframe} hours)"
            image = f"http://xscalp.com/data/CS-96hoursDiverge.png?n={int(time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        elif timeframe == 1050:
            des = f"Currency Divergences ({timeframe} hours)"
            image = f"http://xscalp.com/data/CS-1050hours.png?n={int(time())}"
            ftext = "Updated just moments ago via xscalp.com"
            ficon = "https://www.swingfish.trade/assets/images/chat/Hermes.png"
        else:
            des = "use Parameters 4, 12, 36, 96 or 1050 (eg. !div 36)\n" \
                  "you can also send me this command as Private Message"

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        if image != "":
            data = discord.Embed(
                description=des,
                colour=discord.Colour(value=colour)
            )
            data.set_image(url=image)
            data.set_footer(text=ftext, icon_url=ficon)
            try:
                await ctx.send(embed=data)
            except discord.HTTPException:
                await ctx.send("I need the `Embed links` permission "
                                   "to send this")
        else:
            await ctx.message.delete()
            msg = await ctx.send(des)
            await asyncio.sleep(10)
            await msg.delete()
