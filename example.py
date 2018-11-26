#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.0.0-rc-1543251853
# name: shell_helpers
# license: MIT

import shell_helpers as shell

try:
	import modules.message.message as msg
except:
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    import message.message as msg

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
