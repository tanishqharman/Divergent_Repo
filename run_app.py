from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent 
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-456959321428-457132279874-457101819555-32d6e0ad30802b376a267e58b9f507e9', 
							'xoxb-456959321428-456456818416-4WzFxxER9ueWGgYBssac7SNY',
                            'yFyb4p9S9h5ZRea2cqhkEWld',
                            True
	                       )

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
