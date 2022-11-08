from aiogram.types import Message
from aiogram import Router
from FSM.states import UserProfile
from create_bot import bot
from keyboards.reply.users import gender_kb, like_kb
from aiogram.fsm.context import FSMContext
from db.db_api import user_profile

profile_router = Router()

@profile_router.message(UserProfile.age)
async def get_age(message: Message,state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserProfile.gender)
    await bot.send_message(message.from_user.id, "Какого вы пола?", reply_markup=gender_kb)

@profile_router.message(UserProfile.gender)
async def get_gender(message: Message,state: FSMContext) -> None:
    text = message.text
    if not (text in ["Парень", "Девушка"]):
        await bot.send_message(message.from_user.id, "Нет такого варианта ответа. Выберите пол.")
        return
    await state.update_data(gender=message.text)
    await state.set_state(UserProfile.like)
    await bot.send_message(message.from_user.id, "Кто вам нравится?", reply_markup=like_kb)

@profile_router.message(UserProfile.like)
async def get_like(message: Message,state: FSMContext) -> None:
    text = message.text
    if not (text in ["Парни", "Девушки"]):
        await bot.send_message(message.from_user.id, "Нет такого варианта ответа. Кто вам нравится?")
        return
    await state.update_data(like=message.text)
    await state.set_state(UserProfile.city)
    await bot.send_message(message.from_user.id, "Из какого вы города?\n(Вводи город правильно, без лишних пробелов с большой буквы. Например: Москва)",reply_markup=None)

@profile_router.message(UserProfile.city)
async def get_city(message: Message,state: FSMContext) -> None:
    await state.update_data(city=message.text)
    await state.set_state(UserProfile.name)
    await bot.send_message(message.from_user.id, "Как вас зовут?")

@profile_router.message(UserProfile.name)
async def get_name(message: Message,state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(UserProfile.description)
    await bot.send_message(message.from_user.id, "Добавьте краткое описание")

@profile_router.message(UserProfile.description)
async def get_description(message: Message, state: FSMContext) -> None:
    await state.update_data(description=message.text)
    await state.set_state(UserProfile.photo)
    await bot.send_message(message.from_user.id, "Добавьте фото")

@profile_router.message(UserProfile.photo)
async def get_photo(message: Message, state: FSMContext) -> None:
    id = message.from_user.id
    await state.update_data(photo=message.photo[0].file_id)
    await bot.send_message(id, "Ваша анкета:")
    data = await state.get_data()
    await bot.send_photo(id,caption=f"{data['name']},{data['city']},{data['age']}\n{data['description']}",photo=data['photo'])
    user_profile(id,data["age"],data["gender"],data["like"],data["city"],data["name"],data["description"],data["photo"])
    await state.clear()
