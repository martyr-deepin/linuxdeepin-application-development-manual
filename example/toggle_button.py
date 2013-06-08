#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dtk.ui.init_skin import init_theme
init_theme()
from dtk.ui.application import Application
from dtk.ui.button import ToggleButton
from dtk.ui.theme import ui_theme
from dtk.ui.dialog import ConfirmDialog
import gtk

if __name__ == "__main__":
    application = Application()
    application.set_default_size(600, 450)
    application.add_titlebar(title="ToggleButton example!")
    
    toggle_button = ToggleButton(
        inactive_normal_dpixbuf=ui_theme.get_pixbuf("switchbutton/off.png"),
        active_normal_dpixbuf=ui_theme.get_pixbuf("switchbutton/on.png"),
        button_label="This is toggle button",
        padding_x=5,
        )
    toggle_button.connect(
        "toggled", 
        lambda w: ConfirmDialog(
            "反馈对话框",
            "按钮开启" if w.get_active() else "按钮关闭",
            ).show_all())
    
    toggle_button_align = gtk.Alignment()
    toggle_button_align.set(0.5, 0.5, 0, 0)
    
    toggle_button_align.add(toggle_button)
    application.main_box.add(toggle_button_align)
    
    application.run()
