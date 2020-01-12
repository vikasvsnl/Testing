# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:04:03 2019

@author: Synophic
"""
from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

commands = input ("Enter Commands: ")
cmds = commands.split(",")

for cmd in cmds:
    nr = InitNornir()

    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
        )

    print_result(result)