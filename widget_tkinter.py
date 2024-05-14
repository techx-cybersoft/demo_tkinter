import customtkinter
from PIL import Image

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.title("CyberSoft")
root.geometry("800x500")

entry = customtkinter.CTkEntry(root, placeholder_text="Type something...")
entry.pack()

def button_event():
    print(entry.get())

button = customtkinter.CTkButton(root, text="Press me", text_color="white", fg_color="green", command=lambda: button_event())
button.pack()

def checkbox_event():
    print("Checkbox toggled, current value: ", check_var.get())

check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(root, text="CheckBox", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox.pack()

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(root, from_=0, to=100, command=slider_event)
slider.pack()


my_image = customtkinter.CTkImage(light_image=Image.open("./img/robot.png"),
                                  dark_image=Image.open("./img/robot.png"),
                                  size=(100, 100))

image_label = customtkinter.CTkLabel(root, image=my_image, text="")  # display image with a CTkLabel
image_label.pack()

root.mainloop()