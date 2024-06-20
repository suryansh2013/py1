from tkinter import *
import speech_recognition as sr
root =Tk()
root.geometry("800x600")
textarea = Text(root, height=10, wrap="char", width=50, padx=10, pady=5, bd=5, fg="blue", font=("times", 15, "bold"))
textarea.place(relx=0.5, rely=0.5, anchor=CENTER)
def r_audio():
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ""
        try:
            voice_data = speech_recognisor.recognize_google(audio, language="en-in")
        except:
            print("I did'nt get that. Could you please repeat again?")
        print(voice_data)
        textarea.insert(END, voice_data)
btn = Button(root, text="Click to say", fg="white", bg="maroon", font=("times", 20, "bold"), command=r_audio)
btn.place(relx=0.5, rely=0.1, anchor=CENTER)
root.mainloop()