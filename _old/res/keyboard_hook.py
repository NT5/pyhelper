#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

from collections import namedtuple
from ctypes import windll, CFUNCTYPE, POINTER, c_int, c_void_p, byref
import win32con, win32api, win32gui, atexit

KeyboardEvent = namedtuple('KeyboardEvent', ['event_type', 'key_code', 'scan_code', 'alt_pressed', 'time'])

class key_hook:
	def __init__( self, class_handler ):
		self.class_handler = class_handler
		print "[+] Key!Hook instance created!"
	
	def start(self):
		print "[+] Key!Hook running"
		self.event_types = {win32con.WM_KEYDOWN: 'key down', win32con.WM_KEYUP: 'key up', 0x104: 'key down', 0x105: 'key up', }	
		CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
		pointer = CMPFUNC(self.low_level_handler)
		self.hook_id = windll.user32.SetWindowsHookExA(win32con.WH_KEYBOARD_LL, pointer, win32api.GetModuleHandle(None), 0)
		atexit.register(windll.user32.UnhookWindowsHookEx, self.hook_id)

		while True:
			msg = win32gui.GetMessage(None, 0, 0)
			win32gui.TranslateMessage(byref(msg))
			win32gui.DispatchMessage(byref(msg))
		
	def low_level_handler(self, nCode, wParam, lParam):
		event = KeyboardEvent(self.event_types[wParam], lParam[0], lParam[1], lParam[2] == 32, lParam[3])
		self.class_handler( event )
		return windll.user32.CallNextHookEx(self.hook_id, nCode, wParam, lParam)
		
