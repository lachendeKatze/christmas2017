# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft libraries
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.skills.audioservice import AudioService
from mycroft.util.log import getLogger

#required libraries
import datetime
import requests         # http library, no known relation to re :)

__author__ = 'GregV', '@lachendeKatze'

LOGGER = getLogger(__name__)

class DaysUntilChristmasSkill(MycroftSkill):
    def __init__(self):
        super(DaysUntilChristmasSkill, self).__init__(name="DaysUntilChristmasSkill")
	self.audio_service = None

    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.audio_service = AudioService(self.emitter)
	self.register_intent_file('days.until.christmas.intent',self.handle_christmas)

    def handle_christmas(self,message):
	
	today = datetime.date.today()
	christmasDay = datetime.date(today.year, 12, 25)
	
	# in datetime atimetic, if a day is in the past, it is 'negative' or less 
        # than today, or less than a day in the future
        # check to see if christmas is past :( if so, correct to next year :(
	if christmasDay < today:
		christmasDay = christmasDay.replace(year=today.year+1)
	
	daysUntilChristmas = abs(christmasDay -today)
	self.audio_service.play('file//./music/carol_of_bells.mp3')
	self.speak("there are " + str(daysUntilChristmas.days) + " days until christmas")
	
    def stop(self):
	pass

def create_skill():
	return DaysUntilChristmasSkill()
		
