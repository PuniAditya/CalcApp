from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
import string
import json

class MyApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical',spacing = 0,padding = 100)
        self.str = '_'
        self.angle_mode = 1
        # self.lcd = Label(text = 'DISPLAY HERE' , halign='left' , valign = 'middle')
        # self.lcd = Label(text='DISPLAY HERE', halign='right', valign='middle'); self.lcd.bind(size=lambda *_: setattr(self.lcd, 'text_size', self.lcd.size))
        self.lcd = Label(text='DISPLAY HERE', font_size=40, halign='right', valign='middle'); self.lcd.bind(size=lambda *_: setattr(self.lcd, 'text_size', self.lcd.size))
        self.lcd.bind(size=lambda *_: setattr(self.lcd, 'text_size', self.lcd.size))

        self.shift = ToggleButton(text = 'Shift', state = "normal" , color =(1,1,0,1))
        
        self.btn12 = Button(text = 'e^x') #log 
        self.btn13 = Button(text = '1' , background_color=(1, 1, 0, 1))
        self.btn14 = Button(text = '2', background_color=(1, 1, 0, 1))
        self.btn15 = Button(text = '3' , background_color=(1, 1, 0, 1))
        
        self.btn21 = Button(text = 'sin') #sin^-1
        self.btn22 = Button(text = '\u221a') #a^b
        self.btn23 = Button(text='4', background_color=(1, 1, 0, 1))
        self.btn24 = Button(text='5', background_color=(1, 1, 0, 1))
        self.btn25 = Button(text='6', background_color=(1, 1, 0, 1))

        self.btn31 = Button(text='cos') #cos^-1
        self.btn32 = Button(text='Radian') #degree
        self.btn33 = Button(text='7', background_color=(1, 1, 0, 1))
        self.btn34 = Button(text='8', background_color=(1, 1, 0, 1))
        self.btn35 = Button(text='9', background_color=(1, 1, 0, 1))

        self.btn41 = Button(text='tan') #tan^-1
        self.btn42 = Button(text='+') # -
        self.btn43 = Button(text='×') # / 
        self.btn44 = Button(text='0', background_color=(1, 1, 0, 1))
        self.btn45 = Button(text='=')

        self.btn51 = Button(text='π') # e 
        self.btn52 = Button(text='(')
        self.btn53 = Button(text=')')
        self.btn54 = Button(text='DEL', background_color=(0, 1, 1, 1))
        self.btn55 = Button(text='AC', background_color=(0, 1, 1, 1))

        #connecting keyboard
        Window.bind(on_key_down=self.on_key_down)
        
        self.shift.bind(on_press=self.btnshift)
        
        self.btn12.bind(on_press=self.btn12p)
        self.btn13.bind(on_press=self.btn13p)
        self.btn14.bind(on_press=self.btn14p)
        self.btn15.bind(on_press=self.btn15p)

        self.btn21.bind(on_press=self.btn21p)
        self.btn22.bind(on_press=self.btn22p)
        self.btn23.bind(on_press=self.btn23p)
        self.btn24.bind(on_press=self.btn24p)
        self.btn25.bind(on_press=self.btn25p)

        self.btn31.bind(on_press=self.btn31p)
        self.btn32.bind(on_press=self.btn32p)
        self.btn33.bind(on_press=self.btn33p)
        self.btn34.bind(on_press=self.btn34p)
        self.btn35.bind(on_press=self.btn35p)

        self.btn41.bind(on_press=self.btn41p)
        self.btn42.bind(on_press=self.btn42p)
        self.btn43.bind(on_press=self.btn43p)
        self.btn44.bind(on_press=self.btn44p)
        self.btn45.bind(on_press=self.btn45p)

        self.btn51.bind(on_press=self.btn51p)
        self.btn52.bind(on_press=self.btn52p)
        self.btn53.bind(on_press=self.btn53p)
        self.btn54.bind(on_press=self.btn54p)
        self.btn55.bind(on_press=self.btn55p)


        
        row1 = BoxLayout(orientation = 'horizontal',spacing = 0 , padding = 0)
        row1.add_widget(self.shift)
        row1.add_widget(self.btn12)
        row1.add_widget(self.btn13)
        row1.add_widget(self.btn14)
        row1.add_widget(self.btn15)

        row2 = BoxLayout(orientation='horizontal', spacing=0, padding=0)
        row2.add_widget(self.btn21)
        row2.add_widget(self.btn22)
        row2.add_widget(self.btn23)
        row2.add_widget(self.btn24)
        row2.add_widget(self.btn25)

        row3 = BoxLayout(orientation='horizontal', spacing=0, padding=0)
        row3.add_widget(self.btn31)
        row3.add_widget(self.btn32)
        row3.add_widget(self.btn33)
        row3.add_widget(self.btn34)
        row3.add_widget(self.btn35)

        row4 = BoxLayout(orientation='horizontal', spacing=0, padding=0)
        row4.add_widget(self.btn41)
        row4.add_widget(self.btn42)
        row4.add_widget(self.btn43)
        row4.add_widget(self.btn44)
        row4.add_widget(self.btn45)

        row5 = BoxLayout(orientation='horizontal', spacing=0, padding=0)
        row5.add_widget(self.btn51)
        row5.add_widget(self.btn52)
        row5.add_widget(self.btn53)
        row5.add_widget(self.btn54)
        row5.add_widget(self.btn55)
        
        layout.add_widget(self.lcd)
        layout.add_widget(row1)
        layout.add_widget(row2)
        layout.add_widget(row3)
        layout.add_widget(row4)
        layout.add_widget(row5)
        return layout

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
    #     if codepoint in '1234567890+-/e().':
    #         self.rep(codepoint)
    #         self.lcd.text = self.str
    #     if codepoint == '*':
    #         self.rep('×')
    #         self.lcd.text = self.str
        # -------- BACKSPACE --------
        if key == 8:   # Backspace key
            self.btn54p(None)
            return True

        if key == 13 or key == 271:
            self.btn45p(None) # Call '='
            return True
        
        if key == 27: #esc to clear
            self.btn55p(None)
            return True

        #left arrow
        if key == 276:
            self.btn52s(None) 
            return True

        #right arrow
        if key == 275:
            self.btn53s(None) 
            return True

        if codepoint:# -------- NORMAL INPUT --------
            if codepoint in '1234567890+-*/e().':
                self.rep(codepoint)
                self.lcd.text = self.str
    
    def rep(self,temp):
        self.str = self.str.replace('_',temp+'_')
        # self.lcd.text = self.str

    def btnshift(self, instance):
        if instance.state == "down":
            instance.color = (0, 0, 0, 1)
            
            # Update Button Text
            self.btn12.text = 'log'
            self.btn21.text = 'sin-1'
            self.btn22.text = 'a^b'
            self.btn32.text = 'Degree'
            self.btn31.text = 'cos-1'
            self.btn41.text = 'tan-1'
            self.btn51.text = 'e'
            self.btn42.text = '-'
            self.btn43.text = '÷'
            self.btn52.text = '<-'
            self.btn53.text = '->'
            self.btn55.text = '.'  # Change AC to .

            # UNBIND Primary Functions (p)
            self.btn12.unbind(on_press=self.btn12p)
            self.btn21.unbind(on_press=self.btn21p)
            self.btn22.unbind(on_press=self.btn22p)
            self.btn32.unbind(on_press=self.btn32p)
            self.btn31.unbind(on_press=self.btn31p)
            self.btn41.unbind(on_press=self.btn41p)
            self.btn51.unbind(on_press=self.btn51p)
            self.btn42.unbind(on_press=self.btn42p)
            self.btn43.unbind(on_press=self.btn43p)
            self.btn52.unbind(on_press=self.btn52p)
            self.btn53.unbind(on_press=self.btn53p) # Fix: Unbind 53 from 53p
            self.btn55.unbind(on_press=self.btn55p) # Fix: Unbind 55 from 55p

            # BIND Secondary Functions (s)
            self.btn12.bind(on_press=self.btn12s)
            self.btn21.bind(on_press=self.btn21s)
            self.btn22.bind(on_press=self.btn22s)
            self.btn32.bind(on_press=self.btn32s)
            self.btn31.bind(on_press=self.btn31s)
            self.btn41.bind(on_press=self.btn41s)
            self.btn51.bind(on_press=self.btn51s)
            self.btn42.bind(on_press=self.btn42s)
            self.btn43.bind(on_press=self.btn43s)
            self.btn52.bind(on_press=self.btn52s)
            self.btn53.bind(on_press=self.btn53s) # Fix: Bind 53 to 53s
            self.btn55.bind(on_press=self.btn55s) # Fix: Bind 55 to 55s

        else:
            instance.color = (1, 1, 0, 1)
            
            # Revert Button Text
            self.btn12.text = 'e^x'
            self.btn21.text = 'sin'
            self.btn22.text = '\u221a'
            self.btn32.text = 'Radian'
            self.btn31.text = 'cos'
            self.btn41.text = 'tan'
            self.btn51.text = 'π'
            self.btn42.text = '+'
            self.btn43.text = '×'
            self.btn52.text = '('
            self.btn53.text = ')'
            self.btn55.text = 'AC' # Revert . to AC

            # UNBIND Secondary Functions (s)
            self.btn12.unbind(on_press=self.btn12s)
            self.btn21.unbind(on_press=self.btn21s)
            self.btn22.unbind(on_press=self.btn22s)
            self.btn32.unbind(on_press=self.btn32s)
            self.btn31.unbind(on_press=self.btn31s)
            self.btn41.unbind(on_press=self.btn41s)
            self.btn51.unbind(on_press=self.btn51s)
            self.btn42.unbind(on_press=self.btn42s)
            self.btn43.unbind(on_press=self.btn43s)
            self.btn52.unbind(on_press=self.btn52s)
            self.btn53.unbind(on_press=self.btn53s) # Fix: Unbind 53 from 53s
            self.btn55.unbind(on_press=self.btn55s) # Fix: Unbind 55 from 55s

            # BIND Primary Functions (p)
            self.btn12.bind(on_press=self.btn12p)
            self.btn21.bind(on_press=self.btn21p)
            self.btn22.bind(on_press=self.btn22p)
            self.btn32.bind(on_press=self.btn32p)
            self.btn31.bind(on_press=self.btn31p)
            self.btn41.bind(on_press=self.btn41p)
            self.btn51.bind(on_press=self.btn51p)
            self.btn42.bind(on_press=self.btn42p)
            self.btn43.bind(on_press=self.btn43p)
            self.btn52.bind(on_press=self.btn52p)
            self.btn53.bind(on_press=self.btn53p) # Fix: Bind 53 to 53p
            self.btn55.bind(on_press=self.btn55p) # Fix: Bind 55 to 55p           

    ###########################################
    # NON - MULTI FUNCTIONAL KEYS             #
    ###########################################
    
    def btn13p(self, instance):
        self.rep( '1')
        self.lcd.text = self.str

    def btn14p(self, instance):
        self.rep(  '2')
        self.lcd.text = self.str

    def btn15p(self, instance):
        self.rep(  '3')
        self.lcd.text = self.str

    def btn23p(self, instance):
        self.rep(  '4')
        self.lcd.text = self.str

    def btn24p(self, instance):
        self.rep(  '5')
        self.lcd.text = self.str

    def btn25p(self, instance):
        self.rep(  '6')
        self.lcd.text = self.str

    def btn33p(self, instance):
        self.rep(  '7')
        self.lcd.text = self.str

    def btn34p(self, instance):
        self.rep(  '8')
        self.lcd.text = self.str

    def btn35p(self, instance):
        self.rep(  '9')
        self.lcd.text = self.str

    def btn44p(self, instance):
        self.rep(  '0')
        self.lcd.text = self.str

    # DEL
    def btn54p(self,instance):
        loc = self.str.find('_')
        if loc != -1:
            if len(self.str) > 1 :
                self.str = self.str[:loc-1] + self.str[loc:]
                self.lcd.text = self.str
    # =
    def btn45p(self,instance):
        self.lcd.text = "Calculating..."
        eqn = self.str.replace('_','')
        if self.angle_mode == 1 :
            mode = ''
        else:
            mode = 'deg'
        data = json.dumps({'evaluate':eqn , 'angle':mode})

        headers = {'Content-Type': 'application/json'}

        UrlRequest(
            url='http://127.0.0.1:8000/endpoint',
            req_body = data,
            req_headers = headers,
            on_success= self.on_success,
            on_failure= self.on_failure,
            on_error=self.on_error
        )
    
    def on_success(self, request, result):
        # print(result)

        if isinstance(result, dict):
            answer = result.get('result', str(result))  # adjust 'result' to match your server's response key
        else:
            answer = str(result)
        
        self.str = str(answer) + '_'
        self.lcd.text = self.str
    
    def on_failure(self, request, result):
        self.lcd.text = f'Error: {result}'
        # print(f"Request failed: {result}")
        
    def on_error(self, request , error):
        self.lcd.text = 'No Connection!'
        # print(f"Connection error: {error}")

    ###########################################
    # MULTI FUNCTIONAL KEYS                   #
    ###########################################
    
    def btn12p(self, instance):
        self.rep('e^(')
        self.lcd.text = self.str

    def btn12s(self, instance):
        self.rep('log(')
        self.lcd.text = self.str

    def btn21p(self, instance):
        self.rep('sin(')
        self.lcd.text = self.str

    def btn21s(self, instance):
        self.rep('asin(')
        self.lcd.text = self.str

    def btn22p(self, instance):
        self.rep('sqrt(')
        self.lcd.text = self.str

    def btn22s(self, instance):
        self.rep('^(')
        self.lcd.text = self.str

    def btn31p(self, instance):
        self.rep('cos(')
        self.lcd.text = self.str

    def btn31s(self, instance):
        self.rep('acos(')
        self.lcd.text = self.str

    def btn32p(self, instance):
        self.angle_mode = 1

    def btn32s(self, instance):
        self.angle_mode = 0

    def btn41p(self, instance):
        self.rep('tan(')
        self.lcd.text = self.str

    def btn41s(self, instance):
        self.rep('atan(')
        self.lcd.text = self.str

    def btn42p(self, instance):
        self.rep('+')
        self.lcd.text = self.str

    def btn42s(self, instance):
        self.rep('-')
        self.lcd.text = self.str

    def btn43p(self, instance):
        self.rep('*')
        self.lcd.text = self.str

    def btn43s(self, instance):
        self.rep('/')
        self.lcd.text = self.str

    def btn51p(self, instance):
        self.rep('pi')
        self.lcd.text = self.str

    def btn51s(self, instance):
        self.rep('e')
        self.lcd.text = self.str

    def btn52p(self,instance):
        self.rep('(')
        # self.str += '(_'
        self.lcd.text = self.str
    
    def btn53p(self,instance):
        self.rep(')')
        self.lcd.text = self.str

    def btn52s(self, instance):
        temp = self.str.find('_')
        if temp > 0:   # ensures there IS a previous character
            self.str = (self.str[:temp-1] + '_' + self.str[temp-1] +self.str[temp+1:])
        self.lcd.text = self.str

    def btn53s(self, instance):
        temp = self.str.find('_')
        if temp != -1 and temp < len(self.str) - 1:
            self.str = (self.str[:temp] + self.str[temp+1] + '_' + self.str[temp+2:])
        self.lcd.text = self.str
    
    def btn55p(self,instance):
        self.str = '_'
        self.lcd.text = self.str
    
    def btn55s(self,instance):
        self.rep('.')
        self.lcd.text = self.str
   
MyApp().run()





'''

    def btn13p(self,instance):
        self.str = self.str[:-1]
        self.str += '1_'
        self.lcd.text = self.str
    def btn14p(self,instance):
        self.str = self.str[:-1]
        self.str += '2_'
        self.lcd.text = self.str
    def btn15p(self,instance):
        self.str = self.str[:-1]
        self.str += '3_'
        self.lcd.text = self.str
    
    def btn23p(self,instance):
        self.str = self.str[:-1]
        self.str += '4_'
        self.lcd.text = self.str
    def btn24p(self,instance):
        self.str = self.str[:-1]
        self.str += '5_'
        self.lcd.text = self.str
    def btn25p(self,instance):
        self.str = self.str[:-1]
        self.str += '6_'
        self.lcd.text = self.str

    def btn33p(self,instance):
        self.str = self.str[:-1]
        self.str += '7_'
        self.lcd.text = self.str
    def btn34p(self,instance):
        self.str = self.str[:-1]
        self.str += '8_'
        self.lcd.text = self.str
    def btn35p(self,instance):
        self.str = self.str[:-1]
        self.str += '9_'
        self.lcd.text = self.str

    def btn44p(self,instance):
        self.str = self.str[:-1]
        self.str += '0_'
        self.lcd.text = self.str

    def btn52p(self,instance):
        self.str = self.str[:-1]
        self.str += '(_'
        self.lcd.text = self.str
    
    def btn53p(self,instance):
        self.str = self.str[:-1]
        self.str += ')_'
        self.lcd.text = self.str

        def btn12p(self,instance):
        self.str = self.str[:-1]
        self.str += 'e^(_'
        self.rep(self,'e^(_')
        self.lcd.text = self.str

    def btn12s(self,instance):
        self.str = self.str[:-1]
        self.str += 'log(_'
        self.lcd.text = self.str

    def btn21p(self,instance):
        self.str = self.str[:-1]
        self.str += 'sin(_'
        self.lcd.text = self.str
    
    def btn21s(self,instance):
        self.str = self.str[:-1]
        self.str += 'sin-1(_'
        self.lcd.text = self.str

    def btn22p(self,instance):
        self.str = self.str[:-1]
        self.str += 'rt(_'
        self.lcd.text = self.str

    def btn22s(self,instance):
        self.str = self.str[:-1]
        self.str += '^(_'
        self.lcd.text = self.str    

    def btn31p(self,instance):
        self.str = self.str[:-1]
        self.str += 'cos(_'
        self.lcd.text = self.str

    def btn31s(self,instance):
        self.str = self.str[:-1]
        self.str += 'cos-1(_'
        self.lcd.text = self.str

    def btn32p(self,instance):

        self.angle = 1 

    def btn32s(self,instance):
        self.angle_mode = 0

    def btn41p(self,instance):
        self.str = self.str[:-1]
        self.str += 'tan(_'
        self.lcd.text = self.str

    def btn41s(self,instance):
        self.str = self.str[:-1]
        self.str += 'tan-1(_'
        self.lcd.text = self.str
    
    def btn42p(self,instance):
        self.str = self.str[:-1]
        self.str += '+_'
        self.lcd.text = self.str

    def btn42s(self,instance):
        self.str = self.str[:-1]
        self.str += "-_"
        self.lcd.text = self.str 

    def btn43p(self,instance):
        self.str = self.str[:-1]
        self.str += '×_'
        self.lcd.text = self.str

    def btn43s(self,instance):
        self.str = self.str[:-1]
        self.str += '/_'
        self.lcd.text = self.str

    def btn51p(self,instance):
        self.str = self.str[:-1]
        self.str += 'π_'
        self.lcd.text = self.str

    def btn51s(self,instance):
        self.str = self.str[:-1]
        self.str += 'e_'
        self.lcd.text = self.str

'''



'''
Window.bind(on_key_down=self.on_key_down)

def on_key_down(self, window, key, scancode, codepoint, modifiers):
        if codepoint in '1234567890+-/e().':
            self.rep(codepoint)
            self.lcd.text = self.str
        if codepoint == '*':
            self.rep('×')
            self.lcd.text = self.str
'''










''' TO CHANGE TEXT ON A CLICK
 self.my_label = Label(text='Original Text')
        layout.add_widget(self.my_label)
        
        btn = Button(text='Change Text')
        btn.bind(on_press=self.change_text)
        layout.add_widget(btn)
        
        return layout
    
    def change_text(self, instance):
        self.my_label.text = 'Text Changed!'
'''

''' GETTING USER INPUT

from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.input_box = TextInput(hint_text='Type your name')
        layout.add_widget(self.input_box)
        
        btn = Button(text='Submit')
        btn.bind(on_press=self.show_name)
        layout.add_widget(btn)
        
        self.output = Label(text='Your name will appear here')
        layout.add_widget(self.output)
        
        return layout
    
    def show_name(self, instance):
        typed_text = self.input_box.text
        self.output.text = f'Hello, {typed_text}!'

MyApp().run()


'''

'''
self.btn13 = Button(text = '1' , background_color=(1, 1, 0, 1))
self.btn13.bind(on_press=self.btn13p)
def btn13p(self, instance):
        self.rep( '1')
        self.lcd.text = self.str
def rep(self,temp):
        self.str = self.str.replace('_',temp+'_')
        # self.lcd.text = self.str
'''
