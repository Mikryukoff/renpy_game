﻿# Игра начинается здесь:
label start:

    scene town

    '''Человек — удивительное существо. Каждый из нас вправе распоряжаться своей судьбой, ставить перед собой цели, искать пути их достижения и довольствоваться результатами.'''

    '''Каждый день судьбы людей переплетаются, мы невольно влияем на историю своей жизни, жизни людей вокруг. И лишь нам самим решать, как именно влиять на этот сценарий.''' 

    '''Быть ли в нем главным героем, приносящим добро и свет, или же просто плыть по течению бытия… А может, вам хочется быть злодеем?'''

    '''Эта история про одного маленького мальчика, хотя нет, это история в первую очередь про человека, который всё же сумел повлиять, достичь и воплотить…'''

# Первая сцена в комнате
    scene bedroom

    '*Стук в дверь*'

    show g_boy at right_pos
    with easeinright

    g_boy @ curious 'Мама, папа, вы вернулись?'

    show g_dad smile at left_pos1
    show g_mother at left_pos2
    with easeinleft
    
    g_mother @ talk 'Я и сама в это не верю, день выдался ужасно тяжелым! Еще и выходные оказались забиты...'

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
    
    g_mother @ talk_explain 'Извини, коллега на работе серьезно заболела, придется выйти за неё'

    g_dad @ talk 'Но мы обязательно найдем время и погуляем все вместе. Не расстраивайся!'

    g_mother @ talk 'Зато, смотри-ка, что у нас есть!'

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

    g_mother @ talk_explain 'Тебе подарок от нас с папой, знаем же, как ты любишь рисовать'

    g_dad @ smile_gift_talk 'Уж не знаю в кого ты так хорошо рисуешь, но раз так — талант нужно развивать!' 

    g_boy @ talk 'Здорово! Спасибо вам огромное, сейчас же их опробую!'

    g_mother @ talk 'Сначала пообедаем, а потом за дело!'

    g_boy @ happy 'Конечно! Хорошо! Бегу мыть руки!'

    jump scene_after_lunch

    return

# Сцена после ужина
label scene_after_lunch:

    scene work_zone
    
    g_boy 'Спасибо за ужин! Я буду у себя.'

    menu:
        'Достать карандаши':
            window hide
            show bg_dark with dissolve
            show pencils_export at show_item with easeintop

            g_boy 'Какие же вы красивые, наконец я смогу вас опробовать!'

            hide bg_dark
            hide pencils_export

            $ my_drawing = draw_logic.Draw.main(background='mini_game.png')

    scene bedroom
    show g_boy at right_pos
    show g_mother at left_pos2 with easeinleft

    g_mother @ talk 'Ну что, как успехи, уже попробовал?'

    g_boy @ happy 'Конечно! Смотри как здорово получилось.'

    show work_zone
    show expression my_drawing

    g_mother @ talk 'Ого! Как же здорово у тебя выходит! Этот рисунок так и веет радостью и уютом.' 

    g_mother @ talk_explain 'Не забрасывай своё хобби, я уверена, у тебя талант!'

    hide work_zone
    hide my_drawing

    g_boy @ curious 'Нет конечно, ты что! Я уже решил, хочу стать профессиональным художником, ну или дизайнером.'

    g_boy @ talk 'Вокруг нас всё такое серое, сплошная тоска и скука. Я хочу это исправить!'

    g_mother @ talk_explain 'Да, ты прав, наш город действительно мрачен и уныл, это сказывается и на его жителях.'

    g_boy @ talk 'Вот именно! Я хочу это исправить, хочу чтобы вам с папой жилось уютнее и радостнее!'

    g_mother @ talk 'Ах, какой же ты у нас заботливый!'

    g_mother @ talk 'Делай то, к чему лежит душа! А мы с папой обязательно тебя поддержим!' 

    g_mother @ talk_explain 'Но на сегодня советую закругляться, уже поздно.'

    g_boy @ talk 'Хорошо, спокойной ночи!'

    g_mother @ talk 'Спокойной ночи, сынок!'

    hide g_mother 
    with easeoutleft
    pause(0.5)

    show g_boy at left_pos2 with ease

    g_boy @ talk 'Пора спать.'

    scene bg_dark 

    g_boy 'Что жe... цель поставлена, осталось усердно трудиться и у меня всё получится!'

    g_boy 'Спи (имя гг), тебе предстоит много работы, а пока нужно выспаться...'

    jump slide_show_scene

    return 

# Слайдшоу о том, что произошло
label slide_show_scene:

    scene town

    'Этот день стал точкой невозврата в судьбe нашего главного героя. Он выбрал весьма благородный, но тяжелый путь.'
    'Безусловно (имя гг) ждало множество препятствий, бывало даже возникали мысли, чтобы всё бросить.' 
    'Но поддержка родителей и нескончаемая мотивация дали свои плоды.'

    '(имя гг) рос, а в месте с ним росли и его навыки. Он много трудился, учился, практиковался, при этом не забывая и про «счастливое детство».'

    menu:
        'Послушать о похождениях героя':
            hide bg_dark
            jump storylines

        'Пропустить похождения героя':
            hide bg_dark
            jump urfu_accepted

    return

# Развилки с предысторией
label storylines:
    if school or parents or painting or friends:
        
        scene town

        menu:
            'Школа' if school:
                scene class_room
                'Учеба в школе давалась нашему герою легко, он быстро «втягивался» в новые темы и показывал весьма достойные результаты.' 
                'Это было очень кстати, парню ведь в институт поступать, верно?'
                $ school = False
                jump storylines

            'Друзья' if friends:
                scene lecture_room
                'Общение с ребятами задалось не сразу, (имя гг) был весьма застенчив, а его интересы часто расходились с таковыми у сверстников.'
                'Однако спустя время парню всё же удалось найти компанию, в которой он чувствовал себя более чем комфортно.'
                $ friends = False
                jump storylines

            'Родители' if parents:
                scene future_bedroom
                'Родители поддерживали нашего героя во всем, искренне любили его и старались чаще проводить вместе время, несмотря на их тяжелую работу.'
                $ parents = False
                jump storylines

            'Рисование' if painting:
                scene work_zone
                '(имя гг) активно изучал различные тонкости рисования и дизайна, занимался на онлайн курсах и даже принимал участие в различных художественных конкурсах.' 
                'Желание мальчика связать свою жизнь именно с этой сферой из года в год лишь росло. Восхитительная целеустремленность!'
                $ painting = False
                jump storylines
    else:
        jump urfu_accepted

    return

# Сцена принятия в вуз
label urfu_accepted:

    scene future_bedroom
    show g_dad at left_pos1
    show g_mother at left_pos2

    '*стук в дверь*'

    show g_mc at right_pos with easeinright

    g_mother @ talk 'Ну чего ты так медлишь, говори быстрее, ну как, прошёл или нет?!'

    g_dad '...?!'

    menu:
        'Пошутить':
            jump to_joke
        'Сказать прямо':
            jump talk_true

    return

# Пошутить
label to_joke:

    g_mc 'Послушайте, у меня есть 2 новости, хорошая и плохая, с какой мне начать?'

    g_mother @ talk_explain 'Сынок, ты издеваешься? Выкладывай поскорее, мы очень волнуемся!'

    g_mc 'Хорошо, тогда начну с плохой... {w}Мне придется уехать от вас на некоторое время...'

    g_dad @ talk 'Что значит уехать? Куда это ты собрался? А что же с результатами?'

    g_mother @ talk 'Да погоди, (имя гг), а что насчет хорошей новости?'

    g_mc 'Я прошёл!!!'
    
    g_mother @ talk_explain 'Я так и знала! Шутничок ты наш, зачем же так пугать! Я так рада!!!'

    jump boy_accepted

    return

# Говорим правду
label talk_true:

    g_mc 'Мои любимые родители, я с радостью сообщаю вам — я прошёл!!!' 

    g_mother 'Я так и знала! Я так рада!!!'

    jump boy_accepted

    return

# Исход вариантов с принятием в ВУЗ
label boy_accepted:

    g_dad @ smile_gift_talk 'Молодец! Ты просто молодец! Мы ни капли не сомневались в тебе. Как же ты нас обрадовал, сынок!'

    g_mc 'Нужно потихоньку собираться, поезд уже послезавтра.'

    g_mother @ talk_explain 'Конечно, всё соберем, не беспокойся, пойду расскажу всем родственникам какой ты у нас умница!'

    g_dad @ smile_talk 'Не забудь забежать к бабушке, она тоже очень хороших новостей!'

    g_mc 'Да, конечно, пойду обрадую и её!'

    jump student_room

    return

# Комната в общаге
label student_room:

    scene bg_dark
    show g_mc at center

    g_mc 'Ох, эти поезда очень утомляют, но нужно привыкать, теперь частенько кататься туда-сюда...'

    g_mc 'А здесь довольно уютно, рассчитывал на худшее.'

    menu:
        'Позвонить маме':
            jump call_mom
        'Разобрать вещи и лечь спать':
            jump to_sleep

    return

# Звоним маме
label call_mom:

    g_mc 'Ало, мамуль, всё хорошо, я добрался.'

    g_mother 'Отлично, как тебе комната?'

    g_mc 'Вообще не плохо, признаться, думал всё будет куда печальнее.'

    g_mother 'Вот и здорово! Давай поскорее разбирай вещи и ложись, завтра у тебя уж очень насыщенный день, нужно выспаться!'

    g_mc 'Это точно! Да, сейчас этим и займусь. Вы тоже ложитесь отдыхать, завтра вечером расскажу как всё прошло.'

    g_mother 'Хорошо, очень ждём звонка! Доброй ночи, сынок!'

    g_mc 'Cпокойной ночи!'

    jump first_day_in_urfu

    return

# Разбираем вещи и ложимся спать
label to_sleep:

    scene bg_dark

    g_mc 'Фух, это было не сложно, не так уж у меня и много вещей.'

    g_mc 'Звонить уже не буду, спят небось. Утром поболтаем.'

    g_mc '...'

    g_mc 'Надеюсь, всё пройдёт хорошо, как-то неспокойно на душе.'

    g_mc '...'

    g_mc 'Ладно, нужно выспаться, день завтра обещает быть насыщенным...'

    jump first_day_in_urfu

# Первый день в ВУЗе
label first_day_in_urfu:

    scene lecture_room
    show g_mc at right_pos

    jump studying_scenes

    return

# Сцены с учебой
label studying_scenes:

    scene class_room

    'Первый учебный день оказался позади, за ним — неделя, месяц, время уже подходило к первой в жизни (имя гг) сессии.' 
    
    'Но несмотря на успешную учебу, наш герой чувствовал, что что-то в его жизни изменилось. И явно не в лучшую сторону...'

    scene lecture_room

    'Нагрузка на парня возрастала, всё меньше времени у него оставалось для работы над своими проектами.' 

    'А ведь это была его отдушина, дело, в которое он вкладывал самого себя.'

    scene bg_dark

    'Мотивация парня всё активнее стремилась к нулю, ещё и предстоящие экзамены удручали его ситуацию.'

    'Однако всего один воодушевляющий диалог наконец пустил трещины в снежном коме грусти и тоски...'

    return
