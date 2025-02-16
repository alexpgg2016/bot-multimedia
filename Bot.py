import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# Reemplaza con tu token de BotFather
TOKEN = "7207056614:AAEBRYP48JpWAISz-9IGOPkHNZpVoDBvhN4"

# ID de los canales donde se publicará
CANAL_1_ID = -1002198641569  # Canal 1
CANAL_2_ID = -1002497630593  # Canal 2

# Configurar el bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Activar logs
logging.basicConfig(level=logging.INFO)

# Comando /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📢 Publicar en Canal 1", callback_data="publicar_canal_1"))
    keyboard.add(InlineKeyboardButton("📢 Publicar en Canal 2", callback_data="publicar_canal_2"))

    await message.reply("📢 ¿En qué canal quieres publicar?", reply_markup=keyboard)

# Manejar selección de canal
@dp.callback_query_handler(lambda c: c.data in ["publicar_canal_1", "publicar_canal_2"])
async def publicar_canal(callback_query: types.CallbackQuery):
    canal_id = CANAL_1_ID if callback_query.data == "publicar_canal_1" else CANAL_2_ID

    media = [
        types.InputMediaPhoto("https://via.placeholder.com/400", caption="Imagen 1"),
        types.InputMediaPhoto("https://via.placeholder.com/500", caption="Imagen 2"),
        types.InputMediaVideo("https://samplelib.com/lib/preview/mp4/sample-5s.mp4", caption="Video ejemplo")
    ]

    await bot.send_media_group(chat_id=canal_id, media=media)
    await bot.send_message(chat_id=canal_id, text="🔹 Publicación enviada.")
    await callback_query.answer("✅ Publicado correctamente")

# Ejecutar el bot
if _name_ == "_main_":
    executor.start_polling(dp, skip_updates=True)
