#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.0.0-rc-1544118437
# name: message
# license: MIT

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from format_text import Format_text as ft
from modules.json_config.json_config import Json_config
del sys.path[0:2]

ft.clear_scrolling_history()
print("scrolling history has been erased")

ft.clear_screen()
print("screen has been cleared")

msg.title("This is a title")

msg.subtitle("This is a subtitle")
print()

msg.info("This is a single line info")
print()
msg.info(
    "This is a multiline info",
    "This is a multiline info",
    "This is a multiline info"
    )
print()
msg.warning("This is a single line warning")
print()
msg.warning(
    "This is a multiline line warning",
    "This is a multiline line warning",
    "This is a multiline line warning"
    )
print()

msg.success("This is a single line success")
print()
msg.success(
    "This is a multiline line success",
    "This is a multiline line success",
    "This is a multiline line success"
    )
print()

msg.app_error("This is a single line internal error")
print()
msg.app_error(
    "This is a multiline internal error",
    "This is a multiline internal error",
    "This is a multiline internal error",
    )
print()
msg.user_error("This is a user error")
print()
msg.user_error(
    "This is a multiline user error",
    "This is a multiline user error",
    "This is a multiline user error",
    )
print()

Json_config().set_value("debug", True)
msg.dbg("info", "This is a debug info message")
msg.dbg("subtitle", "This is a debug subtitle, debug can apply to any msg type")
