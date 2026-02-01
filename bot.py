from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

async def start(update: Update, context):
    # Create inline keyboard
    keyboard = [
        [
            InlineKeyboardButton("🇸🇦 العربية", callback_data='ar'),
            InlineKeyboardButton("🇺🇸 English", callback_data='en')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with buttons
    await update.message.reply_text(
        "🥇 Forex Gladiator Gold Bot\n\nاختر اللغة / Choose language 👇",
        reply_markup=reply_markup
    )

# This will handle language selection
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'ar':
        await query.edit_message_text(text="مرحبا بك في بوت الفوركس! 🇸🇦")
    elif query.data == 'en':
        await query.edit_message_text(text="Welcome to the Forex Gladiator Bot! 🇺🇸")

def main():
    # Replace with your bot token
    application = Application.builder().token('8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k').build()

    # Command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Callback handler for button presses
    application.add_handler(CallbackQueryHandler(button))

    # Start polling for updates
    application.run_polling()

if __name__ == "__main__":
    main()
