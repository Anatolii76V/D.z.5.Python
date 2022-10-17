field = list(range(1, 10))
win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_field():
    print("-" * 13)
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
    print("-" * 13)


def take_input(player_token):
    while True:
        value = input('Куда поставит: ' + player_token + ' ? ')
        if not (value in '123456789'):
            print('Некорректный ввод. Повторите.')
            continue
        value = int(value)
        if str(field[value - 1]) in 'xo':
            print('Эта клетка уже занята')
            continue
        field[value - 1] = player_token
        break


def check_win():
    for each in win:
        if (field[each[0] - 1]) == (field[each[1] - 1]) == (field[each[2] - 1]):
            return field[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            take_input('x')
        else:
            take_input('o')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_field()
                print(winner, "Выиграл!")
                break
        counter += 1
        if counter > 8:
            draw_field()
            print('Нечья!')
            break


main()





