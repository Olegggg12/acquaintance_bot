from aiogram.fsm.state import State, StatesGroup

class SendAllAdmin(StatesGroup):
    message = State()

class UserLanguage(StatesGroup):
    language = State()

class Simp(StatesGroup):
    id = State()
    simp = State()

class UserProfile(StatesGroup):
    age = State()
    gender = State()
    like = State()
    city = State()
    name = State()
    description = State()
    photo = State()
