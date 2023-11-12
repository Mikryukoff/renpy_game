# Определение персонажей игры.
define boy = Character('Мальчик', color="#c8ffc8")
define father = Character('Папа', color='#ff80ff')
define mother = Character('Мама', color='00ffff')

# Координаты расположения спрайтов
init:
    $ show_item = Position(xalign=0.5, yalign=0.5)
    $ right_pos = Position(xalign=0.8, yalign=1)
    $ left_pos = Position(xalign=0.3, yalign=1)
