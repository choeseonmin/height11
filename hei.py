import tkinter as tk
import math

def calculate_height():
    try:
        angle_degrees = int(angle_input.get())
        angle_radians = math.radians(angle_degrees)
    except ValueError:
        height_output.config(text="정수값을 입력하세요.")
        return

    try:
        distance = float(distance_input.get())
    except ValueError:
        height_output.config(text="정수값을 입력하세요.")
        return

    height = distance * math.tan(angle_radians)
    height_output.config(text="높이 : {:.2f} m".format(height))

root = tk.Tk()
root.title("건물 높이 측정")
root.geometry("800x600")


angle_label = tk.Label(root, text="각도: ")
angle_input = tk.Entry(root)
distance_label = tk.Label(root, text="관찰자와 건물의 거리: ")
distance_input = tk.Entry(root)
calculate_button = tk.Button(root, text="입력", command=calculate_height)
height_output = tk.Label(root)

angle_label.grid(row=0, column=0)
angle_input.grid(row=0, column=1)
distance_label.grid(row=1, column=0)
distance_input.grid(row=1, column=1)

calculate_button.grid(row=2, column=0, columnspan=2)
height_output.grid(row=3, column=0, columnspan=2)


root.mainloop()
