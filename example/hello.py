#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from deepin_utils.file import get_parent_dir
from dtk.ui.init_skin import init_skin
app_theme = init_skin(
    "deepin-ui-example", 
    "1.0",
    "glass",
    os.path.join(get_parent_dir(__file__), "skin"),
    )
from dtk.ui.application import Application

if __name__ == "__main__":
    application = Application()
    application.set_default_size(600, 450)
    application.add_titlebar(
        button_mask=["theme", "max", "min", "close"],
        title="Hello world!"
        )
    application.run()
