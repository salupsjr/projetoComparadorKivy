from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (14 / 255, 61 / 255, 76 / 255, 0.5)
Window.size = (400, 700)


class Comp(BoxLayout):
    def calc(self):
        pr1 = float(self.ids.pr1.text)
        ps1 = float(self.ids.ps1.text)
        pr2 = float(self.ids.pr2.text)
        ps2 = float(self.ids.ps2.text)

        self.ids.p1.text = str(pr1 / ps1 * 1000)
        self.ids.p2.text = str(pr2 / ps2 * 1000)

        self.ids.dif.text = str((pr1 / ps1) / (pr2 / ps2) * 100) + ' %'


class Comparador(App):
    def build(self):
        return Comp()


Comparador().run()
