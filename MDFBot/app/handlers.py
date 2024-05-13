from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Здравствуйте! Добро пожаловать в мир фасадов МДФ!', reply_markup=kb.main)

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите толщину материала', reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали толщину ...')
    await callback.message.answer('Выберите фрезеровку по толщине',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали фасад')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}руб./кв.м')

@router.message(F.text == 'Контакты')
async def catalog(message: Message):
    await message.answer('г. Казань, ул Лукина, 10, ☎️+1234567890, email: vectordraw@mail.ru', reply_markup=kb.main)

@router.message(F.text == 'О нас')
async def catalog(message: Message):
    await message.answer('Наше производство занимаетсяизготовление фасадов из МДФ на протяжении 20 лет', reply_markup=kb.main)

@router.message(F.text == 'О фасадах')
async def catalog(message: Message):
    await message.answer('MDF - middle density fiberboard. Это плита  срездней плотности. МДФ могут быть крашенными, покрытыми пленками ПВХ и шпонированными', reply_markup=kb.main)
