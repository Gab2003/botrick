import discord
import asyncio
import random
import secreto
import re
import aiohttp
import websockets
from datetime import datetime, timedelta

client = discord.Client()
client.get_all_emojis()

ROXO = 0x43168C
VERMELHO = 0xE1313A
AMARELO = 0xFFFF00
AZUL = 0x5CCFDB
VERDE = 0x10DE3D
token = secreto.seu_token()
msg_id = None
msg_user = None
msg_author = None
qntdd = int


def toint(s):
    s = ''.join(re.findall(r'\d+', s))
    if s != '':
        return int(s)
    else:
        s = 101
        return int(s)


@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo')
    print(client.user.name)
    print(client.servers)
    print(client.user.id)
    print('=-=-=Gabriel=-=-=')
    await client.change_presence(game=discord.Game(name="r!ajuda || Estou on em " +str(len(client.servers))+ "servidores!", url='https://twitch.tv/tmpoarr', type=1))


@client.event
async def on_member_join(member):
    # Envia uma mensagem privada de boas vindas com o nome do servidor e mencionando o usuario
    await client.send_message(member, 'Olá' + member.mention + 'Bem vindo ao' + member.server.name + 'Leia as regras no canal #avisos para evitar banimentos!')
    await client.send_message(client.get_channel('412051386956775426'), 'Bem vindo ao server, ' + member.mention)
    # Adiciona o cargo "Membro" ao membro que entrou
    role = discord.utils.find(lambda r: r.name == "Membro", member.server.roles)
    await client.add_roles(member, role)
    
@client.event
async def on_member_ban(user):
    channel = discord.utils.find(lambda c: c.name == 'banimentos', user.server.channels)
    embed = discord.Embed(title='Sinta o martelo!', description='O usuário **@{0.name}** foi banido do servidor!\n\nO martelo deve ter doído :0'.format(user), color=defcolor)
    embed.set_image(url='https://im4.ezgif.com/tmp/ezgif-4-78bb814d9d.gif')
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)

@client.event
async def on_message(message):
    
    if message.content.lower().startswith('r!mutar'):
        cargomod = discord.utils.find(lambda r: r.name == "Moderadores", message.server.roles)
        if message.author.top_role.position >=  cargomod.position:
            member = re.sub('r!mutar ', '', message.content)
            member = discord.utils.find(lambda r: r.mention == member , message.server.members)
            cargomute = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
            await client.add_roles(member, cargomute)
            await client.send_message(message.channel,'{0.mention} foi mutado por : {1.mention}'.format(member, message.author))
        else:
            await client.send_message(message.channel,'**Você não tem permissão para usar esse comando!**  :rage:')

    if message.content.lower().startswith('r!elos'):
        embed1 = discord.Embed(
            title="→Elos diponíveis:",
            color=AMARELO,
            description="•r!bronze → Adiciona o cargo Bronze.\n"
                        "•r!prata → Adiciona o cargo Prata.\n"
                        "•r!ouro → Adiciona o cargo Ouro.\n"
                        "•r!platina → Adiciona o cargo Platina.\n"
                        "•r!diamante → Adiciona o cargo Diamante.\n"
                        "•r!grão-mestre → Adiciona o cargo Grão Mestre.\n")

    if message.content.lower().startswith('r!prefix'):
        await client.send_message(message.channel, "**Olá jogador, o meu prefix é **`r!`**!**   :smile:")

    # adiciona o cargo Bronze
    if message.content.lower().startswith('r!bronze'):
        cargo = discord.utils.find(lambda r: r.name == "Bronze", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Seu elo foi atualizado para Bronze.** :smile:")

    # adiciona o cargo Prata
    if message.content.lower().startswith('r!prata'):
        cargo = discord.utils.find(lambda r: r.name == "Prata", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Seu elo foi atualizado para Prata.** :smile:")

    # adiciona o cargo Ouro
    if message.content.lower().startswith('r!ouro'):
        cargo = discord.utils.find(lambda r: r.name == "Ouro", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Seu elo foi atualizado para Ouro.** :smile:")

    # adiciona o cargo Platina
    if message.content.lower().startswith('r!platina'):
        cargo = discord.utils.find(lambda r: r.name == "Platina", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Seu elo foi atualizado para Platina.** :smile:")

    # adiciona o cargo Diamante
    if message.content.lower().startswith('r!diamante'):
        cargo = discord.utils.find(lambda r: r.name == "Diamante", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Seu elo foi atualizado para Diamante.** :smile:")

    # adiciona o cargo Grão-Mestre
    if message.content.lower().startswith('r!grão-mestre'):
        cargo = discord.utils.find(lambda r: r.name == "Grão-Mestre", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Seu elo foi atualizado para Grão-Mestre.** :smile:")

    # adiciona o cargo Diamante
    if message.content.lower().startswith('r!oi'):
        cargo = discord.utils.find(lambda r: r.name == "FUNDADOR", message.server.roles)
        await client.add_roles(message.author, cargo)
        await client.send_message(message.channel, "**Olá, tudo bem? Meu nome é Rick! ** :smile:")

    if message.content.lower().startswith('r!ping') and not message.author.id == '415640814371340288':
        d = datetime.utcnow() - message.timestamp
        s = d.seconds * 1000 + d.microseconds // 1000
        await client.send_message(message.channel, ':ping_pong: Pong! {}ms'.format(s))

    if message.content.lower().startswith('r!convidar') and not message.author.id == '415640814371340288':
        await client.send_message(message.channel,
                                  'https://discordapp.com/oauth2/authorize?client_id=415640814371340288&scope=bot&permissions=269740126')

    if message.content.lower().startswith('r!sconvidar') and not message.author.id == '415640814371340288':
        await client.send_message(message.channel,
                                  'https://discord.gg/NY9u3qh')


    if message.content.lower().startswith('r!deletar') and not message.author.id == '415640814371340288':
        modrole = discord.utils.find(lambda r: r.name == "Moderadores", message.server.roles)
        if message.author.top_role.position > modrole.position:
            qntdd = message.content.strip('r!deletar ')
            qntdd = toint(qntdd)
            if qntdd <= 100:
                msg_author = message.author.mention
                await client.delete_message(message)
                # await asyncio.sleep(1)
                deleted = await client.purge_from(message.channel, limit=qntdd)
                botmsgdelete = await client.send_message(message.channel,
                                                         ':mega: **Deletei {} mensagens!**'.format(
                                                             len(deleted), qntdd, msg_author))
                await asyncio.sleep(5)
                await client.delete_message(botmsgdelete)

            else:
                botmsgdelete = await client.send_message(message.channel,
                                                         'Utilize o comando digitando ```ri!deletar <numero de 1 a 100>```')
                await asyncio.sleep(10)
                await client.delete_message(message)
                await client.delete_message(botmsgdelete)
        else:
            await client.send_message(message.channel, " **Você não tem permissão para usar esse comando!**  :rage:")
            await client.delete_message(message)

    if message.content.lower().startswith('r!ajuda'):
        embed1 = discord.Embed(
            title="→Comandos:",
            color=AZUL,
            description="•r!ping → Mostra o seu ping(em ms).\n"
                        "•r!deletar → Deleta uma certa quantidade de mensagens.\n"
                        "•r!convidar → Manda o link do Bot.\n"
                        "•r!sconvidar → Manda o link do server do Dono do Bot.\n"
                        "•r!ajuda → Mostra os comandos diponíveis no servidor.\n"
                        "•r!elos → Mostra os elos disponíveis no servidor.\n"
                        "•r!mutar → Muta o usuário mencionado do servidor.\n")



    botmsg = await client.send_message(message.channel, embed=embed1)

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author

msg_id = '415640814371340288'

client.run(token)
