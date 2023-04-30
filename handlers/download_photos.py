import os

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from handlers.main_commands import TEXT_START_PROGRAM
from create_bot import bot
from keyboards import main_choice_hairstyle, main_action, hairstyle_callback, cancel_add_docs, \
    action_callback, other_choice, coloring_choice, repeated_choice, hairstyle_styling_choice, care_choice, \
    finished_works_choice, cancel_add_finished_works

TEXT_HAIRSTYLE = "Выбери тип фотографии, которую будешь добавлять"

dict_service = {
    'men': ['мужская', 2, 'мужскую стрижку'],
    'women': ['женская', 3, 'женскую стрижку'],
    'children': ['детская', 4, 'детскую стрижку'],
    'boost_up': ['boost_up', 201, 'boost up'],
    'interior': ['интерьер', 254, 'предмет интерьера'],
    'tools': ['инструменты', 254, 'инструменты'],
    'care_products': ['средства_ухода', 254, 'средства для ухода'],
    'other_other': ['другое', 254, 'что-то, для чего мы не смогли придумать название'],
    'hairstyle': ['причёска', 62, 'причёску'],
    'styling': ['укладка', 62, 'укладку'],
    'molecular': ['восстановление', 306, 'молекулярное восстановление волос'],
    'cold_botox': ['холодный_ботокс', 306, 'холодный ботокс'],
    'one_color': ['один_цвет', 66, 'окрашивание в один цвет'],
    'flushing_black': ['смывка_с_чёрного', 66, 'смывку с чёрного'],
    'highlighting': ['мелирование', 66, 'мелирование'],
    'ombre': ['омбре', 66, 'омбре'],
    'shatush': ['шатуш', 66, 'шатуш'],
    'air_touch': ['air_touch', 66, 'Air Touch'],
    'balayage': ['балаяж', 66, 'балаяж']
}

dict_complex_service = {
    'finished_works': ['Выберите тип готовой фотографии', finished_works_choice],
    'coloring': ['Какое именно окрашивание вы хотите добавить?', coloring_choice],
    'hairstyle_styling': ['Что именно, причёску или укладку вы хотите добавить?', hairstyle_styling_choice],
    'other': ['Что именно вы хотите добавить?', other_choice],
    'care': ['Какой именно уход мы выбираем?', care_choice]
}


class FMSDownload(StatesGroup):
    main_state = State()
    download = State()


async def cm_start(message: types.Message):
    global TEXT_HAIRSTYLE

    await message.delete()
    await bot.send_message(message.from_user.id, f"Начнём сначала {TEXT_HAIRSTYLE}", reply_markup=main_choice_hairstyle)


async def open_inline_choice_hairstyle(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
    await call.message.delete()
    await FMSDownload.main_state.set()
    async with state.proxy() as data:
        data['can_send_photo'] = False


async def cancel_choice_add_service(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data.split(':')[1] == "cancel_choice_hairstyle":
        await call.message.answer(
            TEXT_START_PROGRAM,
            reply_markup=main_action)
        await state.finish()
    elif callback_data.split(':')[1] == "cancel_add_type_work":
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
    await call.message.delete()


async def cancel_choice_add_docs(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data.split(':')[1] == "cancel_add_docs":
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
    elif callback_data.split(':')[1] == "cancel_add_finished_works":
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=finished_works_choice)
    await FMSDownload.previous()
    await call.message.delete()


async def forward_docs(message: types.Message, state: FSMContext):
    file = message.document
    async with state.proxy() as data:
        thread_id = data['thread_id']
        description = data['description']
    try:
        await bot.send_document(os.getenv('GROUP_ID'), document=file.file_id, message_thread_id=thread_id,
                                caption=description)
    except:
        await bot.send_message(message.from_user.id, "Слишком много фотографий загруженно сразу!")


async def forward_photo(message: types.Message, state: FSMContext):
    photo = message.photo[0].file_id
    async with state.proxy() as data:
        thread_id = data['thread_id']
        description = data['description']
        can_send_photo = data['can_send_photo']
    try:
        if not can_send_photo:
            await message.answer('Вам запрещенно присылать фотографии в сжатом режиме.\n'
                                 'Выдайте разрешение и попробуйте снова.')
        else:
            await bot.send_photo(os.getenv('GROUP_ID'), photo=photo, message_thread_id=thread_id, caption=description)
    except:
        await bot.send_message(message.from_user.id, "Слишком много фотографий загруженно сразу!")


async def choice_add_simple_hairstyle(call: CallbackQuery, state: FSMContext):
    global dict_service

    await call.answer(cache_time=60)

    callback_data = call.data
    name_hairstyle = dict_service[callback_data.split(':')[1]][2]
    thread_id = dict_service[callback_data.split(':')[1]][1]
    description = '#' + dict_service[callback_data.split(':')[1]][0]

    async with state.proxy() as data:
        data['thread_id'] = thread_id
        data['description'] = description

    await call.message.answer(f"Вы хотите добавить <b>{name_hairstyle}</b>\n"
                              f"Добавьте файлы, а затем нажмите кнопку назад.",
                              reply_markup=cancel_add_docs)
    await call.message.delete()
    await FMSDownload.next()


async def choice_add_hard_hairstyle(call: CallbackQuery, state: FSMContext):
    global dict_complex_service

    await call.answer(cache_time=60)
    callback_data = call.data
    await call.message.answer(dict_complex_service[callback_data.split(':')[1]][0],
                              reply_markup=dict_complex_service[callback_data.split(':')[1]][1])
    await call.message.delete()


async def download_finished_works(call: CallbackQuery, state: FSMContext):
    global dict_service
    callback_data = call.data
    key_for_dict = callback_data.split(':')[1][7::]
    description = '#готово_' + dict_service[key_for_dict][0]
    thread_id = 5
    async with state.proxy() as data:
        data['thread_id'] = thread_id
        data['description'] = description
    await call.message.answer(f"Вы хотите добавить готовую работу по услуге <b>{dict_service[key_for_dict][0]}</b>.\n"
                              f"Добавьте файлы и нажмите кнопку назад.",
                              reply_markup=cancel_add_finished_works, parse_mode="html")
    await call.message.delete()
    await FMSDownload.next()


async def allow_add_photo(call: CallbackQuery, state: FSMContext):
    global TEXT_HAIRSTYLE
    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data.split(':')[1] == "allow_add_photo":
        await call.message.answer("Вы действительно хотите уметь присылать сжатые фотографии?",
                                  reply_markup=repeated_choice)
        await call.message.delete()
    elif callback_data.split(':')[1] == "continue_add_photo":
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_action)
        await call.message.delete()
        async with state.proxy() as data:
            data['can_send_photo'] = True
    elif callback_data.split(':')[1] == "cancel_add_photo":
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_action)
        await call.message.delete()
        async with state.proxy() as data:
            data['can_send_photo'] = False


def register_handlers_docs(dp: Dispatcher):
    dp.register_message_handler(cm_start, Text(equals="Добавление работы в базу", ignore_case=True))
    dp.register_message_handler(forward_docs, content_types=['document'], state=FMSDownload.download)
    dp.register_message_handler(forward_photo, content_types=['photo'], state=FMSDownload.download)
    dp.register_callback_query_handler(open_inline_choice_hairstyle, text_contains="choice_hairstyle")
    dp.register_callback_query_handler(choice_add_simple_hairstyle,
                                       hairstyle_callback.filter(
                                           item_name=["men", "boost_up", "children", "women",
                                                      "one_color", "flushing_black", "ombre", "highlighting", "shatush",
                                                      "air_touch", "balayage", "molecular", "cold_botox", "hairstyle",
                                                      "styling", "interior", "tools", "care_products", "other_other"]),
                                       state=FMSDownload.main_state)
    dp.register_callback_query_handler(download_finished_works,
                                       hairstyle_callback.filter(
                                           item_name=["finish_men", "finish_boost_up", "finish_children",
                                                      "finish_women",
                                                      "finish_highlighting", "finish_one_color",
                                                      "finish_flushing_black", "finish_ombre", "finish_shatush",
                                                      "finish_air_touch", "finish_balayage", "finish_molecular",
                                                      "finish_cold_botox", "finish_hairstyle",
                                                      "finish_styling", "finish_interior", "finish_tools",
                                                      "finish_care_products", "finish_other_other"]),
                                       state=FMSDownload.main_state)
    dp.register_callback_query_handler(choice_add_hard_hairstyle,
                                       hairstyle_callback.filter(
                                           item_name=["hairstyle_styling", "other", "coloring", "care",
                                                      "finished_works"]),
                                       state=FMSDownload.main_state)
    dp.register_callback_query_handler(allow_add_photo,
                                       action_callback.filter(
                                           action_name=["continue_add_photo", "cancel_add_photo", "allow_add_photo"]))
    dp.register_callback_query_handler(cancel_choice_add_service,
                                       action_callback.filter(
                                           action_name=["cancel_choice_hairstyle", "cancel_add_type_work"]),
                                       state=FMSDownload.main_state)
    dp.register_callback_query_handler(cancel_choice_add_docs,
                                       action_callback.filter(
                                           action_name=["cancel_add_docs", "cancel_add_finished_works"]),
                                       state=FMSDownload.download)
