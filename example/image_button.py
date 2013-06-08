#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dtk.ui.init_skin import init_theme
init_theme()
from dtk.ui.application import Application
from dtk.ui.button import ImageButton
from dtk.ui.theme import ui_theme
import gtk

if __name__ == "__main__":
    application = Application()
    application.set_default_size(600, 450)
    application.add_titlebar(title="ImageButton example!")
    
    image_button = ImageButton(
        normal_dpixbuf=ui_theme.get_pixbuf("button/radio_button_active_normal.png"),
        hover_dpixbuf=ui_theme.get_pixbuf("button/radio_button_active_hover.png"),
        press_dpixbuf=ui_theme.get_pixbuf("button/radio_button_active_press.png"),
        insensitive_dpixbuf=ui_theme.get_pixbuf("button/radio_button_active_disable.png"),
        scale_x=False,
        content=None,
        )

    image_button_align = gtk.Alignment()
    image_button_align.set(0.5, 0.5, 0, 0)
    
    image_button_align.add(image_button)
    application.main_box.add(image_button_align)
    
    application.run()
