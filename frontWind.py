import customtkinter as ctk
import subprocess 
# Создаем главное окно приложения





class FrontClass(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("360x640")
        self.title("MyTamagochi")
        self.resizable(False, False)

    def setup_gui(self):
        self.backgr = ctk.CTkFrame(self, width = 360, height = 640, fg_color="black")
        self.backgr.pack(fill ="both", expand= True)


        self.frame1 = ctk.CTkFrame(self.backgr, fg_color="white", corner_radius=5)
        self.frame1.pack(pady=(100, 20))

        self.label1 = ctk.CTkLabel(self.frame1, text="TAMAGOCHI", text_color="black", font=("", 20, "bold"))
        self.label1.pack(pady=(5,2), padx=6) 

        self.frame2 = ctk.CTkFrame(self.backgr, fg_color="white", corner_radius=5)
        self.frame2.pack(pady=(30,15))

        self.label2 = ctk.CTkLabel(self.frame2, text="Type a name for your pet", text_color="black", font=("", 16, "bold"))
        self.label2.pack(pady=(1,0), padx=5) 

        self.entry1 = ctk.CTkEntry(self.backgr, placeholder_text="Enter:",font= ("Arial",16),placeholder_text_color= "white", border_color="red", width= 180, corner_radius=0)
        self.entry1.pack(pady=5)
        
        self.entry1.bind("<Return>", self.get_value)
    def get_value(self):
        value = self.entry1.get()

        self.frame3 = ctk.CTkFrame(self.backgr, fg_color="white", corner_radius=5)
        self.frame3.pack(pady=(15))

        self.label3 = ctk.CTkLabel(self, text="Choose type", text_color="black", font =("", 16, "bold"))
        self.label3.pack(pady = (1,0), padx = 5)

        self.entry2 = ctk.CTkEntry(self.backgr, placeholder_text="Enter:",font= ("Arial",16),placeholder_text_color= "white", border_color="red", width= 180, corner_radius=0)
        self.entry2.pack(pady=5)
        
        self.buttonplay = ctk.CTkButton(self.backgr ,command=self.open_second_window,  text="GET TAMAGOCHI", fg_color="#0FDE23", text_color="white", corner_radius=50, height=70, font=("Lato", 15, "bold"),hover_color="#0E8144")
        self.buttonplay.pack(pady=20, padx = 60)  
       
    def open_second_window(self):
        subprocess.Popen(["python", "backWind.py"])


    
    
def nameType(self):
    name = self.entry1.get() #ввод сделаю через ентри

    while True:
        animalType = input("choose animal: ") # ввод через 2 ентри
        if self.entry2.get() == "cat":   #заменить енимал тайп на геттер ентри
            pet = cat(name)
            break
        elif self.entry2.get() == "dog": # заменить енимал тайп на геттер ентри
            pet = dog(name)
            break
        else:
            print("U can choose only between dog and cat") # текст фоновый который измениться на надпись
            break


class run(FrontClass):

    app = FrontClass()
    FrontClass.setup_gui(self)
    app.mainloop()
    nameType(self)
 
        

