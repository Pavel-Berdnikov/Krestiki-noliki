# Созздадим глобальную переменную со списком чисел от 1 до 9
board = list(range(1, 10))
# Создадим переменную с выигрышными комбинациями (список кортежей)
win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# Функция для отрисовки игрового поля 3x3
def draw_board():
    print("_____________")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("_____________")


# Функция для взаимодействия игроков с полем, проверяет условия ввода нужного числа от 1 до 9 и занято поле или нет
def take_input(player_token):
    while True:
        value = input("Куда ставим: " + player_token + "? ")
        if not (value in '123456789'):
            print("Ошибочный ввод, повторите попытку.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("Эта клетка уже занята")
            continue
        board[value - 1] = player_token
        break


# Функция проверки выигрышных комбинаций. Возвращает False если нет совпадений.
def check_win():
    for each in win_combo:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False


# Задаем главную функцию
def main():
    counter = 0  # Переменная-счетчик для подсчета количества ходов
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:  # Если ходов больше 3, проверка на выигрышные комбинации
            winner = check_win()
            if winner:   # Объявлем победителя если есть совпадения с выигрышными комбинациями
                draw_board()
                print(winner, "победил!")
                break
        counter += 1
        if counter > 8:  # Если ходов больше и победителя нет, объявление ничьей
            draw_board()
            print("Ничья!")
            break


main()