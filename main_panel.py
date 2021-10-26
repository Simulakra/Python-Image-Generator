from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

class form_Main:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto Image Generator")
        self.master.eval('tk::PlaceWindow . center')
        self.frm = ttk.Frame(self.master, padding=20)
        self.frm.grid()

        ttk.Label(self.frm, text="Auto Image Generator").grid(column=0, row=0, columnspan=2)
        ttk.Button(self.frm, text="Settings", command=self.goto_Settings).grid(column=0, row=1)
        ttk.Button(self.frm, text="Generate", command=self.run_Generate).grid(column=1, row=1)
        ttk.Button(self.frm, text="Quit", command=self.close_All).grid(column=1, row=2)

    def goto_Settings(self):
        self.newWindow = Toplevel(self.master)
        self.app = form_Settings(self.newWindow)

    def run_Generate(self):
        print("a")

    def close_All(self):
        self.master.destroy()


class form_Settings:
    def __init__(self, master):
        self.master = master
        self.master.title("Settings")
        self.frm = ttk.Frame(self.master, padding=20)
        self.frm.grid()

        ttk.Label(self.frm, text="Settings").grid(column=0, row=0, columnspan=3)
        
        ttk.Label(self.frm, text="Base File").grid(column=0, row=1)
        self.e_base_file = ttk.Entry(self.frm)
        self.e_base_file.grid(column=1, row=1)
        ttk.Button(self.frm, text="Select", command=self.get_base_file).grid(column=2, row=1)

        ttk.Label(self.frm, text="Output Folder").grid(column=0, row=2)
        self.e_output_folder = ttk.Entry(self.frm)
        self.e_output_folder.grid(column=1, row=2)
        ttk.Button(self.frm, text="Select", command=lambda:self.get_output_folder(self.e_output_folder)).grid(column=2, row=2)

        ttk.Label(self.frm, text="Base File Order").grid(column=0, row=3)
        self.e_base_file_order = ttk.Spinbox(self.frm)
        self.e_base_file_order.grid(column=1, row=3)

        ttk.Label(self.frm, text="Include Empty Layer").grid(column=0, row=4)
        self.e_empty_layer = ttk.Checkbutton(self.frm, text="True")
        self.e_empty_layer.grid(column=1, row=4)

        row_index = 5
        layer_folder_array = []
        for x in range(5):
            
            ttk.Label(self.frm, text="Layer Folder").grid(column=0, row=row_index)
            self.layer_folder = ttk.Entry(self.frm)
            self.layer_folder.grid(column=1, row=row_index)
            ttk.Button(self.frm, text="Select", command=lambda:self.get_output_folder(self.layer_folder)).grid(column=2, row=2)

            layer_folder_array.append(self.layer_folder)
            row_index+=1


        ttk.Button(self.frm, text="Save", command=self.save_settings).grid(column=2, row=999)
    
    def get_base_file(self):
        filename = fd.askopenfilename()
        self.e_base_file.delete(0,'end')
        self.e_base_file.insert(0,filename)
    
    def get_output_folder(self, entry_name):
        filename = fd.askdirectory()
        entry_name.delete(0,'end')
        entry_name.insert(0,filename)
    
    def save_settings(self):
        print(self.e_base_file.get())
        self.master.destroy()

def main(): 
    root = Tk()
    app = form_Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()