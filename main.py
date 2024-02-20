# main.py
import discord
from bot_mantik import gen_pass
from ayarlar import ayarlar
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import *
from new_member import *


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
ayricaliklar = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
ayricaliklar.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
istemci = discord.Client(intents=ayricaliklar)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return  
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$bye'):
        await message.channel.send("sakkın gitme")
    elif message.content.startswith('$neden'):
        await message.channel.send("senle vakit geçirmek çok eğlenceliydi ")
    elif message.content.startswith('$generate_password'):

        # Kullanıcıdan PASSWORD uzunluğunu al
        pass_length = int(message.content.split()[1]) if len(message.content.split()) > 1 else 10

        # gen_pass fonksiyonunu kullanarak PASSWORD CRTEATE EDİYOR
        generated_password = gen_pass(pass_length)

        # Oluşturulan şifreyi ekrana ve USER send ediyor
        await message.channel.send(f"Generated Password: {generated_password}")
    else:
        await message.channel.send(message.content)

client.run("MTIwNTkxOTE0NjQ0NjE1OTk5NA.Gw2W1C.XaHpdJxHB1or_eD2MOdeK28dcTOedv6wFOKhi8")
