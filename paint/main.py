import tkinter as tk
from PIL import ImageGrab

class PaintApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Paint")
    self.root.geometry("1000x800")
    self.width = tk.IntVar(value=1)

    saveBtn = tk.Button(root, text="Save", command=self.save)
    clearBtn = tk.Button(root, text="Clear", command=self.clear)
    saveBtn.pack()
    clearBtn.pack()

    widthOption = tk.OptionMenu(root, self.width, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
    widthOption.pack()

    self.canvas = tk.Canvas(root, bg="white", width=900, height=600)
    self.canvas.pack(expand=True)
    
    self.canvas.bind("<Button-1>", self.start_draw)
    self.canvas.bind("<B1-Motion>", self.draw)

  def start_draw(self, event):
    self.old_x = event.x
    self.old_y = event.y

  def draw(self, event):
    if self.old_x and self.old_y:
      width = self.width.get()
      self.canvas.create_line(
        self.old_x, self.old_y, event.x, event.y,
        fill="black", width=width, smooth=True, capstyle=tk.ROUND
      )
    self.old_x = event.x
    self.old_y = event.y

  def save(self):
    x = root.winfo_rootx() + self.canvas.winfo_x()
    y = root.winfo_rooty() + self.canvas.winfo_y()
    x1 = x + self.canvas.winfo_width()
    y1 = y + self.canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("drawing.png")

  def clear(self):
    self.canvas.delete("all")
  
root = tk.Tk()
app = PaintApp(root)
root.mainloop()