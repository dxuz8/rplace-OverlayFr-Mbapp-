import discord

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Discord
bot_token = 'YOUR_BOT_TOKEN'

# Créez un client Discord
client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')

@client.event
async def on_message(message):
    # Vérifie si le message est envoyé par le bot lui-même pour éviter les boucles
    if message.author == client.user:
        return
      if message.content.lower() == 'r!link':
        # Envoie le lien spécifié
        link = 'https://github.com/dxuz8/rplace-OverlayFr-Mbapp-/blob/main/overlayfr.json'
        await message.channel.send(link)

        # Envoie un message supplémentaire
        additional_message = 'Overlay for mbappé for R/Place are sent to you'
        await message.channel.send(additional_message)

# Connexion au serveur Discord avec le token du bot
client.run(bot_token)
