import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class PageLayout(PageLayout):
    pass
class PageLayoutApp(App):
    def build(self):
        return PageLayout()


plApp = PageLayoutApp()
plApp.run()