import tkinter as tk
 
ventana = tk.Tk()
 
canvas = tk.Canvas(ventana, width=800, height=800)
canvas.pack() 

imagen = tk.PhotoImage(file="mega.png")
imagen = canvas.create_image(10, 10, anchor=tk.NW, image=imagen)
 
 
def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        canvas.move(imagen, -10, 0)
    elif event.char == "d":
        canvas.move(imagen, 10, 0)
    elif event.char == "w":
        canvas.move(imagen, 0, -10)
    elif event.char == "s":
        canvas.move(imagen, 0, 10)

ventana.bind("<Key>", move)

ventana.mainloop()