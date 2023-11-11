# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define boy = Character('Мальчик', color="#c8ffc8")
define father = Character('Папа', color='#ff80ff')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show boy 

    show father

    return
