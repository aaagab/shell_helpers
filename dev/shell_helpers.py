#!/usr/bin/env python3
# author: Gabriel Auger
# version: 2.1.4
# name: shell_helpers
# license: MIT

import platform
import shutil
import subprocess
import sys
import shlex
import inspect

import sys, os

from ..gpkgs import message as msg

def get_split_cmd(command):
    split_cmd=shlex.split(command)
    if platform.system() == "Windows":
        if shutil.which(split_cmd[0]) is None:
            split_cmd.insert(0, "cmd")
            split_cmd.insert(1, "/c")
    return split_cmd

def cmd_devnull(command):
    try:
        return subprocess.check_call(get_split_cmd(command), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as proc:
        return proc.returncode

# ideal for any command with prompt
def cmd(command):
    try:
        return subprocess.call(get_split_cmd(command), shell=False)
    except subprocess.CalledProcessError as proc:
        return proc.returncode

def cmd_get_value(command):
    try:
        process = subprocess.Popen(get_split_cmd(command), 
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
            msg.error("Command: '"+command+"', err: "+stderr.decode("utf-8"))
            sys.exit(1)
    except Exception as e:
        frame,filename,line_number,function_name,lines,index=inspect.stack()[1]
        print(e)
        print("\t"+str(line_number)+": "+filename)
        msg.error("Command: '"+command)
        sys.exit(1)

def cmd_prompt(cmd_txt, prompt_msg=False):
    if prompt_msg:
        msg.info(cmd_txt)

    if cmd(cmd_txt) == 0:
        msg.success(cmd_txt)
    else:
        msg.error(cmd_txt +" failed!")
        sys.exit(1)
