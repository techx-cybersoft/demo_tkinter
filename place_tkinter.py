import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

# place
frameYellow = customtkinter.CTkFrame(master=root, fg_color="yellow")

# 0 - 1: 0.5 = 50%
frameYellow.place(relwidth=0.5, relheight=0.5, relx=0, rely=0)

frameSilver = customtkinter.CTkFrame(master=root, fg_color="grey")
frameSilver.place(relwidth=0.5, relheight=0.5, relx=0, rely=0.5)

frameRed = customtkinter.CTkFrame(master=root, fg_color="red")
frameRed.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0)

frameBlue = customtkinter.CTkFrame(master=root, fg_color="blue")
frameBlue.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5)


root.mainloop()