import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

for column in range(0, 2):
    root.columnconfigure(column, weight=1)
    root.rowconfigure(column, weight=1)


frameRed = customtkinter.CTkFrame(master=root, fg_color="red")
frameRed.grid(row=0, column=1, sticky="nesw")

frameBlue = customtkinter.CTkFrame(master=root, fg_color="blue")
frameBlue.grid(row=1, column=1, sticky="nesw")

frameYellow = customtkinter.CTkFrame(master=root, fg_color="yellow")
frameYellow.grid(row=0, column=0, sticky="nesw")

frameSilver = customtkinter.CTkFrame(master=root, fg_color="grey")
frameSilver.grid(row=1, column=0, sticky="nesw")

# frame2 = customtkinter.CTkFrame(master=root, fg_color="blue")
# frame2.grid(row=0, column=1, sticky="")

root.mainloop()