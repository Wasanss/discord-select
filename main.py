from discord_components import Button, Select, SelectOption, ComponentsBot
import discord

bot = ComponentsBot("!")
token = "봇 토큰"

@bot.event
async def on_ready():
    print(f"{bot.user} 로 로그인 완료")

@bot.command()
async def 역할(ctx):

    member = ctx.message.author

    role1 = discord.utils.get(ctx.guild.roles, name="샌즈")
    role2 = discord.utils.get(ctx.guild.roles, name="파피루스")
    # name에 역할이름 적으면 댐ㅁㅁ
 
    await ctx.send(
        "골라",
        components=[
            Select(
                placeholder="골라바",
                options=[
                    SelectOption(label="샌즈 역할받기", value="1"),
                    SelectOption(label="파피루스 역할받기", value="2"),
                ],
                custom_id="selecter",
            )
        ],
    )

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel
        lambda inter: inter.custom_id == "selecter"

    interaction = await bot.wait_for(
        "select_option", check=check
    )

    if interaction.values[0] == "1":
        if role1 in member.roles:
            await interaction.send(content='이미 있자나')
        else:
            await member.add_roles(role1)
            await interaction.send(content='지급완료')
        
    if interaction.values[0] == "2":
        if role2 in member.roles:
            await interaction.send(content='이미 있자나')
        else:
            await member.add_roles(role2)
            await interaction.send(content='지급완료')

bot.run(token)