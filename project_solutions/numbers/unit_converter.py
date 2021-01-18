import tkinter as tk

# Create Window
root = tk.Tk()
root.geometry('300x300')
root.title('Conversion')

conversionVar = tk.StringVar(root)

#Conversion Drop down list values
convertType = {'Tempature', 'Weight'}
conversionVar.set('Tempature')

#Create list
convertTypeMenu = tk.OptionMenu(root,conversionVar,*convertType)


# Place List
convertTypeMenu.pack()



#Changing Main conversion drop down menu
def change_conversion(*args):
    print(tkvar.get())

root.mainloop()