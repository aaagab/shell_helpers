#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.0.0-rc-1544126767
# name: shell_helpers
# license: MIT

import sys, os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import shell_helpers as shell
import modules.message.message as msg

del sys.path[0:2]

cmd="ls -l"

msg.info("execute command '{}' WITH output.".format(cmd))
shell.cmd(cmd)
print()

msg.info("execute command '{}' WITHOUT output.".format(cmd))
shell.cmd_devnull(cmd)
print()

msg.info("command returns exit code '{}'".format(cmd))
print(shell.cmd_devnull(cmd))
print()

msg.info("get command '{}' output in variable.".format(cmd))
output=shell.cmd_get_value(cmd)
print(output)
print()

msg.info("verbose command '{}' mode.".format(cmd))
shell.cmd_prompt(cmd, True)
print()
