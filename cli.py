#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Hoang Minh Thang <p[at]banphim[dot]net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import pynotify
from miniclip import run_action
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-p", "--primary", dest="primary", default=False,
                  action="store_true",
                  help="Use primary selection instead of clipboard")
parser.add_option("-j", "--jade", dest="jade", action="store_true",
                  help="Convert HTML to Jade")
parser.add_option("-s", "--stylus", dest="stylus", action="store_true",
                  help="Convert CSS to Stylus")
parser.add_option("-c", "--coffee", dest="coffee", action="store_true",
                  help="Convert JS to Coffee")

if __name__ == "__main__":
  if not pynotify.init("Basics"):
    sys.exit(1)
  (options, args) = parser.parse_args()
  if options.primary:
    clipboard_type = "PRIMARY"
  else:
    clipboard_type = "CLIPBOARD"
  conversion = filter(lambda(x): True == getattr(options, x),["jade", "stylus", "coffee"])
  if len(conversion) != 1:
    print "One conversion type at a time, please"
    sys.exit(1)
  run_action(clipboard_type, conversion[0])
