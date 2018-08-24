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
import urllib.request
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'BugHunterPhilosopher'

LOGGER = getLogger(__name__)


class AlfredSkill(MycroftSkill):
    def __init__(self):
        super(AlfredSkill, self).__init__(name="AlfredSkill")

        self.apikey = ""
        self.jeedomaddress = ""

        self.idopen = ""
        self.idclose = ""
        self.idon = ""
        self.idoff = ""
        self.idorange = ""
        self.idred = ""
        self.idgreen = ""
        self.idblue = ""
        self.idcinema = ""

        self.actionopen = ""
        self.actionclose = ""
        self.actionon = ""
        self.actionoff = ""
        self.actionorange = ""
        self.actionred = ""
        self.actiongreen = ""
        self.actionblue = ""
        self.actioncinema = ""

        # This method loads the files needed for the skill's functioning, and
        # creates and registers each intent that the skill uses

    def initialize(self):
        self.load_data_files(dirname(__file__))

        all_open_intent = IntentBuilder("AlfredAllOpenIntent").require("Open").build()
        self.register_intent(all_open_intent, self.handle_all_open_intent)

        all_close_intent = IntentBuilder("AlfredAllCloseIntent").require("Close").build()
        self.register_intent(all_close_intent, self.handle_all_close_intent)

        all_white_intent = IntentBuilder("AlfredAllWhiteIntent").require("White").build()
        self.register_intent(all_white_intent, self.handle_all_white_intent)

        all_black_intent = IntentBuilder("AlfredAllBlackIntent").require("Black").build()
        self.register_intent(all_black_intent, self.handle_all_black_intent)

        all_orange_intent = IntentBuilder("AlfredAllOrangeIntent").require("Orange").build()
        self.register_intent(all_orange_intent, self.handle_all_orange_intent)

        all_red_intent = IntentBuilder("AlfredAllRedIntent").require("Red").build()
        self.register_intent(all_red_intent, self.handle_all_red_intent)

        all_green_intent = IntentBuilder("AlfredAllGreenIntent").require("Green").build()
        self.register_intent(all_green_intent, self.handle_all_green_intent)

        all_blue_intent = IntentBuilder("AlfredAllBlueIntent").require("Blue").build()
        self.register_intent(all_blue_intent, self.handle_all_blue_intent)

        all_cinema_intent = IntentBuilder("AlfredCinemaIntent").require("Cinema").build()
        self.register_intent(all_cinema_intent, self.handle_cinema_intent)

        self.apikey = self.settings['apikey']
        print('apikey equals ' + self.apikey)
        self.jeedomaddress = self.settings['jeedomaddress']
        print('jeedomaddress equals ' + self.jeedomaddress)

        self.idopen = self.settings['idopen']
        self.idclose = self.settings['idclose']
        self.idon = self.settings['idon']
        self.idoff = self.settings['idoff']
        self.idorange = self.settings['idorange']
        self.idred = self.settings['idred']
        self.idgreen = self.settings['idgreen']
        self.idblue = self.settings['idblue']
        self.idcinema = self.settings['idcinema']

        self.actionopen = self.settings['actionopen']
        self.actionclose = self.settings['actionclose']
        self.actionon = self.settings['actionon']
        self.actionoff = self.settings['actionoff']
        self.actionorange = self.settings['actionorange']
        self.actionred = self.settings['actionred']
        self.actiongreen = self.settings['actiongreen']
        self.actionblue = self.settings['actionblue']
        self.actioncinema = self.settings['actioncinema']

    def handle_all_open_intent(self, message):
        self.call_jeedom(self.idopen, self.actionopen)

    def handle_all_close_intent(self, message):
        self.call_jeedom(self.idclose, self.actionclose)

    def handle_all_white_intent(self, message):
        self.call_jeedom(self.idon, self.actionon)

    def handle_all_black_intent(self, message):
        self.call_jeedom(self.idoff, self.actionoff)

    def handle_all_orange_intent(self, message):
        self.call_jeedom(self.idorange, self.actionorange)

    def handle_all_red_intent(self, message):
        self.call_jeedom(self.idred, self.actionred)

    def handle_all_green_intent(self, message):
        self.call_jeedom(self.idgreen, self.actiongreen)

    def handle_all_blue_intent(self, message):
        self.call_jeedom(self.idblue, self.actionblue)

    def handle_cinema_intent(self, message):
        self.call_jeedom(self.idcinema, self.actioncinema)

    def call_jeedom(self, action_id, action):
        urllib.request.urlopen("{}/core/api/jeeApi.php?apikey={}&type=scenario&id={}&action={}".format(
                self.jeedomaddress, self.apikey, action_id, action))

    def stop(self):
        pass


def create_skill():
    return AlfredSkill()
