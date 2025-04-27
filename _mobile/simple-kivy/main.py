from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text="Click me!")
        button.bind(on_press=self.say_hello)
        layout.add_widget(button)
        return layout

    def say_hello(self, instance):
        instance.text = "Hello Dee!"

if __name__ == "__main__":
    MyApp().run()
