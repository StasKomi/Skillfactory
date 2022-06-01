field = [[' ', ' ', ' '] for i in range(3)]


def show_field():
    print(f'  | 0 | 1 | 2 |')
    print('--------------- ')
    for i in range(3):
        print(f'{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |')
        print('--------------- ')


def ask():
    sp = input('Ваш ход:').split()
    if len(sp) != 2:
        print('Необходимо ввести 2 координаты. Попробуйте еще раз')
        ask()
    x, y = sp
    if not(x.isdigit()) or not(y.isdigit()):
        print('Введены не числа. Попробуйте еще раз')
        ask()
    x, y = int(x), int(y)
    if x < 0 or x > 2 or y < 0 or y > 2:
        print('Ваш ход вне диапазона. Попробуйте ещё раз')
        ask()
    if field[x][y] != ' ':
        print('Клетка занята. Попробуйте еще раз')
        ask()
    else:
        return x, y


def win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for comb in win_comb:
        sp = []
        for s in comb:
            sp.append(field[s[0]][s[1]])
        if sp == ['X', 'X', 'X']:
            print('Выиграили крестики')
            return True
        if sp == ['0', '0', '0']:
            print('Выиграли нолики')
            return True
    return False


def game():
    print('Добро пожаловать в "Крестики - нолики"!')
    move = 0
    while True:
        move += 1
        if move % 2 == 1:
            print('Ходит крестик')
        else:
            print('Ходит нолик')
        x, y = ask()
        if move % 2 == 1:
            field[x][y] = 'X'
        else:
            field[x][y] = '0'
        show_field()
        if win():
            continue_game()
        if move == 9:
            print('Ничья')
            break
    continue_game()


def continue_game():
    while True:
        ans = input('Сыграем ещё раз? (да/нет)')
        if ans.lower() not in ['да', 'нет']:
            print('Повторите ответ')
            continue_game()
        if ans.lower() == 'да':
            print('Отлично!')
            game()
        else:
            print('Увидимся в следующий раз!')
        break


game()
