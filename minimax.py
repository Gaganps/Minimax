import tkinter as tk
import time

z = 16

class TreeNode:
    def __init__(self, canvas, x, y, depth, branch_count, branch_spacing, flag,value=0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.depth = depth
        self.branch_count = branch_count
        self.branch_spacing = branch_spacing
        self.children = []
        self.value = value
        self.input_field = None
        self.flag=flag

    def create_children(self):
        if self.depth > 0:
            for i in range(self.branch_count):
                new_x = self.x - (self.branch_count - 1) * self.branch_spacing / 2 + i * self.branch_spacing
                new_y = self.y + 70
                self.canvas.create_line(self.x, self.y, new_x, new_y, fill='blue')

                child = TreeNode(self.canvas, new_x, new_y, self.depth - 1, self.branch_count, self.branch_spacing/2, self.flag-1,value=0)
                child.create_children()
                self.children.append(child)

            if self.children:
                if self.flag % 2 == 0:
                    self.value = max(child.value for child in self.children)
                    self.canvas.create_oval(self.x - z, self.y - z, self.x + z, self.y + z, fill='green')
                else:
                    self.value = min(child.value for child in self.children)
                    self.canvas.create_oval(self.x - z, self.y - z, self.x + z, self.y + z, fill='red')
                # self.canvas.create_text(self.x, self.y, text=str(self.value), fill='white',font = 12)

        elif self.depth == 0:
            # Create input fields for leaf nodes
            self.canvas.create_oval(self.x - z, self.y - z, self.x + z, self.y + z, fill='yellow')
            self.input_field = tk.Entry(self.canvas)
            self.input_field.place(x=self.x, y=self.y + 30, anchor="center", width=30)

    def minimax(self):
        if self.depth == 0:
            try:
                self.value = int(self.input_field.get())
            except ValueError:
                self.value = 0
            time.sleep(0.5)
            root.update()                               
            self.canvas.create_oval(self.x - z, self.y - z, self.x + z, self.y + z, fill='purple')
            self.canvas.create_text(self.x, self.y, text=str(self.value), fill='white',font =12)
        else:
            for child in self.children:
                child.minimax()
            
            if self.flag % 2 == 0:
                self.value = max(child.value for child in self.children)
                self.canvas.create_oval(self.x - z, self.y - z, self.x + z, self.y + z, fill='green')
            else:
                self.value = min(child.value for child in self.children)
                self.canvas.create_oval(self.x - z, self.y - z, self.x + z, self.y + z, fill='red')
            time.sleep(0.5)
            self.canvas.create_text(self.x, self.y, text=str(self.value), fill='white',font =12)

def calculate_minimax():
    root_node.minimax()
    result_label.config(text="Minimax Algorithm Applied")
    
    

# Create the main window
root = tk.Tk()
root.title("Minimax Algorithm")

heading_label = tk.Label(root, text="MiniMax Algorithm",fg="blue",font=48)
heading_label.pack()



# Create a Canvas widget to draw the tree
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack()

# Define the root node's coordinates and create the tree
root_x = 400
root_y = 30
tree_depth = 3
branch_count = 2
branch_spacing = 300
root_node = TreeNode(canvas, root_x, root_y, tree_depth, branch_count, branch_spacing, 10,value=0)
root_node.create_children()

calculate_button = tk.Button(root, text="Calculate Minimax", command=calculate_minimax)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
