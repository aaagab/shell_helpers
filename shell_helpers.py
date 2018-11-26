#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.0.0-rc-1543256431
# name: shell_helpers
# license: MIT

import subprocess
import sys
import shlex
import inspect

try:
	import modules.message.message as msg
except:
    # try:
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    import message.message as msg
	# except:
		# import message as msg

def cmd_devnull(command):
    try:
        return subprocess.check_call(shlex.split(command), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as proc:
        return proc.returncode

# ideal for any command with prompt
def cmd(command):
    try:
        return subprocess.call(shlex.split(command), shell=False)
    except subprocess.CalledProcessError as proc:
        return proc.returncode

def cmd_get_value(command):
    try:
        process = subprocess.Popen(shlex.split(command), 
                                    shell=False, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
        ( stdout, stderr ) = process.communicate()
        if not stderr:
            if stdout:
                return stdout.decode("utf-8").rstrip()
            else:
                return ""
        else:
            frame,filename,line_number,function_name,lines,index=inspect.stack()[1]
            print("\t"+str(line_number)+": "+filename)
            msg.app_error("Command: '"+command+"', err: "+stderr.decode("utf-8"))
            sys.exit(1)
    except Exception as e:
        frame,filename,line_number,function_name,lines,index=inspect.stack()[1]
        print("\t"+str(line_number)+": "+filename)
        msg.app_error("Command: '"+command)
        sys.exit(1)

def cmd_prompt(cmd_txt, prompt_msg=False):
    if prompt_msg:
        msg.info(cmd_txt)

    if cmd(cmd_txt) == 0:
        msg.success(cmd_txt)
    else:
        msg.app_error(cmd_txt +" failed!")
        sys.exit(1)
