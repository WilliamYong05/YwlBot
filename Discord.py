import random
from discord.ext import commands
import praw 

reddit = praw.Reddit(client_id = "ME_UeUZo2u3AIg",
                     client_secret = "M-kqc9Xa09mv2Gz5nDdRTdiV724s2g",
                     username = "Competitive-Study791",
                     password = "ywlisthebestyt",
                     user_agent = "Ywlpraw",)

keywords = [".rv"]

@client.event
async def on_message(message):
  for i in range(len(keywords)):
    if keywords[i] in message.content:
      for j in range(1):
        await message.channel.send("illegal content")

@client.command()
async def meme(ctx,subred = "memes"):
  subreddit = reddit.subreddit(subred)
  all_subs = []

  top = subreddit.top(limit = 50)

  for submission in top:
    all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url) 
    
    await ctx.send(embed= em)

client.run('ODUxNzY2MDk5NDQ2OTg4ODEx.YL9C_w.GKmNqVSZjDMOjSlVljLqSGd0RFc')

