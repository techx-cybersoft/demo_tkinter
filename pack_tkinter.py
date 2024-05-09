import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("Dark")

root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

# frame => khung
# 1/ pack
# 2/ place
# 3/ grid
# Parameter 1: master =>
frameRight = customtkinter.CTkFrame(master=root)
frameRight.pack(side="right", expand=True, fill="both")
frameRed = customtkinter.CTkFrame(master=frameRight, fg_color="red")
# side = top, bottom, left, right
# expand = True, False
# fill = both, x, y
frameRed.pack(side="top", expand=True, fill="both")

frameBlue = customtkinter.CTkFrame(master=frameRight, fg_color="blue")
frameBlue.pack(side="bottom", expand=True, fill="both")

frameLeft = customtkinter.CTkFrame(master=root)
frameLeft.pack(side="left", expand=True, fill="both")

frameYellow = customtkinter.CTkFrame(master=frameLeft, fg_color="yellow")
frameYellow.pack(side="top", expand=True, fill="both")

frameSilver = customtkinter.CTkFrame(master=frameLeft, fg_color="grey")
frameSilver.pack(side="bottom", expand=True, fill="both")

# widgets

# class

# Vòng lặp giao diện
root.mainloop()