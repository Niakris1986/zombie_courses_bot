import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from src.config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список курсов (буквы латинского алфавита)
courses = [chr(i) for i in range(65, 91)]  # A-Z

def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение и показывает меню курсов."""
    try:
        keyboard = []
        for i in range(0, len(courses), 2):
            row = []
            row.append(InlineKeyboardButton(courses[i], callback_data=courses[i]))
            if i + 1 < len(courses):
                row.append(InlineKeyboardButton(courses[i + 1], callback_data=courses[i + 1]))
            keyboard.append(row)

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            'Привет! Я бот для выбора курсов. Выберите курс из меню ниже:',
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте позже.")

def button_callback(update: Update, context: CallbackContext) -> None:
    """Обрабатывает нажатие на кнопки."""
    try:
        query = update.callback_query
        query.answer()
        selected_course = query.data
        query.edit_message_text(f"Вы выбрали курс {selected_course}")
    except Exception as e:
        logger.error(f"Error in button callback: {e}")
        query.edit_message_text("Произошла ошибка. Пожалуйста, попробуйте позже.")

def error_handler(update: Update, context: CallbackContext) -> None:
    """Обработчик ошибок."""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        update.effective_message.reply_text(
            "Произошла ошибка при обработке запроса. Пожалуйста, попробуйте позже."
        )

def main() -> None:
    """Запускает бота."""
    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CallbackQueryHandler(button_callback))
        dispatcher.add_error_handler(error_handler)

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == '__main__':
    main() 