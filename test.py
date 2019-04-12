#!/usr/bin/env python3
# author: Gabriel Auger
# version: 0.1.0
# name: shell_helpers
# license: MIT

import sys, os
import importlib
direpa_script_parent=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
module_name=os.path.basename(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, direpa_script_parent)
pkg = importlib.import_module(module_name)
del sys.path[0]

cmd="ls -l"

pkg.msg.info("execute command '{}' WITH output.".format(cmd))
pkg.shell.cmd(cmd)
print()

pkg.msg.info("execute command '{}' WITHOUT output.".format(cmd))
pkg.shell.cmd_devnull(cmd)
print()

pkg.msg.info("command returns exit code '{}'".format(cmd))
print(pkg.shell.cmd_devnull(cmd))
print()

pkg.msg.info("get command '{}' output in variable.".format(cmd))
output=pkg.shell.cmd_get_value(cmd)
print(output)
print()

pkg.msg.info("verbose command '{}' mode.".format(cmd))
pkg.shell.cmd_prompt(cmd, True)
print()