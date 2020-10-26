import tkn
import scrape
import discord
import standings
import teamLeaders


thumbnails = [
    "http://loodibee.com/wp-content/uploads/nfl-arizona-cardinals-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-atlanta-falcons-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-baltimore-ravens-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-buffalo-bills-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-carolina-panthers-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-chicago-bears-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-cincinnati-bengals-team-logo-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-cleveland-browns-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-dallas-cowboys-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-denver-broncos-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-detroit-lions-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-green-bay-packers-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-houston-texans-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-indianapolis-colts-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-jacksonville-jaguars-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-kansas-city-chiefs-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-oakland-raiders-team-logo-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-los-angeles-chargers-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-los-angeles-rams-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-miami-dolphins-logo-2018-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-minnesota-vikings-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-new-england-patriots-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-new-orleans-saints-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-new-york-giants-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-new-york-jets-team-logo-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-philadelphia-eagles-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-pittsburgh-steelers-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-san-francisco-49ers-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-seattle-seahawks-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-tampa-bay-buccaneers-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/nfl-tennessee-titans-team-logo-2-300x300.png",
    "http://loodibee.com/wp-content/uploads/washington-football-team-2020-logo-300x300.png"
]

nfl = ["http://loodibee.com/wp-content/uploads/nfl-league-logo-300x300.png",
           "http://loodibee.com/wp-content/uploads/nfl-afc-American_Football_Conference_logo-300x300.png",
           "http://loodibee.com/wp-content/uploads/nfl-nfc-National_Football_Conference_logo-300x300.png"]


TOKEN = tkn.tkn

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)


#################### League Leaders ###############################
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
        embed1.set_thumbnail(url=nfl[0])
        await message.channel.send(embed=embed1)
################ ################ ################ ################ ################ ################  
            
################ ################ ################ ################ ################ ################             
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
        embed1.set_thumbnail(url=nfl[0])
        await message.channel.send(embed=embed1)
################ ################ ################ ################ ################ ################ 


################ ################ ################ ################ ################ ################ 
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

        embed1.set_thumbnail(url=nfl[0])
        await message.channel.send(embed=embed1)
################ ################ ################ ################ ################ ################ 

################ ################ ################ ################ ################ ################ 
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
        embed1.set_thumbnail(url=nfl[0])
        await message.channel.send(embed=embed1)
#############################################################################################################

################ ################  AFC STANDINGS ################ ################ 

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
        embed1.set_thumbnail(url=nfl[1])
        await message.channel.send(embed=embed1)
################ ################ ################ ################ ################ ################ 


################ ################ NFC STANDINGS ################ ################ 

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

        embed1.set_thumbnail(url=nfl[2])
        await message.channel.send(embed=embed1)
################ ################ ################ ################ ################ ################ 


################ ################ ################ ################ ################ ################ 
    if message.content.startswith('!stats') or message.content.startswith('!help'):
        embed1 = discord.Embed(title = 'Bot Commands', color=0xA750DE)

        embed1.add_field(name="Passing Stats", value = "!qb", inline=True)
        embed1.add_field(name="Offensive Yards", value = "!yds", inline=True)
        embed1.add_field(name="Defensive Stats", value = "!defense", inline=True)
        embed1.add_field(name="Special Teams Stats", value = "!special", inline=True)
        embed1.add_field(name="AFC Standings", value = "!afc", inline=True)
        embed1.add_field(name="NFC Standings", value = "!nfc", inline=True)
        embed1.add_field(name="Team Leaders", value = "Type an ! and a team abreviation", inline=True)
        
        embed1.set_thumbnail(url=nfl[0])
        await message.channel.send(embed=embed1)
################ ################ ################ ################ ################ ################ 


################ ################ ################ ################ ################ ################ 
    if message.content.startswith('!') and message.content[1:] in teamLeaders.teams:
        teamname = teamLeaders.teamsDict[message.content[1:]]
        embed1 = discord.Embed(title='Team Leaders for the {}'.format(teamname), color=0xA750DE)
        for i in teamLeaders.fetchDB():
            if i[1] == message.content[1:]:
                embed1.add_field(name=i[2], value = (i[7] + ' (' + i[12]) + ')', inline=True)
                embed1.add_field(name=i[3], value = (i[8] + ' (' + i[13]) + ')', inline=True)
                embed1.add_field(name=i[4], value = (i[9] + ' (' + i[14]) + ')', inline=True)
                embed1.add_field(name=i[5], value = (i[10] + ' (' + i[15]) + ')', inline=True)
                embed1.add_field(name=i[6], value = (i[11] + ' (' + i[16]) + ')', inline=True)
        embed1.set_thumbnail(url=thumbnails[teamLeaders.teams.index(message.content[1:])])       
            
        await message.channel.send(embed=embed1)
        
    if message.content.startswith('!update') and (str(message.author) == "10038#4741"):
        await message.channel.send('Updating...')
        scrape.updateDB()
        teamLeaders.updateDB()
        await message.channel.send('Done!')

        
################ ################ ################ ################ ################ ################ 

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)