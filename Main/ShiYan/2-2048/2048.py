#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import curses
from random import randrange, choice    # 放置新元素
from collections import defaultdict


actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']    # 有效事件
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']   # 有效输入按键
actions_dict = dict(zip(letter_codes, actions * 2))  # 将输入与行为进行关联


"""（有限）状态机(FSM)是处理游戏主逻辑时常用的技术
状态机会一直循环，直到达到终结状态而结束程序"""


def get_user_action(keyboard):
    """用户输入处理"""
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


def transpose(field):
    """矩阵转置：行列互转"""
    return [list(row) for row in zip(*field)]


def invert(field):
    """矩阵逆置：元素逆置"""
    return [row[::-1] for row in field]


class GameField:
    """创建棋盘"""
    def __init__(self, height=4, width=4, win=2048):
        """默认4 x 4，胜利分为2048"""
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0      # 即时分数
        self.highscore = 0  # 最高分
        self.field = None   # 游戏区域
        self.reset()

    def reset(self):
        """重置游戏"""
        if self.score > self.highscore:
            '''刷新最高分'''
            self.highscore = self.score
        self.score = 0  # 分数归零
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self, direction):
        """移动元素"""
        def move_row_left(row):
            """向左合并每行"""
            def tighten(row):
                """将零散的非零元素放在一起"""
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                """合并临近元素"""
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            # 先放在一起后合并再放在一起
            return tighten(merge(tighten(row)))

        # 左移，并从矩阵转置和逆转得到其他三个方向的移动操作
        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        """赢局的操作"""
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        """输局的操作"""
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        """绘制界面"""
        help_string_1 = '        (W)Up'
        help_string_2 = '(A)Lfet (S)Down (D)Right'
        help_string_3 = '    (R)Retry (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'

        def cast(string):
            """输出帮助信息"""
            screen.addstr(string + '\n')

        def draw_hor_separator():
            """绘制水平分割线"""
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            """绘制行"""
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()
        cast('SCORE{}'.format(str(self.score)))
        if 0 != self.highscore:
            cast('HIGHSCORE: {}'.format(str(self.highscore)))

        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string_1)
                cast(help_string_2)
        cast(help_string_3)

    def spawn(self):
        """随机产生4或2，产生2的几率是12%"""
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def move_is_possible(self, direction):
        """判断能否移动"""
        def row_is_left_movable(row):
            """能左移"""
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:   # 可以移动
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:    # 可以合并
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False


def main(stdscr):
    """主逻辑"""
    def init():
        game_field.reset()  # 重置棋盘
        return "Game"

    def not_game(state):
        # 绘制输赢的界面
        game_field.draw(stdscr)
        # 读取用户输入，得到action，判断是 restart 还是 exit
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)  # 默认是当前界面，无操作则在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'    # 对应不同行为，转换不同状态
        return responses[action]

    def game():
        # 画出当前棋盘状态
        game_field.draw(stdscr)
        # 读取用户输入，得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        elif action == 'Exit':
            return 'Exit'
        if game_field.move(action):  # 移动成功
            if game_field.is_win():
                return 'Win'
            elif game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game,
    }

    curses.use_default_colors()

    # 设置获胜状态最大元素数字为 32——测试用
    game_field = GameField(win=2048)

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)
