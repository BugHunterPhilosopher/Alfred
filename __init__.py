"""
mycroft-hue : A Mycroft skill for controlling Phillips Hue

Copyright (C) 2016  Christopher Rogers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from os.path import dirname
from phue import Group
from phue import PhueRequestTimeout
from requests import ConnectionError
from requests import get

__author__ = 'BugHunterPhilosopher'

LOGGER = getLogger(__name__)


def intent_handler(handler_function):
    """
    Decorate handler functions with connection and
    error handling.

    Parameters
    ----------
    handler_function : callable

    Returns
    -------
    callable

    """
    def handler(self, message):
        if message.type == 'ConnectLightsIntent' \
                or self.connected or self._connect_to_bridge():
            group = self.default_group
            if "Group" in message.data:
                name = message.data["Group"].lower()
                group_id = self.groups_to_ids_map[name]
                group = Group(self.bridge, group_id)
            try:
                handler_function(self, message, group)
            except PhueRequestTimeout:
                self.speak_dialog('unable.to.perform.action')
            except Exception as e:
                if 'No route to host' in e.args:
                    if self.user_supplied_ip:
                        self.speak_dialog('no.route')
                        return
                    else:
                        self.speak_dialog('could.not.communicate')
                        if self._connect_to_bridge(True):
                            self.handle_intent(message)
                else:
                    raise
    return handler


class AlfredSkill(MycroftSkill):

    def __init__(self):
        super(AlfredSkill, self).__init__(name="AlfredSkill")

        verbose = self.settings.get('verbose', False)
        if type(verbose) == str:
            verbose = verbose.lower()
            verbose = True if verbose == 'true' else False
        self.verbose = verbose

    @property
    def connected(self):
        return True

    @property
    def user_supplied_ip(self):
        return self.settings.get('ip') != ''

    @property
    def user_supplied_username(self):
        return self.settings.get('username') != ''

    def initialize(self):
        """
        Attempt to connect to the bridge,
        and build/register intents.
        """
        self.load_data_files(dirname(__file__))

        turn_all_on_intent = IntentBuilder("TurnAllOnIntent").require("Turn").require("LivingRoom").require("On")\
            .build()
        self.register_intent(turn_all_on_intent, self.handle_turn_all_on_intent)

    @intent_handler(IntentBuilder("").require("Turn").require("LivingRoom").require("On"))
    def handle_turn_all_on_intent(self, message):
        self.speak_dialog('turn.all.on')


def create_skill():
    return AlfredSkill()
