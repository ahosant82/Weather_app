# weather app implemention
from os import readlink
import tkinter as tk
from tkinter import Button, font
from tkinter.constants import ANCHOR
from PIL import Image, ImageTk
from weather_api import weather_information


def open_weather_icon(icon):
    size= int(info_frame.winfo_height()*0.30)
    img= ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor= 'nw', image= img)
    weather_icon.image= img


#
def get_weather_info(city_name):
    # set weather informetion
    weather_report = weather_information(city_name)
    result['text'] = weather_report[0]
    weather_icon_name= weather_report[1]
    open_weather_icon(weather_icon_name)

# besic settings of app eindow
app= tk.Tk()
cenvas=tk.Canvas(width=700, height=600)
cenvas.pack()
app.resizable(False, False)
app.title('Weather App')

#set background imagess
background_img= tk.PhotoImage(file='background_image.png')
background_label= tk.Label(app, image=background_img)
background_label.place(relheight=1, relwidth=1)

#heading of the app
heading= tk.Label(app,
        text='Weather Informetion',
        font=('Comic Sans MS', 25, 'bold'),
        bg='#ffff99',
        bd=5
        )
heading.place(relwidth=1)

# input frame
frame= tk.Frame(app, bg="#42c2f4", bd=5)
frame.place(x=100, y=80, relwidth=0.75, relheight=0.1)

#input text box
textbox= tk.Entry(frame, font=('Courier', 16))
textbox.place(relwidth=0.65, relheight=1)

# submit button
submit_button=tk.Button(frame,
    text='Search Weather',
    font=20,
    command=lambda: get_weather_info(textbox.get())
    )
submit_button.place(x=360, relwidth=0.3, relheight=1)

#informetion frame
info_frame= tk.Frame(app, bg='#42c2f4', bd=6)
info_frame.place(x=90, y=200, relwidth=0.75, relheight=0.55)

result= tk.Label(info_frame,
                    font=('Courier', 16),
                    anchor='nw',
                    justify='left',
                    bg="#fff",
                    bd=4)
result.place(relwidth=1, relheight=1)


#icon
weather_icon= tk.Canvas(result, bg="#ddd" , bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=0.5, relheight=0.5)

#run tk inter
app.mainloop()