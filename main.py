import os
import gdown
import customtkinter as ctk
from PIL import Image
import pandas as pd

url = "https://drive.google.com/uc?id=1g_zZs-URqAOJ8lMPP6fCofLmPQvidkLdBVpzZX1dkPE"
output = "downloaded_file.xlsx"
gdown.download(url, output, quiet=False)

df = pd.read_excel(output)
os.remove(output)

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("GenZ Library")
app.config(bg="#121824")
app.geometry("900x500")
app.resizable(False, False)

title_label = ctk.CTkLabel(app,
                           text="GenZ Library",
                           font=("Lavishly Yours", 64),
                           bg_color="#121824")
title_label.pack(pady=10)

search_entry = ctk.CTkEntry(app,
                            font=("Ovo", 28),
                            width=300, height=38,
                            placeholder_text="Enter word",
                            bg_color="#121824",
                            fg_color="#121824",
                            border_width=1,
                            border_color="#B3AAE2")
search_entry.place(x=233, y=155)

search_button = ctk.CTkButton(app,
                              font=("Ovo", 28),
                              text="Search",
                              command=lambda: search_word(),
                              fg_color="#B3AAE2",
                              text_color="#121824")
search_button.place(x=546, y=155)

meaning_label = ctk.CTkLabel(app,
                             text="Meaning:",
                             font=("Ovo", 28),
                             bg_color="#121824",
                             text_color="#B3AAE2")
meaning_label.place(x=233, y=230)

search_dis = ctk.CTkTextbox(app,
                            font=("Ovo", 16),
                            width=450,
                            height=130,
                            fg_color="#121824",
                            border_width=1,
                            border_color="#B3AAE2")
search_dis.place(x=233, y=265)

image_path1 = "elements/Group 15.png"
png_image1 = ctk.CTkImage(dark_image=Image.open(image_path1),
                          size=(200, 200))
image_label1 = ctk.CTkLabel(app,
                            image=png_image1,
                            text="",
                            bg_color="#121824")
image_label1.place(x=0, y=0)

image_path2 = "elements/Group 2.png"
png_image2 = ctk.CTkImage(dark_image=Image.open(image_path2),
                          size=(30, 110))
image_label2 = ctk.CTkLabel(app,
                            image=png_image2,
                            text="",
                            bg_color="#121824")
image_label2.place(x=820, y=360)


def search_word():
    word = search_entry.get()
    meaning = df.loc[df['Terms'].str.lower() == word.lower(), 'Meaning']
    if not meaning.empty:
        search_dis.delete("1.0", ctk.END)
        search_dis.insert(ctk.END, meaning.iloc[0])
    else:
        search_dis.delete("1.0", ctk.END)
        search_dis.insert(ctk.END, "Term not found.")


app.mainloop()