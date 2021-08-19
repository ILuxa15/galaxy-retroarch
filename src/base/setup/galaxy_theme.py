import os
import tkinter as tk
from tkinter import ttk, font
from tksvg import SvgImage

from constants import DIR

_IMAGES = {}

COLORS = {
    'background': '#2c2a2d',
    'select': '#ca99fd',
    'header': '#333235',
    'foreground': '#f2f2f2',
    'disabled': '#565557',
    'accent': '#a47fcf'
}


def blend_colors(bg, fg, alpha):
    out = tuple(int(int(fg[i:i + 2], 16) * alpha + (1 - alpha) *
                int(bg[i:i + 2], 16)) for i in (1, 3, 5))

    return '#' + format(out[0], 'x') + format(out[1], 'x') + format(out[2], 'x')


def _init_images(root: tk.Tk):
    _IMAGES['box-active'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/box-active.svg"))
    _IMAGES['box-basic'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/box-basic.svg"))
    _IMAGES['box-hover'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/box-hover.svg"))
    _IMAGES['button-active'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/button-active.svg"))
    _IMAGES['button-basic'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/button-basic.svg"))
    _IMAGES['button-hover'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/button-hover.svg"))
    _IMAGES['ellipsis-active'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/ellipsis-active.svg"))
    _IMAGES['ellipsis-basic'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/ellipsis-basic.svg"))
    _IMAGES['ellipsis-hover'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/ellipsis-hover.svg"))
    _IMAGES['separator'] = SvgImage(
        master=root, file=os.path.join(DIR, "img/theme/separator.svg"))


def init_galaxy_theme(root: tk.Tk, style: ttk.Style):
    _init_images(root)
    root.tk_setPalette(background=COLORS['background'],
                       foreground=COLORS['foreground'])

    style.theme_create("galaxy", "default")
    style.theme_settings("galaxy", {
        "Dirbutton.button": {
            "element create": (
                "image", _IMAGES['box-basic'],
                ("pressed", _IMAGES['box-active']),
                ("hover", _IMAGES['box-hover']),
                {
                    "border": 3,
                    "sticky": 'nswe'
                }
            )
        },
        "Accent.button": {
            "element create": (
                "image", _IMAGES['button-basic'],
                ("pressed", _IMAGES['button-active']),
                ("hover", _IMAGES['button-hover']),
                {
                    "border": 3,
                    "sticky": 'nswe'
                }
            )
        },
        "Dirbutton.ellipsis": {
            "element create": (
                "image", _IMAGES['ellipsis-basic'],
                ("pressed", _IMAGES['ellipsis-active']),
                ("hover", _IMAGES['ellipsis-hover']),
                { "sticky": 'nswe' }
            ),
        },
        "Separator.separator": {
            "element create": ("image", _IMAGES['separator'])
        },
        "DirButton.TButton": {
            "layout": [('Dirbutton.button', {
                'sticky': 'nswe',
                'children': [('Dirbutton.padding', {
                    'sticky': 'nswe',
                    'children': [
                        ('Dirbutton.label', {
                            'sticky': 'nswe'
                        }),
                        ('Dirbutton.ellipsis', {
                            'side': 'right',
                            'sticky': 'nswe'
                        })
                    ]
                })]
            })],
            "configure": {
                "padding": (12, 4, 9, 4),
                "foreground": COLORS['foreground']
            }
        },
        "Accent.TButton": {
            "layout": [('Accent.button', {
                'sticky': 'nswe',
                'children': [('Accent.padding', {
                    'sticky': 'nswe',
                    'children': [
                        ('Accent.label', {
                            'sticky': 'nswe'
                        })
                    ]
                })]
            })],
            "configure": {
                "padding": (12, 6),
                "foreground": COLORS['foreground'],
                # "font": ('TkDefaultFont', -13)
            }
        }
    })