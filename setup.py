#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2019 by sailoog <https://github.com/sailoog/openplotter>
#                     e-sailing <https://github.com/e-sailing/openplotter>
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from openplotterSKfilter import version

setup (
	name = 'openplotterSKfilter',
	version = version.version,
	description = 'Tool OpenPlotter app',
	license = 'GPLv3',
	author="e-sailing",
	author_email='e.minus.sailing@gmail.com',
	url='https://github.com/openplotter/openplotter-SKfilter',
	packages=['openplotterSKfilter'],
	install_requires=['websocket_client'],
	classifiers = ['Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 3'],
	include_package_data=True,
	entry_points={'console_scripts': ['openplotter-SKfilter=openplotterSKfilter.openplotterSKfilter:main','diagnostic-SKinput=openplotterSKfilter.diagnosticSKinput:main', 'SKfilterPostInstall=openplotterSKfilter.SKfilterPostInstall:main', 'SKfilterPreUninstall=openplotterSKfilter.SKfilterPreUninstall:main']},
	data_files=[('share/applications', ['openplotterSKfilter/data/openplotter-SKfilter.desktop','openplotterSKfilter/data/openplotter-diagnostic-SK.desktop']),('share/pixmaps', ['openplotterSKfilter/data/openplotter-SKfilter.png','openplotterSKfilter/data/diagnosticSKinput.png']),],
	)
