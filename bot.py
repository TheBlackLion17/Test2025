from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your credentials
api_id = 20919286  # Replace with your API ID
api_hash = "57b85f72104db3f08f9795b0410eb556"  # Replace with your API Hash
bot_token = "7630437489:AAHSWkc9CZaln1JurphrbGlhU7GB-AU3xXE"  # Replace with your Bot Token

# Create the bot client
bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Start Command with Buttons
@bot.on_message(filters.command("start"))
def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Say Hello", callback_data="hello")],
        [InlineKeyboardButton("Visit Website", url="https://example.com")],
    ])
    message.reply_text("Welcome! Choose an option below:", reply_markup=buttons)

# Handling Button Clicks
@bot.on_callback_query()
def button_click(client, callback_query):
    if callback_query.data == "hello":
        callback_query.message.edit_text("Hello! How can I assist you?")

# Start the bot
bot.run()
