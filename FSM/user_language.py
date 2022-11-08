from aiogram.types import Message
from aiogram import Router
from FSM.states import UserLanguage
from create_bot import bot
from keyboards.reply.users import command_kb, language_kb
from aiogram.fsm.context import FSMContext
from db.db_api import user_language

language_router = Router()

@language_router.message(UserLanguage.language)
async def get_language(message: Message,state: FSMContext) -> None:
    text = message.text
    if not (text in ["ru"]):
        await bot.send_message(message.from_user.id, "Нет такого варианта ответа. Выберите язык.",reply_markup=language_kb)
        return
    id = message.from_user.id
    user_language(id, text)
    await state.clear()
    await bot.send_message(id,"Язык установлен", reply_markup=command_kb)
