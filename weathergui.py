import tkinter as tk
from tkinter import font

import requests

HEIGHT = 700
WIDTH = 800

def test_function(entry):
    print("This is the entry:", entry)

def format_response(weather):
    try:
        name = weather['name']
        des=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s \nCondition:%s \nTemperature(C):%s'% (name,des,temp)
    except:
        final_str='There is problem finding the data'
    return final_str   



def get_weather(city):
    weather_key = '3ed771e7e5404da54d5e278c1ccbdbcc'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q':city,'units':'metric'}
    response=requests.get(url,params=params)
    weather=response.json()

    label['text']=format_response(weather)

   
root = tk.Tk()
canvas  = tk.Canvas(root,height =HEIGHT,width = WIDTH )
canvas.pack()

background_image=tk.PhotoImage(file='landscape.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg= "#03b6fc",bd=5)
frame.place(relx = 0.5,rely = 0.1,relwidth =0.75,relheight = 0.1,anchor = 'n')


entry = tk.Entry(frame, font=('courier',20))
entry.place(relwidth = 0.65,relheight=1)

button = tk.Button(frame, text= "Get weather", font =('courier',20), command=lambda: get_weather(entry.get()))
button.place(relx = 0.7,relheight=1, relwidth =0.3)


lower_frame = tk.Frame(root,bg="#03b6fc",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,font=('courier',25),anchor='nw',justify='left', bd=4 )
label.place(relwidth=1,relheight=1)

root.mainloop()
