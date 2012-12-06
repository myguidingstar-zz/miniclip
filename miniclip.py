#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, gtk, pynotify

main_commands = {}
main_commands["jade"]   = lambda: os.system('xsel -b | html2jade | xsel -bi')
main_commands["stylus"] = lambda: os.system('xsel -b | stylus -C | xsel -bi')
main_commands["coffee"] = lambda: os.system('xsel -b | js2coffee | xsel -bi')

def run_action(name):
  main_commands[name]()

def notify(title, content):
  pynotify.Notification(title, content).show()

class SystrayIconApp:
  def __init__(self):
    self.tray = gtk.StatusIcon()
    self.tray.set_from_stock(gtk.STOCK_COPY)
    self.tray.connect('popup-menu', self.on_right_click)
    self.tray.set_tooltip(('Miniclip tray app'))


  def on_right_click(self, icon, event_button, event_time):
    self.make_menu(event_button, event_time)

  def make_menu(self, event_button, event_time):
    menu = gtk.Menu()

    # show about dialog
    about = gtk.MenuItem("About")
    about.show()
    menu.append(about)
    about.connect('activate', self.show_about_dialog)

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
    about_dialog.set_icon_name ("Miniclip")
    about_dialog.set_name('SystrayIcon')
    about_dialog.set_version('0.1')
    about_dialog.set_copyright("(C) 2012 Hoang Minh Thang")
    about_dialog.set_comments(("A Linux tray app that quickly converts HTML to Jade and CSS to Stylus from clipboard"))
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



