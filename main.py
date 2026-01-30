import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
from discord.ui import Button, View

# configurações iniciais
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# classes de view

class Produto1View(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Comprar", style=discord.ButtonStyle.success)
    async def comprar_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Clique aqui para realizar a sua compra: [Link de Compra](https://mercadopago.com/produto1)",
            ephemeral=True
        )

class CloseTicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Fechar Ticket", style=discord.ButtonStyle.danger, emoji="🔒")
    async def close_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Este canal será excluído em 5 segundos...", ephemeral=False)
        await asyncio.sleep(5)
        await interaction.channel.delete()

class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.success)
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True)
        }

        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{user.name}",
            overwrites=overwrites,
            topic=f"Suporte para {user.name}"
        )

        embed_ticket = discord.Embed(
            title="Atendimento Iniciado",
            description=f"Olá {user.mention}, relate o seu problema abaixo.\nPara encerrar o atendimento, clique no botão abaixo.",
            color=discord.Color.blue()
        )
        
        view_fechar = CloseTicketView()
        await ticket_channel.send(embed=embed_ticket, view=view_fechar)

        await interaction.response.send_message(f"Seu ticket foi criado! Acesse aqui: {ticket_channel.mention}", ephemeral=True)

# comandos

@bot.event
async def on_ready():
    print(f'Bot conectado com sucesso como: {bot.user}')

@bot.command(name='produto1')
async def produto1(ctx):
    embed = discord.Embed(
        title='Curso Python - COMPLETO!',
        description='Neste curso você vai aprender tudo o que precisa para sair do absoluto ZERO e se tornar um programador Python de SUCESSO!',
        color=discord.Color.purple()
    )
    embed.set_image(url="https://media.discordapp.net/attachments/1466625550427885792/1466625607415758940/banner.png?ex=697d6d09&is=697c1b89&hm=1efc485fa06eb1a320aa474c6a626adb0f03e5f65535d311324526c4bd1bc752&=&format=webp&quality=lossless")
    embed.set_footer(text='Todos os direitos reservados.')

    view_produto = Produto1View()
    await ctx.send(embed=embed, view=view_produto)

@bot.command(name='ticket')
async def ticket(ctx):
    embed = discord.Embed(
        title='Suporte - Ticket de Usuário',
        description='Clique no botão para abrir um ticket!',
        color=discord.Color.purple()
    )
    embed.set_footer(text='© Kaio Sumikawa - Suporte')

    minha_view = TicketView() 
    await ctx.send(embed=embed, view=minha_view)

bot.run(TOKEN)