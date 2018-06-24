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
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'BugHunterPhilosopher'

LOGGER = getLogger(__name__)


class AlfredSkill(MycroftSkill):

    def __init__(self):
        super(AlfredSkill, self).__init__(name="AlfredSkill")

        verbose = self.settings.get('verbose', False)
        if type(verbose) == str:
            verbose = verbose.lower()
            verbose = True if verbose == 'true' else False
        self.verbose = verbose

    def initialize(self):
        """
        Attempt to connect to the bridge,
        and build/register intents.
        """

    @intent_handler(IntentBuilder("AlfredIntent").require("Turn").require("LivingRoom").require("On"))
    def handle_turn_all_on_intent(self, message):
        self.speak_dialog('turn.all.on')


def create_skill():
    return AlfredSkill()
