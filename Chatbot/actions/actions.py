# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import reviews as rv

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionHelloWorld(Action):
    def __init__(self):
        print("Action Class created")
        self.db = rv.getDB()

    def name(self) -> Text:
        return "action_list"

    def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        s = rv.list_all_reviews(self.db)
        dispatcher.utter_message(text=s)

        return []



class Action5StarReview(Action):
    def __init__(self):
        print("Action Class created")
        self.db = rv.getDB()

    def name(self) -> Text:
        return "action_rating"

    def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        s = rv.find_a_rating(self.db, 5)
        dispatcher.utter_message(text=s)

        return []
