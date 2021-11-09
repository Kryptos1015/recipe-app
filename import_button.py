from libs import *

def import_file(fridge):
    fridge = []
    # Open file explorer, store data
    datafilename = filedialog.askopenfilename(initialdir='/Desktop', title='Select File', filetypes=(('Text Files','*.txt'),))
    
    try:
        fridge = open(datafilename, "r").read().splitlines()
        # Display successfully imported message
        successmsg = tk.Label(text='Imported successfully.', fg='#42f58a', bg='black',font='Courier 8')
        successmsg.place(x=290,y=320)
        window.after(2000, successmsg.destroy)

    except FileNotFoundError:
        errormsg = tk.Label(text='Please select a valid file.', fg='#cc0000', bg='black',font='Courier 8')
        errormsg.place(x=290,y=320)
        window.after(2000, errormsg.destroy)

    print(fridge)
