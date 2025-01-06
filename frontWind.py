import customtkinter as ctk
import subprocess 
from my_class import *

# Создаем главное окно приложения
root = ctk.CTk()
root.geometry("360x640")
root.title("MyTamagochi")
root.resizable(False, False)


backgr = ctk.CTkFrame(master = root, width = 360, height = 640, fg_color="black")
backgr.pack(fill ="both", expand= True)


frame1 = ctk.CTkFrame(master=backgr, fg_color="white", corner_radius=5)
frame1.pack(pady=(100, 20))

label1 = ctk.CTkLabel(master=frame1, text="TAMAGOCHI", text_color="black", font=("", 20, "bold"))
label1.pack(pady=(5,2), padx=6) 

frame2 = ctk.CTkFrame(master=backgr, fg_color="white", corner_radius=5)
frame2.pack(pady=(30,15))

label2 = ctk.CTkLabel(master=frame2, text="Type a name for your pet", text_color="black", font=("", 16, "bold"))
label2.pack(pady=(1,0), padx=5) 

entry1 = ctk.CTkEntry(master = backgr, placeholder_text="Enter:",font= ("Arial",16),placeholder_text_color= "white", border_color="red", width= 180, corner_radius=0)
entry1.pack(pady=5)




frame3 = ctk.CTkFrame(master = backgr, fg_color="white", corner_radius=5)
frame3.pack(pady=(15))

label3 = ctk.CTkLabel(master=frame3, text="Choose type", text_color="black", font =("", 16, "bold"))
label3.pack(pady = (1,0), padx = 5)

entry2 = ctk.CTkEntry(master = backgr, placeholder_text="Enter:",font= ("Arial",16),placeholder_text_color= "white", border_color="red", width= 180, corner_radius=0)
entry2.pack(pady=5)

def open_second_window():
    subprocess.Popen(["python", "backWind.py"])

buttonplay = ctk.CTkButton(command=open_second_window,master=backgr, text="GET TAMAGOCHI", fg_color="#0FDE23", text_color="white", corner_radius=50, height=70, font=("Lato", 15, "bold"),hover_color="#0E8144")
buttonplay.pack(pady=20, padx = 60)  

root.mainloop()


