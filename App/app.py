from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import rgba
from kivy.uix.image import Image



class Home(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = 'vertical'

        title = Label(text = 'AI Helper', size_hint=(1,0.1))
        self.add_widget(title)

        picture = Image(source = 'robot.png')                   
        self.add_widget(picture)                            # adds the picture to that page

        start = Button(text = 'Start', size_hint = (1,0.1))
        start.bind(on_press=self.next)
        self.add_widget(start)

        bottom = Widget(size_hint=(1,0.1))
        self.add_widget(bottom)
    def next(self, instance):                               # changes to the next page
        app.canvas_layer()

# drawInput is what makes the line appear when clicked on
class DrawInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y), width = 7)       # width increase the stroke of the line
    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)
    
    def on_touch_up(self, touch):
        print("RELEASED!", touch)           

    def returnHome():
        app.home_layer()               

class AIHelper(App):
    def build(self):
        self.home = Home()
        return self.home
    
    def canvas_layer(self):                                             #holds all the widgets inside the main canvas page
        layout = BoxLayout(orientation= 'vertical')

        title = Label(text='Draw Number or Letter', size_hint=(1,0.1))
        layout.add_widget(title)

        canvas = DrawInput()
        layout.add_widget(canvas)
        

        refresh = Button(text = 'Restart', size_hint = (1,0.1))
        refresh.bind(on_press=self.refreshCanvas)
        layout.add_widget(refresh)

        submit = Button(text = 'Submit', size_hint = (1,0.1))
        submit.background_color = rgba(109, 205, 109)
        layout.add_widget(submit)

        self.canvas =layout
        self.root.clear_widgets()
        self.root.add_widget(layout)
        
    def home_layer(self):                                   
        self.root.clear_widgets()
        self.build()

    def refreshCanvas(self, instance):                  #after button is pressed this refreshes the canvas
        self.canvas_layer()
    def submitCanvas(self, instance):
        self.root.children[2].export_to_png('canvas.png') # the submit button turns it into a png

if __name__ == "__main__": #main source that runs
    app = AIHelper()
    app.run()








# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button

# class childApp(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text = 'Student Name'))
#         self.s_name = TextInput()
#         self.add_widget(self.s_name)

#         self.add_widget(Label(text = 'Student Marks'))
#         self.s_marks = TextInput()
#         self.add_widget(self.s_marks)

#         self.add_widget(Label(text = 'Student Gender'))
#         self.s_gender = TextInput()
#         self.add_widget(self.s_gender)
# class parentApp(App):
#     def build(self):
#         return childApp()
# if __name__ == "__main__":
#     parentApp().run()