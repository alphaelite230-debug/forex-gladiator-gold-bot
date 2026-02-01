import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from telegram.ext import JobQueue
import asyncio

# حط توكن البوت هنا
API_TOKEN = '8547968244:AAG2f_9xEqOTQnpJeKNcp0pcBSSuNJVNN6k'

# إعدادات اللوج
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# كوماند /start
async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info(f"User {user.id} has started the bot.")
    
    # إعداد الكيبورد لاختيار اللغة
    keyboard = [
        [KeyboardButton("🇺🇸 English"), KeyboardButton("🇪🇬 العربية")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    # إرسال رسالة الترحيب وطلب اللغة
    await update.message.reply_text(
        "Welcome to the bot! Choose your language:",
        reply_markup=reply_markup
    )

# معالج اختيار اللغة
async def language_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "🇺🇸 English":
        await update.message.reply_text("You have selected English.")
    elif text == "🇪🇬 العربية":
        await update.message.reply_text("تم اختيار اللغة العربية.")

# كوماند /help
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Help message.')

# معالج الأخطاء
def error_handler(update: object, context: CallbackContext):
    logger.error(f"Update {update} caused error {context.error}")

# دالة الرئيسية لتشغيل البوت
async def main():
    application = Application.builder().token(API_TOKEN).build()

    # إعداد JobQueue (إذا كنت بحاجة لمهام مجدولة)
    job_queue = JobQueue()

    # إضافة المعالجات
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, language_handler))
    
    # بدء البوت
    await application.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
