from mycroft import MycroftSkill, intent_file_handler


class WhatAreYouMadeOf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('of.made.you.are.what.intent')
    def handle_of_made_you_are_what(self, message):
        self.speak_dialog('of.made.you.are.what')


def create_skill():
    return WhatAreYouMadeOf()

