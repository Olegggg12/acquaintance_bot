from aiogram.types import Message
from aiogram import Router
from FSM.states import Simp
from create_bot import bot
from config import admin_id
from aiogram.fsm.context import FSMContext
from db.db_api import check_profile

simp_router = Router()

@simp_router.message(Simp.simp)
async def simpp(message: Message,state: FSMContext) -> None:
    id = message.from_user.id
    if message.text=="👎":
        await state.clear()
        return
    elif message.text=="👍":
        data = await state.get_data()
        profile = check_profile(id)
        if profile==None:
            bot.send_message(id,"У вас еще нет анкеты.")
            await state.clear()
            return
        await bot.send_photo(int(data["id"]),caption=f"{profile[5]},{profile[1]},{profile[4]}\n{profile[6]}\n\n{message.from_user.username}",photo=profile[7])
        await state.clear()   
    elif message.text=="/report":
        data = await state.get_data()
        await bot.send_message(admin_id,f"Поступила жалоба на пользователя:{data['id']}")
        await bot.send_message(id,f"Жалоба была отправлена.")
        await state.clear()
