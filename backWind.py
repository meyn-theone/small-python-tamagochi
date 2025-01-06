import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.title("Тамагочи")
app.geometry("600x600")


framebg = ctk.CTkFrame(master= app,  fg_color="black")
framebg.pack(fill = "both", expand = True)

cmdFrame = ctk.CTkFrame(master= framebg, fg_color="black" )
cmdFrame.pack(pady = 5, fill ="both")

feedbutt = ctk.CTkButton(master = cmdFrame, text= "Feed", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")
playbutt = ctk.CTkButton(master = cmdFrame, text= "Play", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")
sleepbutt = ctk.CTkButton(master = cmdFrame, text= "sleep", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144" )
cleanbutt = ctk.CTkButton(master = cmdFrame, text= "clean", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")

healbutt = ctk.CTkButton(master = cmdFrame, text= "heal", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")
habbitbutt = ctk.CTkButton(master = cmdFrame, text= "habbit", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")
behaviourbutt = ctk.CTkButton(master = cmdFrame, text= "behaviour", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")
callbutt = ctk.CTkButton(master = cmdFrame, text= "call", fg_color="#0FDE23", text_color="white", corner_radius=20, font=("Lato", 15, "bold"),hover_color="#0E8144")

cmdFrame.grid_columnconfigure(0, minsize= 200)
cmdFrame.grid_columnconfigure(1, minsize = 200)
cmdFrame.grid_columnconfigure(2, minsize = 200)


left_buttons = [feedbutt, playbutt, sleepbutt]

for i, buttons in enumerate (left_buttons):
    buttons.grid(row=i, column=0, padx=25, pady=5, sticky="w")

mid_buttons = [cleanbutt, healbutt]

for i, buttons in enumerate(mid_buttons):
    buttons.grid(row = i, column = 1, padx = 25, pady=5, sticky = "nsew")

right_buttons = [habbitbutt,behaviourbutt,callbutt]
 

for i, buttons in enumerate(right_buttons):
    buttons.grid(row = i, column = 2, padx = 25, sticky = "e", pady=5)


imgFrame = ctk.CTkFrame(master = framebg ,fg_color="black")
imgFrame.pack(fill ="both")

pet_image = Image.open("pet_image.jpg") 
pet_image = pet_image.resize((200, 250)) 

pet_image_tk = ImageTk.PhotoImage(pet_image)

pet_label = ctk.CTkLabel(imgFrame, image=pet_image_tk, text="")
pet_label.pack()

aliveLabel = ctk.CTkLabel(master=imgFrame, text = "Alive", bg_color="#0FDE23", text_color="white", padx = 5, font = (" ", 25, "bold"))
orLabel = ctk.CTkLabel(master = imgFrame ,text = "or", text_color="white", padx = 5, font = ("Arial", 20, "italic"))
deadLabel = ctk.CTkLabel(master=imgFrame, text = "Dead", bg_color="gray", text_color="red", padx = 5, font = (" ", 25, "bold"))

imgFrame.grid_columnconfigure(0,minsize=400)
imgFrame.grid_columnconfigure(1,minsize=200)

pet_label.grid(row = 0,column = 0, sticky = "e", pady = 10)

aliveLabel.grid(row = 0, column = 1, pady = (20, 5), sticky = "n")
orLabel.grid(row = 0, column = 1, pady = 70, sticky = "n")
deadLabel.grid(row = 0, column = 1, pady = 120, sticky = "n")

outputFrame = ctk.CTkFrame(master= framebg, fg_color="black")
outputFrame.pack(fill = "both")

sleepLabel = ctk.CTkLabel(master = outputFrame ,text = "Sleeping:", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))
hungerLabel = ctk.CTkLabel(master = outputFrame ,text = "Hunger:", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))
happyLabel = ctk.CTkLabel(master = outputFrame ,text = "Happiness: ", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))
clearLabel = ctk.CTkLabel(master = outputFrame ,text = "Clearness:", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))

outputFrame.grid_columnconfigure(0, minsize=300)
outputFrame.grid_columnconfigure(1, minsize=300)

left_stats = [sleepLabel, hungerLabel, happyLabel, clearLabel]

for i, stats in enumerate(left_stats):
    stats.grid (row = i, column = 0, padx = 30, sticky = "w", pady=5)

healthLabel = ctk.CTkLabel(master = outputFrame ,text = "Health:", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))
habbitLabel = ctk.CTkLabel(master = outputFrame ,text = "Habbit:", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))
behaviourLabel = ctk.CTkLabel(master = outputFrame ,text = "Behaviour: ", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))
callLabel = ctk.CTkLabel(master = outputFrame ,text = "Call:", bg_color="white", text_color="black", padx = 5, font = ("Arial", 20, "italic"))


right_stats = [healthLabel , habbitLabel, behaviourLabel, callLabel]

for i, stats in enumerate(right_stats):
    stats.grid (row = i, column = 1, padx = 50, sticky = "e", pady=5)

app.mainloop()

