from aiogram.filters import Command
from FSM.states import UserProfile, UserLanguage, Simp
from db.db_api import check_profile, ankets
from keyboards.reply.users import language_kb, ldr
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from create_bot import bot,dp

@dp.message(Command(commands=["start","change_language"]))
async def start(message : Message, state: FSMContext) -> None:
    id = message.from_user.id
    await bot.send_message(id, "Привет. Выбери язык.",reply_markup=language_kb)
    await state.set_state(UserLanguage.language)

@dp.message(Command(commands=["myprofile"]))
async def myprofile(message: Message) -> None:
    id = message.from_user.id
    profile = check_profile(id)
    if profile==None:
        await bot.send_message(id,"У вас еще нет анкеты.")
        return
    await bot.send_photo(id,caption=f"{profile[5]},{profile[4]},{profile[1]}\n{profile[6]}",photo=profile[7])

@dp.message(Command(commands=["ankets"]))
async def get_ankets(message: Message, state: FSMContext) -> None:
    id = message.from_user.id
    profile = check_profile(id)
    if profile==None:
        await bot.send_message(id,"У вас отсутствует анкета.")
        return
    gender = "Девушка" if profile[3]=="Девушки" else "Парень"
    like = "Девушки" if profile[2]=="Девушка" else "Парни"
    anket = ankets(gender,profile[1],like,id,profile[4])
    if anket==None:
        await bot.send_message(id,"Нет подходящих пользователей")
        return
    await bot.send_photo(id,caption=f"{anket[5]},{anket[4]},{anket[1]}\n{anket[6]}\n\n/ankets",photo=anket[7],reply_markup=ldr)
    await state.set_state(Simp.id)
    await state.update_data(id=anket[0])
    await state.set_state(Simp.simp)

@dp.message(Command(commands=["отмена"]))
async def cancel(_,state: FSMContext) -> None:
    if await state.get_state()==None:
        return
    await state.clear()

@dp.message(Command(commands=["edit_profile"]))
async def edit_profile(message: Message, state: FSMContext) -> None:
    id = message.from_user.id
    await state.set_state(UserProfile.age)
    await bot.send_message(id, "Сколько тебе лет?",reply_markup=None)

