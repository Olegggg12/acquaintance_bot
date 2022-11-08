from aiogram.filters import Filter
from aiogram.types import Message

class AdminFilter(Filter):
    def __init__(self, id: str|int) -> None:
        self.id = id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id==self.id
