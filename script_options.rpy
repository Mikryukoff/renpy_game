# Определение персонажей игры.
define boy = Character('Мальчик', color='#c8ffc8', image='boy')
define dad = Character('Папа', color='#ff80ff', image='dad')
define mom = Character('Мама', color='00ffff', image='mom')

# Координаты расположения спрайтов
init:
    $ show_item = Position(xalign=0.5, yalign=0.5)
    $ right_pos = Position(xalign=0.8, yalign=1)
    $ left_pos1 = Position(xalign=0.2, yalign=1.5)
    $ left_pos2 = Position(xalign=0.4, yalign=1.5)
