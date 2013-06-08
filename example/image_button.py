#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dtk.ui.init_skin import init_skin
import os
from deepin_utils.file import get_parent_dir, get_current_dir
app_theme = init_skin(
        "deepin-ui",
        "1.0",
        "default",
        os.path.join(get_parent_dir(__file__, 2), "skin"),
        os.path.join(get_current_dir(__file__), "app_theme"),
        )
from dtk.ui.application import Application
from dtk.ui.button import ImageButton
from dtk.ui.dialog import ConfirmDialog
import gtk

if __name__ == "__main__":
    application = Application()
    application.set_default_size(600, 450)
    application.add_titlebar(title="ImageButton example!")
    
    image_button = ImageButton(
        normal_dpixbuf=app_theme.get_pixbuf("action/play_normal.png"),
        hover_dpixbuf=app_theme.get_pixbuf("action/play_hover.png"),
        press_dpixbuf=app_theme.get_pixbuf("action/play_press.png"),
        insensitive_dpixbuf=None,
        scale_x=False,
        content=None,
        )
    image_button.connect(
        "clicked", 
        lambda w: ConfirmDialog(
            title="反馈对忽框",
            message="点击播放按钮",
            ).show_all())

    image_button_align = gtk.Alignment()
    image_button_align.set(0.5, 0.5, 0, 0)
    
    image_button_align.add(image_button)
    application.main_box.add(image_button_align)
    
    application.run()
