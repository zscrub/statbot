import discord
import scrape
import standings

TOKEN = 'NzY2MDg1NTUxNTY4MDYwNDE3.X4eOxA.5UVlY1AowqJbRf-OdT_zk1VIm9A'
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)


    if message.content.startswith('!qb'):
        c = 0
        embed1 = discord.Embed(title ='Passing Stat Leaders', color=0xA750DE)
        for i in scrape.passingStatsList():
            ++c
            if len(i)==3:                
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=True)
            elif len(i)==2:
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=True)
        await message.channel.send(embed=embed1)
            
            
    if message.content.startswith('!yds'):
        c = 0
        embed1 = discord.Embed(title ='Rushing/Receiving Stat Leaders', color=0xA750DE)
        for i in scrape.rushingStatsList():
            ++c
            if len(i) == 3:
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=True)
            elif len(i) == 2:
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=True)
        await message.channel.send(embed=embed1)



    if message.content.startswith('!defense'):
        c = 0
        embed1 = discord.Embed(title ='Defensive Stat Leaders', color=0xA750DE)
        for i in scrape.defensiveStatsList():
            ++c
            if len(i)==3:                
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=True)
            elif len(i)==2:
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=True)
        await message.channel.send(embed=embed1)


    if message.content.startswith('!special'):
        c = 0
        embed1 = discord.Embed(title ='Special Teams Stat Leaders', color=0xA750DE)
        for i in scrape.specialTeamsStatsList():
            ++c
            if len(i)==3:                
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]+' '+'('+i[2]+')'), inline=True)
            elif len(i)==2:
                if c%2!=0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=False)
                elif c%2==0:
                    embed1.add_field(name=i[0], value=(i[1]), inline=True)
        await message.channel.send(embed=embed1)


### AFC STANDINGS ###

    if message.content.startswith('!afc'):
        embed1 = discord.Embed(title = 'AFC Regular Season Standings', color=0xA750DE)
        
        embed1.add_field(name="AFC East - W/L/T", value = '----------------------', inline=False)
        n=0
        for i in standings.afcEast():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)
            
            
        embed1.add_field(name="AFC North - W/L/T", value = '----------------------', inline=False)
        for i in standings.afcNorth():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)


        embed1.add_field(name="AFC South - W/L/T", value = '----------------------', inline=False)
        for i in standings.afcSouth():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)
        
        embed1.add_field(name="AFC West - W/L/T", value = '----------------------', inline=False)
        for i in standings.afcWest():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)
        await message.channel.send(embed=embed1)


### NFC STANDINGS ###

    if message.content.startswith('!nfc'):
        embed1 = discord.Embed(title = 'NFC Regular Season Standings', color=0xA750DE)
        
        embed1.add_field(name="NFC East - W/L/T", value = '----------------------', inline=False)
        n=0
        for i in standings.nfcEast():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)
                        
        embed1.add_field(name="NFC North - W/L/T", value = '----------------------', inline=False)
        for i in standings.nfcNorth():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)

        embed1.add_field(name="NFC South - W/L/T", value = '----------------------', inline=False)
        for i in standings.nfcSouth():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)
        
        embed1.add_field(name="NFC West - W/L/T", value = '----------------------', inline=False)
        for i in standings.nfcWest():
            embed1.add_field(name = ' '.join(i[0]), value=(str(i[1][0])+'-'+str(i[2][0]+'-'+str(i[3][0]))), inline=False)
        await message.channel.send(embed=embed1)


    if message.content.startswith('!stats') or message.content.startswith('!help'):
        embed1 = discord.Embed(title = 'Bot Commands', color=0xA750DE)

        embed1.add_field(name="Passing Stats", value = "!qb", inline=True)
        embed1.add_field(name="Offensive Yards", value = "!yds", inline=True)
        embed1.add_field(name="Defensive Stats", value = "!defense", inline=True)
        embed1.add_field(name="Special Teams Stats", value = "!special", inline=True)
        embed1.add_field(name="AFC Standings", value = "!afc", inline=True)
        embed1.add_field(name="NFC Standings", value = "!nfc", inline=True)

        await message.channel.send(embed=embed1)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)