#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dtk.ui.init_skin import init_theme
init_theme()
from dtk.ui.application import Application

application = Application()
application.set_default_size(600, 450)
application.add_titlebar(title="Hello world!")
application.run()
