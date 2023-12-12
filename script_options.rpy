# Определение персонажей игры.
define g_boy = Character('Мальчик', color='#c8ffc8', image='g_boy')
define g_dad = Character('Папа', color='#ff80ff', image='g_dad')
define g_mother = Character('Мама', color='00ffff', image='g_mother')

# Координаты расположения спрайтов
init:
    $ show_item = Position(xalign=0.5, yalign=0.5)
    $ right_pos = Position(xalign=0.8, yalign=1.0)
    $ left_pos1 = Position(xalign=0.2, yalign=1.0)
    $ left_pos2 = Position(xalign=0.3, yalign=1.0)

# Переменные 
# Меню выбора истории
define friends = True
define school = True
define parents = True
define painting = True
define story_count = 0
