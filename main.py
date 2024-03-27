import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate' , rate+10)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("welcome to third umpire decision review system")

stream = cv2.VideoCapture("clip_2.mp4")
def play(speed):
    print(f"you clicked on play.Speed is {speed}")

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    canvas.create_text(120, 25, fill="blue", font="Times 20 italic bold", text = "Decision Pending")

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("Pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW) 

    time.sleep(1) 

    frame = cv2.cvtColor(cv2.imread("Sponser.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW) 

    time.sleep(1.5)

    if decision =='out' :
        decisionImg = "Out.jpg"
        speak("The decision is on the way")
    else:
        decisionImg = "Not_Out.jpg"
        speak("the decision is on the way")  

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if decision=='out':
        speak(" and the player is out") 
    else:
        speak("and the player is not out")    



def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out.")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is Not Out.") 

def exit():
    speak("Exit from the review system")
    window.destroy()   



SET_WIDTH = 640
SET_HEIGHT = 360


window = tkinter.Tk()
window.title("Third Umpire decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("Welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img)) 
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()



btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -3))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 3))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" Give Out", width=50, command = out)
btn.pack()


btn = tkinter.Button(window, text=" Give Not Out", width=50, command = not_out)
btn.pack()

btn = tkinter.Button(window, text=" Exit" , width = 50 ,command = exit)
btn.pack()

window.mainloop()
