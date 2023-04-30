import os

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from create_bot import bot
from handlers.main_commands import TEXT_START_PROGRAM
from keyboards import main_choice_hairstyle, repeated_choice, main_action, hairstyle_callback, cancel_choice, \
    action_callback, other_choice, coloring_choice, hairstyle_styling_choice, care_choice, finished_works_choice

thread_id = 0
can_send_photo = False
description = "кто-то криво скинул файлы)))"

TEXT_HAIRSTYLE = "Выбери тип фотографии, которую будешь добавлять"


dict_service = {
    'men': '#мужская',
    'women': '#женская',
    'children': '#детская',
    'boost_up': '#boost_up',
    'interior': '#интерьер',
    'tools': '#инструменты',
    'care_products': 'средства_ухода',
    'other_other': '#другое',
    'hairstyle': '#причёска',
    'styling': '#укладка',
    'molecular': '#восстановление',
    'cold_botox': '#холодный_ботокс',
    'one_color': '#один_цвет',
    'flushing_black': '#смывка_с_чёрного',
    'highlighting': '#мелирование',
    'ombre': '#омбре',
    'shatush': '#шатуш',
    'air_touch': '#air_touch',
    'balayage': 'балаяж'
}


async def cm_start(message: types.Message):
    global TEXT_HAIRSTYLE

    await message.delete()
    await bot.send_message(message.from_user.id, f"Начнём сначала {TEXT_HAIRSTYLE}", reply_markup=main_choice_hairstyle)


async def forward_docs(message: types.Message):
    global description
    file = message.document
    try:
        await bot.send_document(os.getenv('GROUP_ID'), document=file.file_id, message_thread_id=thread_id,
                                caption=description)
    finally:
        print("Что-то не так")


async def forward_photo(message: types.Message):
    global can_send_photo
    global description

    photo = str(message.photo).split('"')[3]
    if not can_send_photo:
        await message.answer('Вам запрещено присылать фотографии в обычном формате.\n'
                             'Укажите разрешение и попробуйте снова')
    else:
        try:
            await bot.send_photo(os.getenv('GROUP_ID'), photo=photo, message_thread_id=thread_id, caption=description)
        finally:
            print("Что-то не так")


async def allow_add_photo(call: CallbackQuery):
    global can_send_photo
    global TEXT_HAIRSTYLE

    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data.split(':')[1] == "allow_add_photo":
        await call.message.answer("Вы хотите разрешить присылать фотографии в обычном, не сжатом формате?",
                                  reply_markup=repeated_choice)
        await call.message.delete()
    elif callback_data.split(':')[1] == "continue_add_photo":
        can_send_photo = True
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
        await call.message.delete()
    elif callback_data.split(':')[1] == "cancel_add_photo":
        can_send_photo = False
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
        await call.message.delete()


async def cancel_diff_choice(call: CallbackQuery):
    global TEXT_HAIRSTYLE

    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data.split(':')[1] == "cancel_choice_hairstyle":
        await call.message.answer(
            TEXT_START_PROGRAM,
            reply_markup=main_action)
    elif callback_data.split(':')[1] == "cancel_add_docs":
        await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
    await call.message.delete()


async def choice_add_simple_hairstyle(call: CallbackQuery):
    global thread_id
    global description
    global dict_service

    await call.answer(cache_time=60)
    callback_data = call.data
    name_hairstyle = ""
    if callback_data.split(':')[1] == 'men':
        name_hairstyle = "мужскую стрижку"
        description = dict_service['men']
        thread_id = 2
    elif callback_data.split(':')[1] == 'women':
        name_hairstyle = "женскую стрижку"
        description = dict_service['women']
        thread_id = 3
    elif callback_data.split(':')[1] == 'children':
        name_hairstyle = "детскую стрижку"
        description = dict_service['children']
        thread_id = 4
    elif callback_data.split(':')[1] == 'finished_works':
        name_hairstyle = "готовую работу"
        thread_id = 5
        await call.message.answer(f"Выберите тип готовой фотографии",
                                  reply_markup=finished_works_choice)
        await call.message.delete()
        return
    elif callback_data.split(':')[1] == 'boost_up':
        name_hairstyle = "boost up"
        description = dict_service['boost_up']
        thread_id = 201
    await call.message.answer(f"Вы хотите добавить {name_hairstyle}\n"
                              f"Добавьте файлы или нажмите кнопку назад",
                              reply_markup=cancel_choice)
    await call.message.delete()


async def choice_add_hard_hairstyle(call: CallbackQuery):
    global thread_id
    global description
    global dict_service
    name_hairstyle = ""
    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data.split(':')[1] == "coloring":
        await call.message.answer("Какое именно окрашивание вы хотите добавить?", reply_markup=coloring_choice)
        await call.message.delete()
        thread_id = 66
        return
    elif callback_data.split(':')[1] == "hairstyle_styling":
        await call.message.answer("Что именно, причёску или укладку вы хотите добавить?",
                                  reply_markup=hairstyle_styling_choice)
        await call.message.delete()
        thread_id = 62
        return
    elif callback_data.split(':')[1] == "other":
        await call.message.answer("Что именно вы хотите добавить?", reply_markup=other_choice)
        await call.message.delete()
        thread_id = 254
        return
    elif callback_data.split(':')[1] == "care":
        await call.message.answer("Какой именно уход мы выбираем?", reply_markup=care_choice)
        await call.message.delete()
        thread_id = 306
        return
    elif callback_data.split(':')[1] == "interior":
        name_hairstyle = "предмет интерьера"
        description = dict_service['interior']
    elif callback_data.split(':')[1] == "tools":
        name_hairstyle = "инструменты"
        description = dict_service['tools']
    elif callback_data.split(':')[1] == "care_products":
        name_hairstyle = "средства для ухода"
        description = dict_service['care_products']
    elif callback_data.split(':')[1] == "other_other":
        name_hairstyle = "что-то, для чего мы не смогли придумать название"
        description = dict_service['other_other']
    elif callback_data.split(':')[1] == "hairstyle":
        name_hairstyle = "причёску"
        description = dict_service['hairstyle']
    elif callback_data.split(':')[1] == "styling":
        name_hairstyle = "укладку"
        description = dict_service['styling']
    elif callback_data.split(':')[1] == "molecular":
        name_hairstyle = "молекулярное восстановление волос"
        description = dict_service['molecular']
    elif callback_data.split(':')[1] == "cold_botox":
        name_hairstyle = "Холодный ботокс"
        description = dict_service['cold_botox']
    elif callback_data.split(':')[1] == "one_color":
        name_hairstyle = "окрашивание в один цвет"
        description = dict_service['one_color']
    elif callback_data.split(':')[1] == "flushing_black":
        name_hairstyle = "смывку с чёрного"
        description = dict_service['flushing_black']
    elif callback_data.split(':')[1] == "highlighting":
        name_hairstyle = "мелирование"
        description = dict_service['highlighting']
    elif callback_data.split(':')[1] == "ombre":
        name_hairstyle = "омбре"
        description = dict_service['ombre']
    elif callback_data.split(':')[1] == "shatush":
        name_hairstyle = "шатуш"
        description = dict_service['shatush']
    elif callback_data.split(':')[1] == "air_touch":
        name_hairstyle = "Air Touch"
        description = dict_service['air_touch']
    elif callback_data.split(':')[1] == "balayage":
        name_hairstyle = "балаяж"
        description = dict_service['balayage']
    await call.message.answer(f"Вы хотите добавить {name_hairstyle}\n"
                              f"Добавьте файлы или нажмите кнопку назад",
                              reply_markup=cancel_choice)
    await call.message.delete()


async def download_finished_works(call: CallbackQuery):
    global thread_id
    global description
    global dict_service

    callback_data = call.data
    key_for_dict = callback_data.split("_")[1]
    description = dict_service.get(key_for_dict)
    description = "#готово_" + description
    thread_id = 5


def register_handlers_docs(dp: Dispatcher):
    dp.register_message_handler(cm_start, Text(equals="Добавление работы в базу", ignore_case=True))
    dp.register_message_handler(forward_docs, content_types=['document'])
    dp.register_message_handler(forward_photo, content_types=['photo'])
    dp.register_callback_query_handler(choice_add_simple_hairstyle,
                                       hairstyle_callback.filter(
                                           item_name=["men", "finished_works", "boost_up", "children", "women"]))
    dp.register_callback_query_handler(download_finished_works,
                                       hairstyle_callback.filter(
                                           item_name=["finish_men", "finish_boost_up", "finish_children",
                                                      "finish_women",
                                                      "finish_highlighting", "finish_one_color",
                                                      "finish_flushing_black", "finish_ombre", "finish_shatush",
                                                      "finish_air_touch", "finish_balayage", "finish_molecular",
                                                      "finish_cold_botox", "finish_hairstyle",
                                                      "finish_styling", "finish_interior", "finish_tools",
                                                      "finish_care_products", "finish_other_other"]))
    dp.register_callback_query_handler(choice_add_hard_hairstyle,
                                       hairstyle_callback.filter(
                                           item_name=["hairstyle_styling", "other", "coloring", "care",
                                                      "one_color", "flushing_black", "ombre", "highlighting", "shatush",
                                                      "air_touch", "balayage", "molecular", "cold_botox", "hairstyle",
                                                      "styling", "interior", "tools", "care_products", "other_other"]))
    dp.register_callback_query_handler(cancel_diff_choice,
                                       action_callback.filter(
                                           action_name=["cancel_add_docs", "cancel_choice_hairstyle"]))
    dp.register_callback_query_handler(allow_add_photo,
                                       action_callback.filter(
                                           action_name=["continue_add_photo", "cancel_add_photo", "allow_add_photo"]))
