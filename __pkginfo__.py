#  This file is managed by `git_helper`. Don't edit it directly
#  Copyright (C) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This file is distributed under the same license terms as the program it came with.
#  There will probably be a file called LICEN[S/C]E in the same directory as this file.
#
#  In any case, this program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py
#

# stdlib
import pathlib

__all__ = [
		"__copyright__",
		"__version__",
		"modname",
		"pypi_name",
		"py_modules",
		"entry_points",
		"__license__",
		"__author__",
		"short_desc",
		"author",
		"author_email",
		"github_username",
		"web",
		"github_url",
		"project_urls",
		"repo_root",
		"long_description",
		"install_requires",
		"extras_require",
		"classifiers",
		"keywords",
		"import_name",
		]

__copyright__ = """
2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
"""

__version__ = "0.1.1"

modname = "wx_icons_adwaita"
pypi_name = "wx_icons_adwaita"
import_name = "wx_icons_adwaita"
py_modules = []
entry_points = {
		"console_scripts": []
		}

__license__ = "GNU Lesser General Public License v3 or later (LGPLv3+)"

short_desc = "Adwaita icon theme for wxPython 🐍"

__author__ = author = "Dominic Davis-Foster"
author_email = "dominic@davis-foster.co.uk"
github_username = "domdfcoding"
web = github_url = f"https://github.com/domdfcoding/custom_wx_icons_adwaita"
project_urls = {
		"Documentation": f"https://custom_wx_icons_adwaita.readthedocs.io",
		"Issue Tracker": f"{github_url}/issues",
		"Source Code": github_url,
		}

repo_root = pathlib.Path(__file__).parent

# Get info from files; set: long_description
long_description = (repo_root / "README.rst").read_text(encoding="utf-8").replace("0.1.1", __version__) + '\n'

install_requires = (repo_root / "requirements.txt").read_text(encoding="utf-8").split('\n')
extras_require = {'all': []}

classifiers = [
		'Development Status :: 3 - Alpha',
		'Environment :: X11 Applications :: GTK',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
		'Operating System :: OS Independent',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: Implementation :: CPython',
		'Topic :: Desktop Environment :: Gnome',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: User Interfaces',
		'Typing :: Typed',

		]

keywords = "wxpython icons iconset adwaita"
