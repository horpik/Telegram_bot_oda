from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import hairstyle_callback, action_callback

main_action = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить новые фотографии", callback_data=action_callback.new(
                action_name="choice_hairstyle"
            ))
        ]
    ]
)

main_choice_hairstyle = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Стрижка мужская", callback_data=hairstyle_callback.new(
                item_name="men"
            )),
            InlineKeyboardButton(text="Стрижка женская", callback_data=hairstyle_callback.new(
                item_name="women"
            )),
            InlineKeyboardButton(text="Стрижка дестская", callback_data=hairstyle_callback.new(
                item_name="children"
            ))
        ],
        [
            InlineKeyboardButton(text="Окрашивание", callback_data=hairstyle_callback.new(
                item_name="coloring"
            )),
            InlineKeyboardButton(text="Причёска/укладка", callback_data=hairstyle_callback.new(
                item_name="hairstyle_styling"
            )),
            InlineKeyboardButton(text="Другое", callback_data=hairstyle_callback.new(
                item_name="other"
            ))
        ],
        [
            InlineKeyboardButton(text="Готовые работы", callback_data=hairstyle_callback.new(
                item_name="finished_works"
            )),
            InlineKeyboardButton(text="Уход", callback_data=hairstyle_callback.new(
                item_name="care"
            )),
            InlineKeyboardButton(text="Boost Up", callback_data=hairstyle_callback.new(
                item_name="boost_up"
            ))
        ],
        [
            InlineKeyboardButton(text="Разрешить добавлять обычные фото", callback_data=action_callback.new(
                action_name="allow_add_photo"
            ))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_choice_hairstyle"
            ))
        ]
    ]
)

coloring_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Один цвет", callback_data=hairstyle_callback.new(
                item_name="one_color"
            )),
            InlineKeyboardButton(text="Смывка с чёрного", callback_data=hairstyle_callback.new(
                item_name="flushing_black"
            )),
            InlineKeyboardButton(text="Мелирование", callback_data=hairstyle_callback.new(
                item_name="highlighting"
            ))
        ],
        [
            InlineKeyboardButton(text="Омбре", callback_data=hairstyle_callback.new(
                item_name="ombre"
            )),
            InlineKeyboardButton(text="Шатуш", callback_data=hairstyle_callback.new(
                item_name="shatush"
            ))
        ],
        [
            InlineKeyboardButton(text="Air Touch", callback_data=hairstyle_callback.new(
                item_name="air_touch"
            )),
            InlineKeyboardButton(text="Балаяж", callback_data=hairstyle_callback.new(
                item_name="balayage"
            ))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_add_docs"
            ))
        ]
    ]
)
care_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Молекулярное восст. волос", callback_data=hairstyle_callback.new(
                item_name="molecular"
            )),
            InlineKeyboardButton(text="Холодный ботокс", callback_data=hairstyle_callback.new(
                item_name="cold_botox"
            ))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_add_docs"
            ))
        ]
    ]
)

hairstyle_styling_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Причёска", callback_data=hairstyle_callback.new(
                item_name="hairstyle"
            )),
            InlineKeyboardButton(text="Укладка", callback_data=hairstyle_callback.new(
                item_name="styling"
            ))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_add_docs"
            ))
        ]
    ]
)
other_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Предмет интерьера", callback_data=hairstyle_callback.new(
                item_name="interior"
            )),
            InlineKeyboardButton(text="Инструменты", callback_data=hairstyle_callback.new(
                item_name="tools"
            ))
        ],
        [
            InlineKeyboardButton(text="Уход", callback_data=hairstyle_callback.new(
                item_name="care_products"
            )),
            InlineKeyboardButton(text="Другое", callback_data=hairstyle_callback.new(
                item_name="other_other"
            ))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_add_docs"
            ))
        ]
    ]
)
cancel_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_add_docs"
            ))
        ]
    ]
)

repeated_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data=action_callback.new(
                action_name="continue_add_photo"
            )),
            InlineKeyboardButton(text="Нет", callback_data=action_callback.new(
                action_name="cancel_add_photo"
            ))
        ]
    ]
)

finished_works_choice = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="Стрижка мужская", callback_data=hairstyle_callback.new(
                item_name="finish_men"
            )),
            InlineKeyboardButton(text="Стрижка женская", callback_data=hairstyle_callback.new(
                item_name="finish_women"
            )),
            InlineKeyboardButton(text="Стрижка дестская", callback_data=hairstyle_callback.new(
                item_name="finish_children"
            ))
        ],
        [
            InlineKeyboardButton(text="Boost Up", callback_data=hairstyle_callback.new(
                item_name="finish_boost_up"
            ))
        ],
        [
            InlineKeyboardButton(text="Один цвет", callback_data=hairstyle_callback.new(
                item_name="finish_one_color"
            )),
            InlineKeyboardButton(text="Смывка с чёрного", callback_data=hairstyle_callback.new(
                item_name="finish_flushing_black"
            )),
            InlineKeyboardButton(text="Мелирование", callback_data=hairstyle_callback.new(
                item_name="finish_highlighting"
            ))
        ],
        [
            InlineKeyboardButton(text="Омбре", callback_data=hairstyle_callback.new(
                item_name="finish_ombre"
            )),
            InlineKeyboardButton(text="Шатуш", callback_data=hairstyle_callback.new(
                item_name="finish_shatush"
            ))
        ],
        [
            InlineKeyboardButton(text="Air Touch", callback_data=hairstyle_callback.new(
                item_name="finish_air_touch"
            )),
            InlineKeyboardButton(text="Балаяж", callback_data=hairstyle_callback.new(
                item_name="finish_balayage"
            ))
        ],
        [
            InlineKeyboardButton(text="Молекулярное восст. волос", callback_data=hairstyle_callback.new(
                item_name="finish_molecular"
            )),
            InlineKeyboardButton(text="Холодный ботокс", callback_data=hairstyle_callback.new(
                item_name="finish_cold_botox"
            ))
        ],
        [
            InlineKeyboardButton(text="Предмет интерьера", callback_data=hairstyle_callback.new(
                item_name="finish_interior"
            )),
            InlineKeyboardButton(text="Инструменты", callback_data=hairstyle_callback.new(
                item_name="finish_tools"
            ))
        ],
        [
            InlineKeyboardButton(text="Уход", callback_data=hairstyle_callback.new(
                item_name="finish_care_products"
            )),
            InlineKeyboardButton(text="Другое", callback_data=hairstyle_callback.new(
                item_name="finish_other_other"
            ))
        ],
        [
            InlineKeyboardButton(text="Причёска", callback_data=hairstyle_callback.new(
                item_name="finish_hairstyle"
            )),
            InlineKeyboardButton(text="Укладка", callback_data=hairstyle_callback.new(
                item_name="finish_styling"
            ))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=action_callback.new(
                action_name="cancel_add_docs"
            ))
        ]

    ]
)
