#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pattern/singleton.py
# Description : Singleton pattern
# Auteur : Nils Schaetti <n.schaetti@gmail.com>
# Date : 09.08.2017 15:48:00
# Lieu : Nyon, Suisse
#
# This file is part of the TwitterAnalyzer.
# The TwitterAnalyzer is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTweetBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with pyTweetBar.  If not, see <http://www.gnu.org/licenses/>.
#


def singleton(class_):

    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        # end if
        return instances[class_]
    # end getinstance

    return getinstance

# end singleton