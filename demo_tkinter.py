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
frameTop = customtkinter.CTkFrame(master=root, fg_color="red")
# side = top, bottom, left, right
# expand = True, False
# fill = both, x, y
frameTop.pack(side="left", expand=True, fill="both")

frameBot = customtkinter.CTkFrame(master=root, fg_color="blue")
frameBot.pack(side="right", expand=True, fill="both")

# widgets

# class

# Vòng lặp giao diện
root.mainloop()