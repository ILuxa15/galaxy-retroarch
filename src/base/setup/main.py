import tkinter as tk
from tkinter import ttk, font
from tkinter.filedialog import askdirectory
from tksvg import SvgImage

import os
from base.setup.galaxy_theme import COLORS, blend_colors

from galaxy_theme import init_galaxy_theme
from page import Page

from constants import ICON, DIR


class SetupApplication():
    def __init__(self):
        self._root = tk.Tk()
        self._root.geometry("486x423")
        self._root.resizable(False, False)
        self._root.title("RetroArch Setup")
        self._root.iconbitmap(ICON)

        self._style = ttk.Style(self._root)

        init_galaxy_theme(self._root, self._style)
        self._style.theme_use("galaxy")

        self._setup_page = SetupPage(self._root)
        self._setup_page.pack(expand=True, fill=tk.BOTH)

    def run(self):
        self._root.mainloop()


class SetupPage(Page):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._logo_img = SvgImage(master=self.header,
                                  file=os.path.join(DIR, "img/logo", "retroarch-logo.svg"))
        self._logo = tk.Label(self.header, background=self.header['background'],
                              image=self._logo_img)
        self._logo.grid(column=0, row=0, rowspan=2)

        self._title = tk.Label(self.header, background=self.header['background'],
                               font=('TkDefaultFont', -13, 'bold'), text="RetroArch Setup")
        self._title.grid(column=1, row=0, padx=15, sticky=tk.W)

        self._subtitle = tk.Label(self.header, background=self.header['background'],
                                  text="Specify the directory where RetroArch is installed")
        self._subtitle.grid(column=1, row=1, padx=15, sticky=tk.W)

        self._desc = tk.Label(self.content, justify='left', wraplength=426,
                              text="Specify the directory where RetroArch is installed to access your Nintendo Entertainment System games.")
        self._desc.grid(column=0, row=0, columnspan=2, sticky=tk.W)

        self._dir_path_label = tk.Label(
            self.content, justify='left', foreground=blend_colors(self._content["background"], COLORS['foreground'], 0.6), text="RetroArch directory")
        self._dir_path_label.grid(column=0, row=1, pady=30, sticky=tk.W)

        self._dir_button = ttk.Button(
            self.content, style="DirButton.TButton", width=1, command=self._choose_dir)
        self._dir_button.grid(column=1, row=1, sticky=tk.EW)

        self._continue_button = ttk.Button(self.footer, style="Accent.TButton", text="Continue")
        self._continue_button.pack(side=tk.RIGHT)

    def _choose_dir(self):
        dir = askdirectory()
        self._dir_button['text'] = dir

setup = SetupApplication()
setup.run()

