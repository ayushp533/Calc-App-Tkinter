from tkinter import *
from tkinter import messagebox

calc_win = Tk()
calc_win.title("Basic Calculator")
calc_win.iconbitmap("D:\Downloads\calculator-icon_34473.ico")
calc_win.config(bg="lightgrey")
calc_win.resizable(0, 0)

window_width = 423
window_height = 575
calc_win.geometry(f"{window_width}x{window_height}")

left_x = int(calc_win.winfo_screenwidth()/2 - window_width/2)
top_y = int(calc_win.winfo_screenheight()/2 - window_height/2)
calc_win.geometry("+{}+{}".format(left_x, top_y))

#! ---------------------- OPERATION FUNCTIONS ----------------------

def credit():
    messagebox.showinfo(title="CREDITS", message="This calculator was created by Ayush using Python tkinter.")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def btn_equals():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

#! ------------------------------- GUI -------------------------------
#? ----------------------------- TOP ROW -----------------------------
input_frame = Frame(calc_win, width=423, height=70, bd=0, highlightbackground="black", highlightcolor="white", highlightthickness=2)
input_frame.pack(side=TOP)

user_entry = Entry(input_frame, text="0", bg="#eee", bd=0, justify="right", font=('arial', 32, 'bold'), width=50, textvariable=input_text)
user_entry.grid(row=0, column=0)
user_entry.pack(ipady=20)

#? ----------------------------- 2nd ROW -----------------------------
btn_frame = Frame(calc_win, width=423, height = 280, bg="grey")
btn_frame.pack()

btn_cl = Button(btn_frame, text="Clear", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=18, cursor="hand2", command = btn_clear).grid(row=0, column=0, columnspan=2, padx=1, pady=1)

btn_equals = Button(btn_frame, text="=", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, width=12, bd=0, cursor="hand2", command = btn_equals).grid(row=0, column=3, padx=1, pady=1)

#? ----------------------------- 3rd ROW -----------------------------
row3_frame = Frame(calc_win, width=423, height = 280, bg="grey")
row3_frame.pack()

btn_7 = Button(row3_frame, text="7", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2",command = lambda: btn_click("7")).grid(row=0, column=0, padx=1, pady=1)

btn_8 = Button(row3_frame, text="8", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, width=7, bd=0, cursor="hand2", command = lambda: btn_click("8")).grid(row=0, column=1, padx=1, pady=1)

bt_9 = Button(row3_frame, text="9", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, width=7, bd=0, cursor="hand2", command = lambda: btn_click("9")).grid(row=0, column=2, padx=1, pady=1)

btn_divide = Button(row3_frame, text="/", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, width=7, bd=0, cursor="hand2", command = lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

#? ----------------------------- 4th ROW -----------------------------
row4_frame = Frame(calc_win, width=423, height = 280, bg="grey")
row4_frame.pack()

btn_4 = Button(row4_frame, text="4", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("4")).grid(row=1, column=0, padx=1, pady=1)

btn_5 = Button(row4_frame, text="5", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("5")).grid(row=1, column=1, padx=1, pady=1)

btn_6 = Button(row4_frame, text="6", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("6")).grid(row=1, column=2, padx=1, pady=1)

btn_multiply = Button(row4_frame, text="X", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

#? ----------------------------- 5th ROW -----------------------------
row6_frame = Frame(calc_win, width=423, height = 280, bg="grey")
row6_frame.pack()

btn_1 = Button(row6_frame, text="1", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("1")).grid(row=2, column=0, padx=1, pady=1)

btn_2 = Button(row6_frame, text="2", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("2")).grid(row=2, column=1, padx=1, pady=1)

btn_3 = Button(row6_frame, text="3", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("3")).grid(row=2, column=2, padx=1, pady=1)

btn_plus = Button(row6_frame, text="+", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("+")).grid(row=2, column=3, padx=1, pady=1)

#? ----------------------------- BOTTOM ROW -----------------------------
row6_frame = Frame(calc_win, width=423, height = 280, bg="grey")
row6_frame.pack()

btn_credit = Button(row6_frame, text="Credit", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = credit).grid(row=3, column=0, padx=1, pady=1)

btn_0 = Button(row6_frame, text="0", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("0")).grid(row=3, column=1, padx=1, pady=1)

btn_decimal = Button(row6_frame, text=".", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click(".")).grid(row=3, column=2, padx=1, pady=1)

btn_minus = Button(row6_frame, text="-", fg = "black", bg = "#eee", font=("Times", 18, "bold"), height=3, bd=0, width=7, cursor="hand2", command = lambda: btn_click("-")).grid(row=3, column=3, padx=1, pady=1)

calc_win.mainloop()