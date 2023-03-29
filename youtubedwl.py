import tkinter as tk
from tkinter import messagebox, simpledialog
from pytube import YouTube
from threading import Thread
from tkinter import ttk

def download_video():
    url = input_url.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        title = yt.title
        filesize = stream.filesize
        stream.download(filename="video")
        messagebox.showinfo("Download completo", f"O vídeo {title} foi baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download do vídeo.\n\n{str(e)}")
    
def update_progress_bar(progress, progress_bar):
    while progress < 100:
        progress_bar["value"] = progress
        progress += 1

# janela principal
root = tk.Tk()
root.title("Download de vídeos do YouTube")

#  widgets da janela
label_url = tk.Label(root, text="URL do vídeo:")
input_url = tk.Entry(root)
button_download = tk.Button(root, text="Baixar vídeo", command=lambda: Thread(target=download_video).start())
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")

#  widgets na janela
label_url.pack()
input_url.pack()
button_download.pack()
progress_bar.pack()

# Iniciar a janela
root.mainloop()



