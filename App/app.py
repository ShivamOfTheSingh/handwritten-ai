from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Quad
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import rgba
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.uix.popup import Popup
import cv2 as cv
import tensorflow as tf
import numpy as np
import data_prep as dp




# drawInput is what makes the line appear when clicked on
class DrawInput(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (640, 832)
        with self.canvas.before:
            Color(1,1,1,1)
            self.bg_quad = Quad(points= [0,0,0,0,0,0,0, 0])
        self.bind(size = self.on_size)
    def on_size(self, *args):
        self.bg_quad.points = [self.x, self.y, self.right, self.y, self.right, self.top, self.x, self.top]
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(0,0,0,1)
            touch.ud["line"] = Line(points=(touch.x, touch.y), width = 45)       # width increase the stroke of the line
    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)
    
    def on_touch_up(self, touch):
        print("RELEASED!", touch) 

class PredictionPopup(Popup):
    def __init__(self, prediction, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        content = Label(text = f'AI PREDICTION: {prediction} ')
        layout.add_widget(content)
        close = Button(text = 'X', size_hint= (1,0.2))
        close.bind(on_press = self.dismiss)
        layout.add_widget(close)

        self.content = layout
        self.size_hint = (0.5,0.5)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.title = 'PREDICTION'
        self.auto_dismiss = False
        

class AIHelper(App):
    def build(self):                                                 #holds all the widgets inside the main canvas page

        layout = BoxLayout(orientation= 'vertical')


        title = Label(text='Draw Number or Letter', size_hint=(1,0.1))
        layout.add_widget(title)

        canvas = DrawInput()
        layout.add_widget(canvas)
        

        refresh = Button(text = 'Restart', size_hint = (1,0.1))
        refresh.bind(on_press=self.refreshCanvas)
        layout.add_widget(refresh)

        submit = Button(text = 'Submit', size_hint = (1,0.1))
        submit.bind(on_press = self.submitCanvas)
        submit.background_color = rgba(109, 205, 109)
        layout.add_widget(submit)

        return layout
    

    def refreshCanvas(self, instance):                  #after button is pressed this refreshes the canvas
        self.root.children[2].canvas.clear()
    def submitCanvas(self, instance):
        self.root.children[2].export_to_png('./App/img.png', size =(64,64)) # the submit button turns it into a png
        model = tf.keras.models.load_model('model')
        X = []
        img_arr = cv.imread('./App/img.png', cv.IMREAD_GRAYSCALE)
        new_arr = cv.resize(img_arr, (64, 64))
        X.append(new_arr)
        X = np.array(X)
        X = X.reshape(-1, 64, 64)
        X = tf.keras.utils.normalize(X, axis=1)
        prediction = dp.Ascii2Char(dp.getLabel(np.argmax(model.predict(X))))
        popup = PredictionPopup(prediction)
        popup.open()


if __name__ == "__main__": #main source that runs
    app = AIHelper()
    app.run()


