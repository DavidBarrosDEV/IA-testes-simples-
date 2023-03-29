from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
import os
import tkinter as tk


bot = ChatBot('MeuBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.portuguese')


def get_audio_response(user_input):
    # Obtém a resposta do chatbot
    bot_response = bot.get_response(user_input)

    # Converte a resposta em um áudio utilizando o gTTS
    tts = gTTS(text=bot_response.text, lang='pt-br')
    tts.save('bot_response.mp3')

    # Toca o áudio
    os.system('mpg123 bot_response.mp3')


class ChatInterface(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.chatbot = bot
        self.master = master
        self.initialize_interface()

    def initialize_interface(self):
        self.master.title("Meu ChatBot")
        self.grid()

        self.message_listbox = tk.Listbox(self, height=15, width=50)
        self.message_listbox.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)

        self.message_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.message_listbox.yview)

        self.message_entry = tk.Entry(self, width=50)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self, text="Enviar", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.message_listbox.insert(tk.END, "Você: " + message)
        self.message_entry.delete(0, tk.END)

        # Obtém a resposta do chatbot e adiciona à lista de mensagens
        bot_response = self.chatbot.get_response(message)
        self.message_listbox.insert(tk.END, "Bot: " + str(bot_response))

        # Converte a resposta em áudio e toca
        get_audio_response(bot_response)

