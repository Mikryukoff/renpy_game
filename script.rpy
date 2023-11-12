# Игра начинается здесь:
label start:

    scene bedroom

    show boy at right_pos

    show dad_calm at left_pos

    father 'Привет, малыш!'

    boy 'Привет!'

    mother 'У нас есть для тебя небольшой сюрприз'

    boy 'Какой?'

    # Показываем карандаши
    window hide
    show bg_dark with dissolve
    show pencils_export at show_item with easeintop

    menu:
        'Взять карандаши':
            hide bg_dark
            hide pencils_export
            jump take_pencils

        'Не брать карандаши':
            hide bg_dark
            hide pencils_export
            jump dont_take_pencils

    return

# Берём карандаши
label take_pencils:

    boy 'Охуеть спасибо папаша!'

    return

# Не берём карандаши
label dont_take_pencils:

    'Мальчик решил, что рисовать не для него, стал программистом и теперь живёт на вокзале'
