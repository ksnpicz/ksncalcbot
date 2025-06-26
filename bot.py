import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.command()
async def arb(ctx, odd1: float, odd2: float, total_stake: float):
    inv1 = total_stake / (1 + (odd1 / odd2))
    inv2 = total_stake - inv1
    profit = min(inv1 * odd1, inv2 * odd2) - total_stake

    response = (
        f"📊 **Arbitrage Bet Calculator**\n"
        f"Total Stake: ${total_stake:.2f}\n"
        f"Odds 1: {odd1}, Odds 2: {odd2}\n\n"
        f"➡️ Bet ${inv1:.2f} on Odds {odd1}\n"
        f"➡️ Bet ${inv2:.2f} on Odds {odd2}\n\n"
        f"✅ Guaranteed Profit: ${profit:.2f}"
    )

    await ctx.send(response)

bot.run(os.getenv("TOKEN"))
