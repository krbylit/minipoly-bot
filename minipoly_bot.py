import os
import discord
from discord.ext import commands
import requests
import json
import random
from replit import db
from RealEstateGame import *
# from dotenv import load_dotenv

# DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# secret_token = os.environ["andys_bot_token"]  # token for bot
client = discord.Client()
bot = commands.Bot(command_prefix="$")
game = RealEstateGame()
rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250,
		 250, 250, 300, 300, 300, 350, 350, 350]

bot.run('')

# https://betterprogramming.pub/how-to-make-discord-bot-commands-in-python-2cae39cbfd55


@client.event
async def on_ready():
	"""Greeting message."""
	print(
		"Hello, I am {0.user}. I can run a game of Minipoly for 2-4 players. Just "
		"message '$help' to see a list of commands or '$help [command]' for "
		"detailed command information.".format(client)
	)


@bot.command(
	help="$help long docstring for when called on command",
	brief="brief $help desc for general calling when listing all commands",
	name="start",  # optional shorter command call, prefix w/ $ in chat to execute
)
async def play_minipoly(ctx):
	"""Creates a Minipoly game."""
	game.create_spaces(50, rents)


@bot.command(
	help="$help long docstring for when called on command",
	brief="brief $help desc for general calling when listing all commands",
	name="play",  # optional shorter command call, prefix w/ $ in chat to execute
)
async def add_player(ctx, message):
	"""Creates a Minipoly game."""
	player = message.author
	game.create_player(f"{player}", 1000)


@bot.command(
	help="$help long docstring for when called on command",
	brief="brief $help desc for general calling when listing all commands",
	name="roll",  # optional shorter command call, prefix w/ $ in chat to execute
)
async def roll(ctx, message):
	"""Creates a Minipoly game."""
	player = message.author
	die_roll = random.randint(1, 6)
	await message.channel.send(f"{player} rolled a {die_roll}!")


@client.event
async def on_message(message):
	"""Defines interactions with the event of any message being sent."""
	msg = message.content

	if message.author == client.user:
		# if client.user.id != message.author.id: # another implementation
		"""If message sender is bot, do nothing."""
		return

	if msg.startswith("$help"):
		"""List bot commands."""
		await message.channel.send("")

	if msg.startswith("$play"):
		"""Creates a Minipoly game."""
		game.create_spaces(50, rents)

	if game is not None:
		if msg.startswith("$add_player2"):
			"""Creates two players."""
			game.create_player("Player1", 1000)
			game.create_player("Player2", 1000)
		if msg.startswith("$add_player3"):
			"""Creates three players."""
			game.create_player("Player1", 1000)
			game.create_player("Player2", 1000)
			game.create_player("Player3", 1000)
		if msg.startswith("$add_player4"):
			"""Creates four players."""
			game.create_player("Player1", 1000)
			game.create_player("Player2", 1000)
			game.create_player("Player3", 1000)
			game.create_player("Player4", 1000)



# client.run(secret_token)

#
# game = RealEstateGame()
#
# rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350, 350, 350]
# game.create_spaces(50, rents)
#
# game.create_player("Player 1", 1000)
# game.create_player("Player 2", 1000)
# game.create_player("Player 3", 1000)
#
# while game.check_game_over() == '':
# 	roll = random.randint(1, 6)
# 	game.move_player("Player 1", roll)
# 	game.space_info('Player 1')
# 	game.buy_space("Player 1")
# 	print('Player 1: ' + str(game.get_player_account_balance("Player 1")))
#
# 	roll = random.randint(1, 6)
# 	game.move_player("Player 2", roll)
# 	game.space_info('Player 2')
# 	# game.buy_space("Player 2")
# 	print('Player 2: ' + str(game.get_player_account_balance("Player 2")))
#
# 	roll = random.randint(1, 6)
# 	game.move_player("Player 3", roll)
# 	game.space_info('Player 3')
# 	# game.buy_space("Player 3")
# 	print('Player 3: ' + str(game.get_player_account_balance("Player 3")))
#
# 	game.check_game_over()
#
# # spaces = game.get_spaces()
# # player = game.get_players()['Player 1']
# # spaces['Space_6'].set_owner(player)
# # game.move_player("Player 1", 6)
# # game.buy_space("Player 1")
# # game.move_player("Player 2", 6)
# #
# # print(game.get_player_account_balance("Player 1"))
# # print(game.get_player_account_balance("Player 2"))
# #
# # player1 = game.get_players()['Player 1']
# # player2 = game.get_players()['Player 2']
# # player1.set_status()
# # player2.set_status()
# print(game.check_game_over())
