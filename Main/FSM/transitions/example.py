#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ
Email: yj1516268@outlook.com
Created Date: 2018-10-29 16:08:38


"""

from transitions import Machine
import random


class NarcolepticSuperhero(object):

    # 定义有限的状态
    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']

    def __init__(self, name):
        self.name = name

        # flags
        self.kittens_rescued = 0

        # 初始化状态机
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states,
                               initial='asleep')

        self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')
        self.machine.add_transition('work_out', 'hanging out', 'hungry')
        self.machine.add_transition('eat', 'hungry', 'hanging out')
        self.machine.add_transition('distress_call', '*', 'saving the world', before='change_into_super_secret_costume')
        self.machine.add_transition('complete_mission', 'saving the world', 'sweaty', after='update_journal')
        self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'sweaty', 'hanging out')
        self.machine.add_transition('nap', '*', 'asleep')

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    def is_exhausted(self):
        """随机数"""
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")


batman = NarcolepticSuperhero('Batman')
print(batman.state)
batman.distress_call()
print(batman.state)
print(batman.state)
