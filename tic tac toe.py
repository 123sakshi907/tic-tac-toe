import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont


def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Toc-Toe",f'player{buttons[combo[0]]['text']}wins!')
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player ='x' if current_player == "0" else "0"
    label.config(text=f"player {current_player}'s turn")

root = tk.Tk()
custom_font = tkFont.Font(family="Arial", size=25) 

buttons = [tk.Button(root, text="", font=custom_font, width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]



for i,button in enumerate(buttons):
    button.grid(row=i //3,column=i%3)

current_player="x"
winner=False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 20))

root.mainloop()