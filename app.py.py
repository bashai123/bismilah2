from kivy.app import App
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display

class BasmalaApp(App):
    def build(self):
        raw_text = "بسم الله الرحمن الرحيم"
        
        # Reshape and reorder the letters so they connect properly
        reshaped_text = arabic_reshaper.reshape(raw_text)
        display_text = get_display(reshaped_text)
        
        return Label(
            text=display_text,
            font_size='36sp',
            font_name='Amiri-Regular.ttf'  # <-- Matches your uploaded font exactly
        )

if __name__ == '__main__':
    BasmalaApp().run()
