# Игра начинается здесь:
label start:

    scene bedroom
    show g_boy at right_pos

    '*Стук в дверь*'

    g_boy @ curious 'Мама, папа, вы вернулись?'

    show g_dad smile at left_pos1
    show g_mom at left_pos2
    with easeinleft
    
    g_mom @ talk 'Я и сама в это не верю, день выдался ужасно тяжелым! Еще и выходные оказались забиты...'

    # Диалоговое окно
    menu:
        'Что случилось? Мы же хотели на выходных вместе погулять в парке, там уточки…':
            jump asking_what_happened
        'Ничего страшного, раздевайтесь поскорее, будем обедать!':
            jump dont_asking

    return

# Не спрашиваем, что случилось
label dont_asking:
    
    g_dad @ smile_talk 'Погоди-ка, не только же плохие новости нам домой приносить. Лови!'

    jump show_pencils
    
    return

# Спрашиваем, что случилось
label asking_what_happened:
    
    g_mom @ talk 'Извини, коллега на работе серьезно заболела, придется выйти за неё'

    g_dad @ talk 'Но мы обязательно найдем время и погуляем все вместе. Не расстраивайся!'

    g_mom @ talk 'Зато, смотри-ка, что у нас есть!'

    g_dad @ smile_talk 'Лови!'

    jump show_pencils

    return

# Дарим карандаши
label show_pencils:

    window hide
    show bg_dark with dissolve
    show pencils_export at show_item with easeintop

    menu:
        'Поймать карандаши':
            hide bg_dark
            hide pencils_export
            jump after_gift

        'Уронить карандаши':
            hide bg_dark
            hide pencils_export
            jump drop_pencils

    return

# Роняем карандаши
label drop_pencils:

    g_dad @ smile_talk 'Ну вот, надо бы нам с тобой потренироваться, в следующий раз на прогулку возьмём мячик!'

    jump after_gift

    return

# Продолжение после подарка
label after_gift:

    show g_dad smile_gift at left_pos1

    g_boy @ happy 'Вау! Откуда?! Они такие классные!'

    g_mom @ talk 'Тебе подарок от нас с папой, знаем же, как ты любишь рисовать'

    g_dad @ smile_gift_talk 'Уж не знаю в кого ты так хорошо рисуешь, но раз так — талант нужно развивать!' 

    g_boy @ talk 'Здорово! Спасибо вам огромное, сейчас же их опробую!'

    g_mom @ talk 'Сначала пообедаем, а потом за дело!'

    g_boy @ happy 'Конечно! Хорошо! Бегу мыть руки!'

    return

