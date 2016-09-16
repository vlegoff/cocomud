"""This demo file creates a simple client with TTS support."""

import wx

from ytranslate.tools import init, select

init(root_dir="translations")
select("en")

from game import GameEngine
from ui.window import MainWindow

app = wx.App()
engine = GameEngine()
engine.load()
client = engine.open("vanciamud.fr", 4000)
window = MainWindow(engine)
client.link_window(window)
client.start()
app.MainLoop()
