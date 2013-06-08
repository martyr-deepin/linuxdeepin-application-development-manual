#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dtk.ui.init_skin import init_theme
init_theme()
from dtk.ui.application import Application
from dtk.ui.button import Button
import gtk

if __name__ == "__main__":
    application = Application()
    application.set_default_size(600, 450)
    application.add_titlebar(title="Button example!")
    
    button = Button("Linux Deepin", 12)

    button_align = gtk.Alignment()
    button_align.set(0.5, 0.5, 0, 0)
    
    button_align.add(button)
    application.main_box.add(button_align)
    
    application.run()
