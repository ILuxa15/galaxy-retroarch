import tkinter as tk
from tkinter import ttk

from galaxy_theme import blend_colors


class Page(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._header = tk.Frame(master=self,
                                background=blend_colors(
                                    self['bg'], '#ffffff', 0.03),
                                height=74, padx=30, pady=16)
        self._header.pack(side=tk.TOP, fill=tk.X)

        self._content = tk.Frame(master=self, padx=30, pady=30)
        self._content.grid_columnconfigure(0, weight=1)
        self._content.grid_columnconfigure(1, weight=3)
        self._content.pack(expand=True, fill=tk.BOTH)

        self._separator = ttk.Separator(master=self, orient='horizontal')
        self._separator.pack(fill=tk.X)

        self._footer = tk.Frame(master=self, height=74, padx=30, pady=16)
        self._footer.pack(side=tk.BOTTOM, fill=tk.X)

    @property
    def header(self):
        return self._header

    @property
    def footer(self):
        return self._footer

    @property
    def content(self):
        return self._content
