import sys

from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType

from nes.version import __version__ as version

class NESPlugin(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(Platform.NintendoEntertainmentSystem, version, reader, writer, token)
