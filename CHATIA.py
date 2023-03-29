from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot('MeuBot')
bot.set_trainer(ListTrainer)
bot.train(['Olá!', 'Olá, como posso ajudar?', 'Qual é o seu nome?', 'Meu nome é MeuBot'])

janela = Tk()
janela.geometry('400x500')
janela.title('ChatBot')

texto_chat = Text(janela, bd=1, bg='white', height='8', width='50', font=('Arial', 16))
texto_chat.place(x=6, y=6, height=385, width=385)

entrada = Entry(janela, bd=0, bg='white', font=('Arial', 16))
entrada.place(x=6, y=400, height=50, width=320)

def enviar_mensagem():
    pergunta = entrada.get()
    resposta = bot.get_response(pergunta)
    texto_chat.insert(END, "Você: " + pergunta + '\n\n')
    texto_chat.insert(END, "Bot: " + str(resposta) + '\n\n')
    entrada.delete(0, END)

botao_enviar = Button(janela, font=('Arial', 16), text='Enviar', width='8', height='2', bg='gray', command=enviar_mensagem)
botao_enviar.place(x=330, y=400, height=50)

janela.mainloop()
