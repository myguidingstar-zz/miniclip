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

import pygtk, gtk, pynotify
pygtk.require('2.0')

from subprocess import Popen, PIPE
def pipeData(command, data):
  sub       = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
  out, err  = sub.communicate(data)
  rc = sub.returncode
  return [out, err, rc]

convertCommands = {}
convertCommands["jade"]   = ['html2jade']
convertCommands["coffee"] = ['js2coffee']
convertCommands["stylus"] = ['stylus', '-C']

# Eg: out, err, rc = pipeData(convertCommands["stylus"], css_code)

display=gtk.gdk.display_get_default()

def getClipboard():
  return gtk.Clipboard(display, "CLIPBOARD").wait_for_text()

def setClipboard(text):
  clipboard = gtk.Clipboard(display, "CLIPBOARD")
  clipboard.set_text(text)
  clipboard.store()

def notify(title, content=""):
  pynotify.Notification(title, content).show()

def notEmptyString(text):
  return isinstance(text, str) or isinstance(text, unicode) and text != ""

def run_action(name):
  text = getClipboard()
  if notEmptyString(text):
    out, err, rc = pipeData(convertCommands[name], text)
    if rc == 0:
      if text == out:
        notify("Nothing happened!")
      else:
        if notEmptyString(out):
          setClipboard(out)
          notify("Converted successfully!", out[:200])
        else:
          notify("Got an empty output...", "Please check your input!")
    else:
      notify("Error converting:", "Program exited with code: " + str(rc))
      notify("Error output: ", err[:120])

  else:
    notify("No text found on clipboard...")

class SystrayIconApp:
  def __init__(self):
    self.tray = gtk.StatusIcon()
    self.tray.set_from_stock(gtk.STOCK_COPY)
    self.tray.connect('popup-menu', self.on_right_click)
    self.tray.connect('activate', self.on_left_click)
    self.tray.set_tooltip(('Miniclip tray app'))


  def on_right_click(self, icon, event_button, event_time):
    self.make_menu(event_button, event_time)

  def on_left_click(self, widget):
    menu = gtk.Menu()

    # show jade dialog
    jade = gtk.MenuItem("HTML -> Jade")
    jade.show()
    menu.append(jade)
    jade.connect('activate', self.show_jade_dialog)

    # show stylus dialog
    stylus = gtk.MenuItem("CSS  -> Stylus")
    stylus.show()
    menu.append(stylus)
    stylus.connect('activate', self.show_stylus_dialog)

    # show coffee dialog
    coffee = gtk.MenuItem("JS  -> Coffee")
    coffee.show()
    menu.append(coffee)
    coffee.connect('activate', self.show_coffee_dialog)

    menu.popup(None, None, gtk.status_icon_position_menu,
               0, 0, self.tray)

  def make_menu(self, event_button, event_time):
    menu = gtk.Menu()

    # show about dialog
    about = gtk.MenuItem("About")
    about.show()
    menu.append(about)
    about.connect('activate', self.show_about_dialog)

    # add quit item
    quit = gtk.MenuItem("Quit")
    quit.show()
    menu.append(quit)
    quit.connect('activate', gtk.main_quit)

    menu.popup(None, None, gtk.status_icon_position_menu,
               event_button, event_time, self.tray)

  def show_about_dialog(self, widget):
    about_dialog = gtk.AboutDialog()
    about_dialog.set_destroy_with_parent (True)
    about_dialog.set_icon_name ("edit-paste")
    about_dialog.set_name('Miniclip')
    about_dialog.set_version('0.2')
    about_dialog.set_copyright("(C) 2012 Hoang Minh Thang")
    about_dialog.set_comments(("""
    A Linux tray app that quickly converts HTML to Jade, JS to Coffee and CSS to Stylus from clipboard
    """))
    about_dialog.set_authors(['Hoang Minh Thang <p@banphim.net>'])
    about_dialog.run()
    about_dialog.destroy()

  def show_jade_dialog(self, widget):
    run_action("jade")

  def show_stylus_dialog(self, widget):
    run_action("stylus")

  def show_coffee_dialog(self, widget):
    run_action("coffee")

if __name__ == "__main__":
  if not pynotify.init("Basics"):
    sys.exit(1)
  SystrayIconApp()
  gtk.main()
