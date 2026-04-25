import tkinter as tk
import winsound
import threading
root = tk.Tk() # it creates a window
root.title("Paino 🎹") # it sets the title of the window
canvas = tk.Canvas(root , width =800 , height = 300, bg = 'black')#it creates a canvas widget with a specified width, height, and background color
canvas.pack()# it adds the canvas to the window
## white keys
key_width = 57
key_height = 450
gap = 2
num_key = 14
white_frequencies = [
    261, 294, 329, 349, 392, 440, 494,
    523, 587, 659, 698, 784, 880, 988
]

for i in range(num_key):
    x1 = i * (key_width +gap)
    y1 = 0
    x2 = x1 + key_width
    y2 = key_height
    canvas.create_rectangle(x1 , y1 , x2 , y2 , fill = 'white' , outline = 'black' , tags=f'white_key_{i}') # it creates a rectangle on the canvas with the specified coordinates, fill color, and outline color
    canvas.tag_bind(f"white_key_{i}", "<Button-1>", lambda event,tag=f"white_key_{i}", freq=white_frequencies[i]: on_click(tag, freq))
    

def on_click(tag, freq):
    canvas.itemconfig(tag, fill='yellow')
    threading.Thread(target=lambda: winsound.Beep(freq, 300)).start() # it starts a new thread to play the sound without blocking the main thread
    root.after(300, lambda: canvas.itemconfig(tag, fill='white'))# it schedules a function to change the color of the key back to white after 300 milliseconds

##black keys
black_width = 30
black_height = 160
black_position = [0 , 1,3,4,5,7,8,10,11,12]
for pos in black_position:
    x1 = pos * (key_width + gap) + key_width - black_width // 2
    y1 = 0
    x2 = x1 +black_width
    y2 = black_height
    canvas.create_rectangle(x1 , y1 , x2 , y2 , fill = 'black' , outline = 'black') # it creates a rectangle on the canvas with the specified coordinates, fill color, and outline color
    
        
    

root.mainloop()# it starts the main loop of the window, which keeps it open and responsive to user interactions
    
    
    
    
