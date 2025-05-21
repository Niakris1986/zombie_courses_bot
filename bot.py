import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
COURSES = [chr(i) for i in range(65, 91)]  

def start(update: Update, context: CallbackContext):
    """Send a greeting message when the command /start is issued."""
    try:
        keyboard = []
        for course in COURSES:
            keyboard.append([InlineKeyboardButton(f"Course {course}", callback_data=f"course_{course}")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "👋 Привет! Я бот для выбора курсов.\n"
            "Выберите интересующий вас курс из меню ниже:",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте позже.")

def button_callback(update: Update, context: CallbackContext):
    try:
        query = update.callback_query
        query.answer()
        if query.data.startswith("course_"):
            course = query.data.split("_")[1]
            query.edit_message_text(
                f"Вы выбрали курс {course}!\n"
                "В будущем здесь будет подробная информация о курсе."
            )
    except Exception as e:
        logger.error(f"Error in button callback: {e}")
        if update.callback_query:
            update.callback_query.edit_message_text("Произошла ошибка. Пожалуйста, попробуйте позже.")

def error_handler(update: Update, context: CallbackContext):
    """Log the error and send a message to the user."""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        update.effective_message.reply_text("Произошла ошибка. Пожалуйста, попробуйте позже.")

def main():
    updater = Updater('7563305053:AAFT6Cx7wSWF-Mxn_LWLW9uYtck5lBUL0OQ', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_callback))
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 