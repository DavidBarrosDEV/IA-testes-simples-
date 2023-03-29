from tkinter import *
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

janela = Tk()
janela.geometry('400x500')
janela.title('IA que fala')

texto_falar = Entry(janela, font=('Arial', 16))
texto_falar.pack(pady=10)

botao_falar = Button(janela, font=('Arial', 16), text='Falar', width='8', height='2', bg='gray', command=lambda: falar(texto_falar.get()))
botao_falar.pack(pady=10)

janela.mainloop()
