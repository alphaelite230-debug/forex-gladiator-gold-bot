from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Token and Channel User for later use
TOKEN = '8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k'
CHANNEL_USER = "@ForexGladiator"

# Language Buttons
def language_buttons():
    keyboard = [
        [InlineKeyboardButton("العربية", callback_data='arabic')],
        [InlineKeyboardButton("English", callback_data='english')],
    ]
    return InlineKeyboardMarkup(keyboard)

# Start Command Handler
async def start(update: Update, context):
    chat_id = update.message.chat_id

    # Send the welcome message with language options
    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\n"
        "اهلا بك في بوت فوركس جلادياتور\n"
        "اختر اللغة / Choose language 👇", 
        reply_markup=language_buttons()
    )

# Language Selection Handler
async def button(update: Update, context):
    query = update.callback_query
    choice = query.data

    if choice == "arabic":
        text = "اهلا بك في بوت فوركس جلادياتور باللغة العربية."
    elif choice == "english":
        text = "Welcome to the Forex Gladiator bot in English."
    
    # Send message based on user language choice
    await query.answer()
    await query.edit_message_text(text=text)

# Helper Function for Job Queue (if needed)
async def send_daily(update: Update, context):
    # You can replace this with a message to be sent daily
    await context.bot.send_message(chat_id=update.effective_chat.id, text="هذا رسالة يومية")

# Main function to start the bot
async def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    # Start polling (keep bot running)
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
