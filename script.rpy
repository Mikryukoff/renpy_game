# Игра начинается здесь:
label start:

    scene bedroom

    show boy at right_pos
    show dad at left_pos1
    show mom at left_pos2

    dad @ talk 'Привет, малыш!'

    boy @ talk 'Привет!'

    mom @ talk 'У нас есть для тебя небольшой сюрприз'

    boy @ talk 'Какой?'

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

    show dad happy at left_pos1

    boy happy 'Ого, спасибо!'

    return

# Не берём карандаши
label dont_take_pencils:

    'Мальчик решил, что рисовать не для него, стал программистом и теперь живёт на вокзале'
