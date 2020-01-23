from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Play'
            on_press:
                root.manager.transition.direction = 'down'
                root.manager.current = 'category'
        Button:
            text: 'Settings'
            on_press:
                root.manager.transition.direction = 'up'
                root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_press:
                app.stop()
<CategoryScreen>:
    BoxLayout:
        orientation: 'vertical'

        GridLayout:
            cols: 2
            Button:
                text: 'Category 1'
            Button:
                text: 'Category 2'
            Button:
                text: 'Category 3'
            Button:
                text: 'Category 4'
        Button:
            size_hint: 0.5, 0.2
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'up'
                root.manager.current = 'menu'
        
        
<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
""")

# Declare screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class CategoryScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=SlideTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(CategoryScreen(name='category'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()