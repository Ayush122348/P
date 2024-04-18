from math import *
from art import *
print("-------------------------------------------")
tprint(text="Calculator")
print("                                        - By Ayush Kumar Kurrey")
print("-------------------------------------------")
Num1 = input("Enter the first number: ")
Operator = input("Enter the operator: ")
Num2 = input("Enter the second number: ")
Result_Txt = "Result: "
Result_Txt_non_space = "Result:"

def CP_Sector():
    import tkinter as tk
    from tkinter import colorchooser
    import colorsys

    def choose_color():
        color_code = colorchooser.askcolor(title="Choose Color")
        if color_code[1]:
            rgb_label.config(text=f"RGB: {color_code[0]}")
            rgba_label.config(text=f"RGBA: {(*color_code[0], 1)}")

            # Convert RGB to HSL
            hsl_color = rgb_to_hsl(*color_code[0])
            hsl_label.config(text=f"HSL: {hsl_color}")

            # Convert RGB to HSV
            hsv_color = rgb_to_hsv(*color_code[0])
            hsv_label.config(text=f"HSV: {hsv_color}")

            # Convert RGB to CMYK
            cmyk_color = rgb_to_cmyk(*color_code[0])
            cmyk_label.config(text=f"CMYK: {cmyk_color}")

            # Convert RGB to CIE Lab
            lab_color = rgb_to_lab(*color_code[0])
            lab_label.config(text=f"CIE Lab: {lab_color}")

            pantone_label.config(text="Pantone: Not implemented")

    def rgb_to_hsl(r, g, b):
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        h_deg = round(h * 360)
        l_percent = round(l * 100)
        s_percent = round(s * 100)
        return f"{h_deg}, {s_percent}%, {l_percent}%"

    def rgb_to_hsv(r, g, b):
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        h_deg = round(h * 360)
        s_percent = round(s * 100)
        v_percent = round(v * 100)
        return f"{h_deg}, {s_percent}%, {v_percent}%"

    def rgb_to_cmyk(r, g, b):
        c = 1 - (r / 255)
        m = 1 - (g / 255)
        y = 1 - (b / 255)
        k = min(c, m, y)
        if k == 1:
            return "0%, 0%, 0%, 100%"
        c = round((c - k) / (1 - k) * 100)
        m = round((m - k) / (1 - k) * 100)
        y = round((y - k) / (1 - k) * 100)
        k = round(k * 100)
        return f"{c}%, {m}%, {y}%, {k}%"

    def rgb_to_lab(r, g, b):
        r_norm, g_norm, b_norm = [x / 255 for x in (r, g, b)]
        return f"{r_norm}, {g_norm}, {b_norm}"

    # Create the main window
    window = tk.Tk()
    window.title("Color Picker - By Ayush Kumar Kurrey")
    window.geometry("400x300")
    window.resizable(False, False)
    window.minsize(False, False)
    # Create labels to display color codes
    rgb_label = tk.Label(window, text="RGB: ")
    rgb_label.pack(pady=5)
    rgba_label = tk.Label(window, text="RGBA: ")
    rgba_label.pack(pady=5)
    hsl_label = tk.Label(window, text="HSL: ")
    hsl_label.pack(pady=5)
    hsv_label = tk.Label(window, text="HSV: ")
    hsv_label.pack(pady=5)
    cmyk_label = tk.Label(window, text="CMYK: ")
    cmyk_label.pack(pady=5)
    lab_label = tk.Label(window, text="CIE Lab: ")
    lab_label.pack(pady=5)
    pantone_label = tk.Label(window, text="Pantone: ")
    pantone_label.pack(pady=5)

    # Create a button to open the color picker dialog
    color_btn = tk.Button(window, text="Choose Color For Values", command=choose_color)
    color_btn.pack(pady=20)

    # Run the application
    window.mainloop()


def SQ_Sector():
    SQ_in = input("Enter the number whose SQ is wanted: ")
    if SQ_in in ["1", "first", "First"]:
        print(Result_Txt + str(sqrt(float(Num1))))
    elif SQ_in in ["2", "second", "Second"]:
        print(Result_Txt + str(sqrt(float(Num2))))
    else:
        print("Double Enter to exit. [Program Ended as of Invalid Selection.]")
        p = input("")
def eflood():
    while True:
        print("😟😃😭😣😰🥵🧐💔✨🤪🎃" * 10)

def oflood():
    while True:
        print(str(Num1) * 30)

def tflood():
    while True:
        print(str(Num2) * 30)

def flood():
    FluInput = input("Enter the number being flooded: ")
    if FluInput.lower() in ["1", "first", "First"]:
        oflood()
    elif FluInput.lower() in ["2", "second", "Second"]:
        tflood()
    else:
        print("Double Enter to Exit [Program Ended as of Invalid Selection.]")
        p = input("")

def eCon():
    eConfirm = input("Are you sure? (Y/N): ").lower()
    if eConfirm == "y":
        eflood()
    elif eConfirm == "n":
        print("Double enter to exit.")
        p = input("")


try:
    if Operator in ["+", "add"]:
        print(Result_Txt + str(float(Num1) + float(Num2)))
    elif Operator in ["*", "mul"]:
        print(Result_Txt + str(float(Num1) * float(Num2)))
    elif Operator in ["/", "div"]:
        if (float(Num2) != 0):
            print(Result_Txt_non_space + "; Quotient: " + str(float(Num1) / float(Num2)))
            print(Result_Txt_non_space + "; Remainder: " + str(float(Num1) % float(Num2)))
        else:
            print("Error: Division by zero!")
    elif Operator in ["-", "subs"]:
        print(Result_Txt + str(float(Num1) - float(Num2)))
    elif Operator == "flood":
        print("Flood:")
        flood()
    elif Operator in ["emoflood", "emoji flood"]:
        eCon()
    elif Operator in ["sqrt", "square root", "SQ", "sq"]:
        SQ_Sector()
    elif Operator in ["CP", "cp", "colour picker", "Colour Picker", "colourpicker"]:
        CP_Sector()
    else:
        print("Error: Invalid Operator.")
except ZeroDivisionError as ZeroError:
    print("Error:", "Division By Zero!")
except ValueError as Value_Erosion:
    print("Error: ", "Value Conversion Failed.")
except SyntaxError as Error:
    print("Error: ", "Something went wrong... [Syntax Error!]")
P = input("")
input("Press Enter to exit.")
