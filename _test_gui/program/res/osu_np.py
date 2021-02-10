#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

import win32con, win32api, win32gui, ctypes, ctypes.wintypes, re

class COPYDATASTRUCT(ctypes.Structure):
	_fields_ = [('dwData', ctypes.wintypes.LPARAM), ('cbData', ctypes.wintypes.DWORD), ('lpData', ctypes.c_void_p)]

PCOPYDATASTRUCT = ctypes.POINTER(COPYDATASTRUCT)

class Listener:
	def __init__(self, _class_handler):
		self._class_handler = _class_handler
		print "[+] Osu!np instance created!"
		
	def start(self):
		print "[+] Osu!np running"
		message_map = {
			win32con.WM_COPYDATA: self.OnCopyData
		}
		
		wc = win32gui.WNDCLASS()
		wc.lpfnWndProc = message_map
		wc.lpszClassName = 'MsnMsgrUIManager'
		hinst = wc.hInstance = win32api.GetModuleHandle(None)
		classAtom = win32gui.RegisterClass(wc)
		self.hwnd = win32gui.CreateWindow ( classAtom, "pyNPOsu", 0, 0, 0, win32con.CW_USEDEFAULT,  win32con.CW_USEDEFAULT, 0, 0, hinst, None )

		win32gui.PumpMessages()

	def OnCopyData(self, hwnd, msg, wparam, lparam):
		pCDS = ctypes.cast(lparam, PCOPYDATASTRUCT)
		_data = ctypes.wstring_at(pCDS.contents.lpData)
		
		_parse_data = self.data_handler( _data )
		self._class_handler( _parse_data )
		
		return 1
		
	def data_handler( self, data ):
		def _get_diff( text ):
			if text == "Playing": return 0
			elif text == "Watching": return 1
			else: return 3
			
		regex = re.compile("\\\\0(.*?)\\\\01.*?\\\\0(.*?) \{0\} - (?:.*?)\\\\0(.*?)\\\\0(.*?)\\\\0(.*?)\\\\0(.*?)\\\\0",re.UNICODE)
		reg = regex.findall( data )
		
		if reg:
			reg = reg[0]
			return { 'type': reg[0], 'action': _get_diff(reg[1]), 'name': reg[2], 'artist': reg[3], 'player': reg[4], 'difficulty': None if len(reg[5]) <= 0 else reg[5] }
		else: return None

