#!/usr/bin/env python

#l.glade through gtk-builder-convert with this command:
# gtk-builder-convert tutorial.glade tutorial.xml
# Then save this file as tutorial.py and make it executable using this command:
# chmod a+x tutorial.py
# And execute it:
# ./tutorial.py

import pygtk
pygtk.require("2.0")
import gtk

from remote import xmlrpc

class ClientApp(object):
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("client.glade")
        self.builder.connect_signals({ 
            "on_login_destroy" : gtk.main_quit ,
            "on_login_ok_clicked" : self.login_check_details,
            "on_login_cancel_clicked" : gtk.main_quit,
            "on_main_window_destroy" : gtk.main_quit ,
            "on_main_window_quit_activate" : gtk.main_quit,
            "on_main_window_entry_tree_view_cursor_changed" : self.main_window_update_main,
        })
        self.login = self.builder.get_object("login")
        self.window = self.builder.get_object("main_window")
        self.login.show()

    def login_check_details(self, arg):
        login_password = self.builder.get_object("login_password")
        login_username = self.builder.get_object("login_username")
        login_url = self.builder.get_object("login_url")
        login_dialog = self.builder.get_object("login_dialog")
        try:
            self.api = xmlrpc(login_url.get_text())
            if self.api.proxy.system.login(login_username.get_text(), login_password.get_text()):
                self.main_window_show(arg)
            else:
                login_dialog.set_text("Authentication failed!")
        except IOError:
            login_dialog.set_text("Invalid URL")

    def main_window_show(self, arg):
        self.login.hide()
        # We need to get our data and populate it here.
        self.main_window_update_data()
        self.window.show()

    def main_window_update_data(self):
        #We want to update our knowledge of the entries we have
        entry_liststore = self.builder.get_object('entry_liststore')
        entries = self.api.proxy.blogalog.list_entries()
        for entry in entries:
            iter = entry_liststore.append( [ entry['id'], entry['title'] ] )

    def main_window_update_main(self, arg):
        ### Should save the selection we are moving away from. Need a way to track
        ### The state of what we are currently looking at on the mainPane
        selection = arg.get_selection()
        (model, iter) = selection.get_selected()
        entry_id = model.get(iter, 0)[0]
        entry = self.api.proxy.blogalog.get_entry(entry_id)[0]
        visible_check = self.builder.get_object('main_window_visible_check')
        date = self.builder.get_object('main_window_date')
        text_entry = self.builder.get_object('main_window_entry')
        visible_check.set_active(entry['visible'])
        #date.set_text(entry['pub_date'])
        text_entry.get_buffer().set_text(entry['entry'])

if __name__ == "__main__":
    app = ClientApp()
    gtk.main()
