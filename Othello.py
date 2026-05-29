import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 580
SCREEN_TITLE = "Othello"


def draw_game_board():
    for i in range(0, 8):
        for j in range(0, 8):
            disc = Othello.game_board[i][j]
            if disc == 1 or disc == -1:
                arcade.draw_circle_filled(200 + 50 * j, 450 - 50 * i, 18,
                                          arcade.color.BLACK if disc == 1 else arcade.color.WHITE)
    for li in Othello.available_moves:
        for a, b in li:
            if 0 <= a < 8 and 0 <= b < 8:
                arcade.draw_circle_outline(200 + 50 * b, 450 - 50 * a, 18,
                                       arcade.color.BLACK if disc == 2 else arcade.color.BLACK)


def index_finding(x, y):
    temp = y // 50 * 50
    if y - temp <= 24:
        indexes = (temp - 450) // -50
    else:
        indexes = (temp - 400) // -50

    temp = x // 50 * 50
    if x - temp <= 24:
        indexes = indexes, (temp - 200) // 50
    else:
        indexes = indexes, (temp - 150) // 50

    return indexes


def flipping(a, b, x, y, turn):
    # Horizontal
    if a == x:
        for i in range(min(b, y), max(b, y) + 1):
            if i == y: continue
            if turn == 1:
                Othello.game_board[a][i] = 1
                if (a, i) not in Othello.black_discs: Othello.black_discs.append((a, i))
                if (a, i) in Othello.white_disks: Othello.white_disks.remove((a, i))
            else:
                Othello.game_board[a][i] = -1
                if (a, i) not in Othello.white_disks: Othello.white_disks.append((a, i))
                if (a, i) in Othello.black_discs: Othello.black_discs.remove((a, i))

    # Vertical
    elif b == y:
        for i in range(min(a, x), max(a, x) + 1):
            if i == x: continue
            if turn == 1:
                Othello.game_board[i][b] = 1
                if (i, b) not in Othello.black_discs: Othello.black_discs.append((i, b))
                if (i, b) in Othello.white_disks: Othello.white_disks.remove((i, b))
            else:
                Othello.game_board[i][b] = -1
                if (i, b) not in Othello.white_disks: Othello.white_disks.append((i, b))
                if (i, b) in Othello.black_discs: Othello.black_discs.remove((i, b))

    # Diagonal /
    elif (b - y) / (a - x) == -1:
        temp_x = min(a, x)
        temp_y = max(b, y)
        while temp_x <= max(a, x):
            if temp_x == x:
                temp_x, temp_y = temp_x + 1, temp_y - 1
                continue
            if turn == 1:
                Othello.game_board[temp_x][temp_y] = 1
                if (temp_x, temp_y) not in Othello.black_discs: Othello.black_discs.append((temp_x, temp_y))
                if (temp_x, temp_y) in Othello.white_disks: Othello.white_disks.remove((temp_x, temp_y))
            else:
                Othello.game_board[temp_x][temp_y] = -1
                if (temp_x, temp_y) not in Othello.white_disks: Othello.white_disks.append((temp_x, temp_y))
                if (temp_x, temp_y) in Othello.black_discs: Othello.black_discs.remove((temp_x, temp_y))
            temp_x, temp_y = temp_x + 1, temp_y - 1

    # Diagonal \
    elif (b - y) / (a - x) == 1:
        temp_x = min(a, x)
        temp_y = min(b, y)
        while temp_x <= max(a, x):
            if temp_x == x:
                temp_x, temp_y = temp_x + 1, temp_y + 1
                continue
            if turn == 1:
                Othello.game_board[temp_x][temp_y] = 1
                if (temp_x, temp_y) not in Othello.black_discs: Othello.black_discs.append((temp_x, temp_y))
                if (temp_x, temp_y) in Othello.white_disks: Othello.white_disks.remove((temp_x, temp_y))
            else:
                Othello.game_board[temp_x][temp_y] = -1
                if (temp_x, temp_y) not in Othello.white_disks: Othello.white_disks.append((temp_x, temp_y))
                if (temp_x, temp_y) in Othello.black_discs: Othello.black_discs.remove((temp_x, temp_y))
            temp_x, temp_y = temp_x + 1, temp_y + 1


def finding_available_moves(x, y, turn):
    moves = [(x, y)]
    # LEFT
    if y > 0 and Othello.game_board[x][y - 1] == -turn:
        j = y - 1
        while j >= 0 and Othello.game_board[x][j] == -turn:
            j = j - 1
            if j == 0: break
        if Othello.game_board[x][j] == 0: moves.append((x, j))

    # RIGHT
    if y < 7 and Othello.game_board[x][y + 1] == -turn:
        j = y + 1
        while j < 7 and Othello.game_board[x][j] == -turn:
            j = j + 1
            if j == 7: break
        if Othello.game_board[x][j] == 0: moves.append((x, j))

    # TOP
    if x > 0 and Othello.game_board[x - 1][y] == -turn:
        i = x - 1
        while Othello.game_board[i][y] == -turn:
            i = i - 1
            if i == 0: break
        if Othello.game_board[i][y] == 0: moves.append((i, y))

    # DOWN
    if x < 7 and Othello.game_board[x + 1][y] == -turn:
        i = x + 1
        while i <= 7 and Othello.game_board[i][y] == -turn:
            i = i + 1
            if i == 7: break
        if i <= 7 and Othello.game_board[i][y] == 0: moves.append((i, y))

    # TOP LEFT
    if x > 0 and y > 0 and Othello.game_board[x - 1][y - 1] == -turn:
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0 and Othello.game_board[i][j] == -turn:
            i, j = i - 1, j - 1
            if i == 0 or j == 0: break
        if i >= 0 and j >= 0 and Othello.game_board[i][j] == 0: moves.append((i, j))

    # TOP RIGHT
    if x > 0 and y < 7 and Othello.game_board[x - 1][y + 1] == -turn:
        i, j = x - 1, y + 1
        while i >= 0 and j <= 7 and Othello.game_board[i][j] == -turn:
            i, j = i - 1, j + 1
            if i == 0 or j == 7: break
        if i >= 0 and j <= 7 and Othello.game_board[i][j] == 0: moves.append((i, j))

    # BOTTOM LEFT
    if x < 7 and y > 0 and Othello.game_board[x + 1][y - 1] == -turn:
        i, j = x + 1, y - 1
        while i <= 7 and j >= 0 and Othello.game_board[i][j] == -turn:
            i, j = i + 1, j - 1
            if i == 7 or j == 0: break
        if i <= 7 and j >= 0 and Othello.game_board[i][j] == 0: moves.append((i, j))

    # BOTTOM RIGHT
    if x < 7 and y < 7 and Othello.game_board[x + 1][y + 1] == -turn:
        i, j = x + 1, y + 1
        while i <= 7 and j <= 7 and Othello.game_board[i][j] == -turn:
            i, j = i + 1, j + 1
            if i == 7 or j == 7: break
        if i <= 7 and j <= 7 and Othello.game_board[i][j] == 0: moves.append((i, j))

    return moves


def board_updating(a, b):
    has_updated = False
    for li in Othello.available_moves:
        if (a, b) in li:
            if a != li[0][0] or b != li[0][1]:
                flipping(a, b, li[0][0], li[0][1], Othello.turn)
                has_updated = True
    if has_updated:
        Othello.available_moves.clear();
        if Othello.turn == 1:
            for a, b in Othello.white_disks:
                Othello.available_moves.append(finding_available_moves(a, b, -Othello.turn))
        else:
            for a, b in Othello.black_discs:
                Othello.available_moves.append(finding_available_moves(a, b, -Othello.turn))
        Othello.turn *= -1

        print(Othello.available_moves)


class Othello(arcade.Window):
    game_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, -1, 1, 0, 0, 0],
                  [0, 0, 0, 1, -1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]
    black_discs = [(3, 4), (4, 3)]
    white_disks = [(3, 3), (4, 4)]
    available_moves = [[(4, 3), (2, 3), (4, 5)], [(3, 4), (3, 2), (5, 4)]]
    turn = 1

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        arcade.start_render()
        for i in range(0, 8):
            for j in range(0, 8):
                arcade.draw_rectangle_outline(200 + 50 * i, 450 - 50 * j, 50, 50, arcade.color.WHITE)
        draw_game_board()
        arcade.draw_text("Turn: " + ("Black" if Othello.turn == 1 else "White"), 240, 500, arcade.color.BLACK, 50)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if 175 < x < 575 and 75 < y < 475:
                (a, b) = index_finding(x, y)
                board_updating(a, b)


def main():
    Othello(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
