import tkinter as tk
 
ventana = tk.Tk()
 
canvas = tk.Canvas(ventana, width=800, height=800)
canvas.pack() 

img = tk.PhotoImage(file="mega.png")
image = canvas.create_image(10, 10, anchor=tk.NW, image=img)
 
 
def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        canvas.move(img , -10, 0)
    elif event.char == "d":
        canvas.move(img , 10, 0)
    elif event.char == "w":
        canvas.move(img , 0, -10)
    elif event.char == "s":
        canvas.move(img , 0, 10)

ventana.bind("<Key>", move)

ventana.mainloop()