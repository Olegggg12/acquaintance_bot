from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from create_bot import bot,dp
from myfilters.filters import AdminFilter
from config import admin_id
from keyboards.inline.admin import inline_admin_kb
from FSM.states import SendAllAdmin


@dp.message(AdminFilter(admin_id), Command(commands=["admin"]))
async def admin(message : Message):
    id = message.from_user.id
    await bot.send_message(id,"Админ панель:", reply_markup=inline_admin_kb)

@dp.callback_query(lambda c: c.data=="send_all_button")
async def send_all(call: CallbackQuery, state: FSMContext):
    await call.answer("Введите ваше сообщение:")
    await state.set_state(SendAllAdmin.message)
