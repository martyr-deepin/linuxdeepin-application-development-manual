#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dtk.ui.init_skin import init_theme
init_theme()
from dtk.ui.application import Application
from dtk.ui.button import CheckButton
import gtk

if __name__ == "__main__":
    application = Application()
    application.set_default_size(600, 450)
    application.add_titlebar(title="CheckButton example!")
    
    check_button_1 = CheckButton(
        label_text="科幻片",
        padding_x=5,
        )

    check_button_2 = CheckButton(
        label_text="动作片",
        padding_x=5,
        )

    check_button_3 = CheckButton(
        label_text="悬疑片",
        padding_x=5,
        )
    
    check_button_box = gtk.VBox()
    
    check_button_align = gtk.Alignment()
    check_button_align.set(0.5, 0.5, 0, 0)
    
    check_button_box.pack_start(check_button_1)
    check_button_box.pack_start(check_button_2)
    check_button_box.pack_start(check_button_3)
    check_button_align.add(check_button_box)
    application.main_box.add(check_button_align)
    
    application.run()
