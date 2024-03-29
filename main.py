import discord
import music_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
file_path = 'APIKEY.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    args = message.content.split(" ")
    command = args.pop(0)
    
    if command == '.top10':
        artist = " ".join(args)
        try:
            await top_tracks(message.channel, artist)
        except Exception as e:
            await message.channel.send("That artist cannot be found.")
    
    if command == '.related':
        artist = " ".join(args)
        try:
            await related(message.channel, artist)
        except Exception as e:
            await message.channel.send("That artist cannot be found.")

async def top_tracks(ctx, artist):
    tracks = music_commands.getTrack(artist)
    embed=discord.Embed(title="Top 10 Tracks", color=0xa30000)
    embed.add_field(name=music_commands.getArtist(artist), value=tracks, inline=False)
    await ctx.send(embed=embed)

async def related(ctx, artist):
    artists = music_commands.getRelatedArtists(artist)
    embed=discord.Embed(title="Related Artists", color=0xa30000)
    embed.add_field(name=music_commands.getArtist(artist), value=artists, inline=False)
    await ctx.send(embed=embed)
    

client.run(file_content)