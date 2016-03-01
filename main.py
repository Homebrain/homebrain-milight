import milight as mi

from homebrain import Agent

class MiLight(Agent):
    def __init__(self):
        super(MiLight, self).__init__()

    def handle_event(self, event):
        print(event)




