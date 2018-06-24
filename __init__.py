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
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'BugHunterPhilosopher'

LOGGER = getLogger(__name__)


class AlfredSkill(MycroftSkill):
    def __init__(self):
        super(AlfredSkill, self).__init__(name="AlfredSkill")

        # This method loads the files needed for the skill's functioning, and
        # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        wait_time_intent = IntentBuilder("AlfredIntent"). \
            require("Turn").require("Living").require("Room").require("On").build()

        self.register_intent(wait_time_intent, self.handle_turn_all_on_intent)

    def handle_turn_all_on_intent(self, message):
        self.speak('hold on')

    def stop(self):
        pass


def create_skill():
    return AlfredSkill()
