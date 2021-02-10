from distutils.core import setup
import py2exe

setup(
	name='py!np',
	version='0.1',
	author='NT5',
	license="GPL",
	options = {'build': {'build_base': 'compile/build'}, 'py2exe': { 'dll_excludes': ['w9xpopen.exe'], 'packages': ['win32api', 'win32gui', 'win32con'], 'bundle_files': 1, 'compressed': True, 'optimize': 2}},
	zipfile = None,
	# data_files=[("",["config.json"])],
	windows = [{
            "script": "preview.py",
            "icon_resources": [(0, "icon.ico")]
	}],
	# console=[{'script': 'pyhelper.py'}]
)