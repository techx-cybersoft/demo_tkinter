import customtkinter

class FrameGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, fg_color):
        super().__init__(master=master, fg_color=fg_color)
        self.grid(row=0, column=0, sticky="news")


        for index in range(0, 50):
            button = customtkinter.CTkButton(self, text=f"Press {index}", text_color="white", fg_color="green", command=lambda i =index :self.show_num(i))
            button.pack(pady=10)
    
    def show_num(self, num):
        print(num)

class App(customtkinter.CTk):
    def __init__(self, name, size):
        super().__init__()
        self.title(name)
        self.geometry(size)

        FrameGrid(self, "silver")

customtkinter.set_appearance_mode("dark")
app = App("Cybersoft", "800x500")

for column in range(0, 1):
    app.columnconfigure(column, weight=1)
    app.rowconfigure(column, weight=1)

app.mainloop()