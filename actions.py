from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    def name(self):
    	return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key =  'd0db3e9a32b342e080a191744181510'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name'] 
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_kph = current['current']['wind_kph']	

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} kph.""".format(condition, city, temperature_c, humidity, wind_kph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]


