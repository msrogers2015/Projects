import tkinter as tk
import math as m


# Variables
# General
btn_relief = 'flat'

# Colors
btn_color = '#38484e'
btn_num_color = '#596b6e'
base_color = '#222e34'
text_color = 'white'

# Locations
row1= 151
row2= 209
row3= 267
row4= 325
row5= 383
row6= 441
col1 = 1
col2 = 81
col3 = 161
col4 = 241

# Dimensions
btn_w = 78
btn_h = 56

f_num = None
s_num = None
e_num = None

# Equal variables
math_equation = ""
current = 0
float_prec = 6


# Functions
# Add first and second values
def add():
  entry.config(state='normal')
  history.config(state='normal')
  global f_num
  global math_equation
  f_num = entry.get()
  entry.delete(0, tk.END)
  entry.insert(0, '0')
  history.delete(0, tk.END)
  history.insert(0, f'{f_num} +')
  math_equation = 'add'
  entry.config(state='disabled')
  history.config(state='disabled')

# Subtract second value from first
def subtract():
  entry.config(state='normal')
  history.config(state='normal')
  global f_num
  global math_equation
  f_num = entry.get()
  entry.delete(0, tk.END)
  entry.insert(0, '0')
  history.delete(0, tk.END)
  history.insert(0, f'{f_num} -')
  math_equation = 'subtract'
  entry.config(state='disabled')
  history.config(state='disabled')

# Mulitply first and second values
def multiply():
  entry.config(state='normal')
  history.config(state='normal')
  global f_num
  global math_equation
  f_num = entry.get()
  entry.delete(0, tk.END)
  entry.insert(0, '0')
  history.delete(0, tk.END)
  history.insert(0, f'{f_num} *')
  math_equation = 'multiply'
  entry.config(state='disabled')
  history.config(state='disabled')

# divide first value by
def divide():
  entry.config(state='normal')
  history.config(state='normal')
  global f_num
  global math_equation
  f_num = entry.get()
  entry.delete(0, tk.END)
  entry.insert(0, '0')
  history.delete(0, tk.END)
  history.insert(0, f'{f_num} /')
  math_equation = 'divide'
  entry.config(state='disabled')
  history.config(state='disabled')

# Turn current value into a decimal reflecting percentage
def percentage():
  entry.config(state='normal')
  current = float(entry.get())
  percent = round(current/100, float_prec)
  entry.delete(0, tk.END)
  entry.insert(0, str(percent))
  entry.config(state='disabled')

# Find square root of current value
def squareroot():
  entry.config(state='normal')
  current = float(entry.get())
  if current % 1 == 0:
    current = int(current)
  root = m.sqrt(current)
  if root % 1 == 0:
    root = int(root)
  else:
    root = round(root, float_prec)
  entry.delete(0, tk.END)
  entry.insert(0, str(root))
  entry.config(state='disabled')

# Multiply current value by itself
def square():
  entry.config(state='normal')
  history.config(state='normal')
  current = float(entry.get())
  square = current * current
  if square % 1 == 0:
    square = int(square)
  if current % 1 == 0:
    current = int(current)
  entry.delete(0, tk.END)
  entry.insert(0, square)
  history.delete(0, tk.END)
  history.insert(0, f'{current} * {current}')
  entry.config(state='disabled')
  history.config(state='disabled')

# Turn current entry into a fraction:
def fraction():
  entry.config(state='normal')
  current = float(entry.get())
  frac = round(1/current, float_prec)
  entry.delete(0, tk.END)
  if frac % 1 == 0:
    frac = int(frac)
  entry.insert(0, str(frac))
  entry.config(state='disabled')

# Clear entry screen
def clear():
  entry.config(state='normal')
  entry.delete(0, tk.END)
  entry.insert(0, '0')
  entry.config(state='disabled')

# Clear entry screen and all saved values
def clear_all():
  global f_num
  global s_num
  global math_equation
  f_num = None
  s_num = None
  math_equation = ""
  entry.config(state='normal')
  history.config(state='normal')
  entry.delete(0, tk.END)
  history.delete(0, tk.END)
  entry.insert(0, '0')
  history.insert(0, '0')
  entry.config(state='disabled')
  history.config(state='disabled')

# Delete last value typed into entry
def delete():
  entry.config(state='normal')
  current = len(entry.get())
  last = current-1
  entry.delete(last, tk.END)
  entry.config(state='disabled')

# Change the sign of the current entry
def negate():
  entry.config(state='normal')
  current = entry.get()
  negate = -1 * float(current)
  entry.delete(0, tk.END)
  if negate % 1 == 0:
    entry.insert(0, int(negate))
  else:
    entry.insert(0, float(negate))
  entry.config(state='disabled')
  

# Preform calculation
def equal():
  entry.config(state='normal')
  history.config(state='normal')
  global current
  global s_num
  current += 1
  if current > 1:
    if math_equation == 'add':
      solve = float(s_num) + float(entry.get())
      current_history = entry.get()
      history.delete(0, tk.END)
      history.insert(0, f'{current_history} + {s_num}')
    if math_equation == 'subtract':
      solve = float(entry.get()) - float(s_num)
      current_history = entry.get()
      history.delete(0, tk.END)
      history.insert(0, f'{current_history} - {s_num}')
    if math_equation == 'multiply':
      solve = float(entry.get()) * float(s_num)
      current_history = entry.get()
      history.delete(0, tk.END)
      history.insert(0, f'{current_history} * {s_num}')
    if math_equation == 'divide':
      solve = float(entry.get()) / float(s_num)
      current_history = entry.get()
      history.delete(0, tk.END)
      history.insert(0, f'{current_history} / {s_num}')
    if solve % 1 == 0:
      solve = int(solve)
  else:
    if math_equation == 'add':
      solve = float(f_num) + float(entry.get())
      s_num = entry.get()
      history.insert(tk.END, entry.get())
    if math_equation == 'subtract':
      solve = float(f_num) - float(entry.get())
      s_num = entry.get()
      history.insert(tk.END, entry.get())
    if math_equation == 'multiply':
      solve = float(f_num) * float(entry.get())
      s_num = entry.get()
      history.insert(tk.END, entry.get())
    if math_equation == 'divide':
      solve = float(f_num) / float(entry.get())
      s_num = entry.get()
      history.insert(tk.END, entry.get())
    if solve % 1 == 0:
      solve = int(solve)
  entry.delete(0, tk.END)
  entry.insert(0, str(solve))
  entry.config(state='disabled')
  history.config(state='disabled')

# Pass value of button to entry
def button_pressed(digit):
  entry.config(state='normal')
  current = entry.get()
  list_current = list(current)
  if entry.get() == "0" and digit != '.':
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(digit))
  elif '.' not in list_current and digit == '.':
    entry.insert(tk.END, str(digit))
  elif '.' not in list_current and digit != '.':
    entry.insert(tk.END, str(digit))
  elif '.' in list_current and digit != '.':
    entry.insert(tk.END, str(digit))
  entry.config(state='disabled')


# Create Tkinter window
root = tk.Tk()
root.geometry('321x498')
root.title('Calculator')
root.configure(bg=base_color)


# Creating gui content

# Display Window
entry = tk.Entry(root, bg=base_color, fg=text_color, font=('Helvetica', 48), justify='right', relief='flat' ,disabledbackground=base_color)
history = tk.Entry(root, bg=base_color,fg=btn_num_color,font=('Helvetica', 20), justify='left', relief='flat', disabledbackground=base_color)

# First row
percent = tk.Button(root, text="%", relief=btn_relief, bg=btn_color, fg=text_color, command=percentage)
c_all = tk.Button(root, text="CE", relief=btn_relief, bg=btn_color, fg=text_color, command=clear)
c_screen = tk.Button(root, text="CA", relief=btn_relief, bg=btn_color, fg=text_color, command=clear_all)
delete = tk.Button(root, text="DEL", relief=btn_relief, bg=btn_color, fg=text_color, command=delete)

# Second row
fraction = tk.Button(root, text="1/x", relief=btn_relief, bg=btn_color, fg=text_color, command=fraction)
exponent = tk.Button(root, text="x^2", relief=btn_relief, bg=btn_color, fg=text_color, command=square)
sqroot = tk.Button(root, text="sqrt", relief=btn_relief, bg=btn_color, fg=text_color, command=squareroot)
divide = tk.Button(root, text="/", relief=btn_relief, bg=btn_color, fg=text_color, command=divide)

# Third row
b7 = tk.Button(root, text="7", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(7))
b8 = tk.Button(root, text="8", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(8))
b9 = tk.Button(root, text="9", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(9))
multiply = tk.Button(root, text="*", relief=btn_relief, bg=btn_color, fg=text_color, command=multiply)

# Forth row
b4 = tk.Button(root, text="4", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(4))
b5 = tk.Button(root, text="5", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(5))
b6 = tk.Button(root, text="6", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(6))
subtract = tk.Button(root, text="-", relief=btn_relief, bg=btn_color, fg=text_color, command=subtract)

# Fifth row
b1 = tk.Button(root, text="1", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(1))
b2 = tk.Button(root, text="2", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(2))
b3 = tk.Button(root, text="3", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(3))
addition = tk.Button(root, text="+", relief=btn_relief, bg=btn_color, fg=text_color, command=add)

# Sixth row
negate = tk.Button(root, text="+-", relief=btn_relief, bg=btn_color, fg=text_color, command=negate)
b0 = tk.Button(root, text="0", relief=btn_relief, bg=btn_num_color, fg=text_color, command=lambda: button_pressed(0))
period = tk.Button(root, text=".", relief=btn_relief, bg=btn_color, fg=text_color, command=lambda: button_pressed('.'))
equal = tk.Button(root, text="=", relief=btn_relief, bg=btn_color, fg=text_color, command=equal)


# Placing gui content
entry.place(width=320, height=125, y=25)
entry.insert(0, '0')
entry.config(state='disabled')
history.place(width=320,height=25)
history.insert(0, "0")
history.config(state='disabled')


# First row
percent.place(width=btn_w, height=btn_h, y=row1, x=col1)
c_all.place(width=btn_w, height=btn_h, y=row1, x=col2)
c_screen.place(width=btn_w, height=btn_h, y=row1, x=col3)
delete.place(width=btn_w, height=btn_h, y=row1, x=col4)

# Second row
fraction.place(width=btn_w, height=btn_h, y=row2, x=col1)
exponent.place(width=btn_w, height=btn_h, y=row2, x=col2)
sqroot.place(width=btn_w, height=btn_h, y=row2, x=col3)
divide.place(width=btn_w, height=btn_h, y=row2, x=col4)

# Third row
b7.place(width=btn_w, height=btn_h, y=row3, x=col1)
b8.place(width=btn_w, height=btn_h, y=row3, x=col2)
b9.place(width=btn_w, height=btn_h, y=row3, x=col3)
multiply.place(width=btn_w, height=btn_h, y=row3, x=col4)

# Forth row
b4.place(width=btn_w, height=btn_h, y=row4, x=col1)
b5.place(width=btn_w, height=btn_h, y=row4, x=col2)
b6.place(width=btn_w, height=btn_h, y=row4, x=col3)
subtract.place(width=btn_w, height=btn_h, y=row4, x=col4)

# Fifth row
b1.place(width=btn_w, height=btn_h, y=row5, x=col1)
b2.place(width=btn_w, height=btn_h, y=row5, x=col2)
b3.place(width=btn_w, height=btn_h, y=row5, x=col3)
addition.place(width=btn_w, height=btn_h, y=row5, x=col4)

# Sixth row
negate.place(width=btn_w, height=btn_h, y=row6, x=col1)
b0.place(width=btn_w, height=btn_h, y=row6, x=col2) 
period.place(width=btn_w, height=btn_h, y=row6, x=col3)
equal.place(width=btn_w, height=btn_h, y=row6, x=col4)


root.mainloop()
