from pprint import pp
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from typing import ItemsView

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
        '''
        import threading
        import generate
        thr = threading.Thread(target=generate.main, args=(), kwargs={})
        thr.start()
        '''
        import generate
        generate.main()

    def close_All(self):
        self.master.destroy()


class form_Settings:
    def __init__(self, master):

        #get first data
        import json
        with open('settings.json') as json_file:
            json_data = json.load(json_file)

        #set tkinter window with variables
        self.master = master
        self.master.title("Settings")
        self.frm = ttk.Frame(self.master, padding=20)
        self.frm.grid()

        ttk.Label(self.frm, text="Settings").grid(column=0, row=0, columnspan=3)
        
        ttk.Label(self.frm, text="Base File").grid(column=0, row=1)
        self.e_base_file = ttk.Entry(self.frm)
        self.e_base_file.insert(0, json_data["settings"]["base_file"])
        self.e_base_file.grid(column=1, row=1)
        ttk.Button(self.frm, text="Select", command=self.get_base_file).grid(column=2, row=1)

        ttk.Label(self.frm, text="Output Folder").grid(column=0, row=2)
        self.e_output_folder = ttk.Entry(self.frm)
        self.e_output_folder.insert(0, json_data["settings"]["output_folder"])
        self.e_output_folder.grid(column=1, row=2)
        ttk.Button(self.frm, text="Select", command=lambda:self.get_output_folder(self.e_output_folder)).grid(column=2, row=2)

        ttk.Label(self.frm, text="Base File Order").grid(column=0, row=3)
        t_int_var1 = StringVar(value=json_data["settings"]["base_order"])
        self.e_base_file_order = Spinbox(self.frm, from_=0, to=99, increment=1, textvariable=t_int_var1)
        self.e_base_file_order.grid(column=1, row=3)

        ttk.Label(self.frm, text="Include Empty Layer").grid(column=0, row=4)
        self.t_int_var2 = BooleanVar(value=json_data["settings"]["empty_layer"])
        self.e_empty_layer = Checkbutton(self.frm, text="Include?", variable=self.t_int_var2, onvalue=True, offvalue=False)
        self.e_empty_layer.grid(column=1, row=4)


        ttk.Label(self.frm, text="Layer Folders\n(Ordered)").grid(column=0, row=5)
        self.e_layers_area = Text(self.frm, width=20, height=10)
        self.e_layers_area.grid(column=1, row=5)
        for x_ln in json_data["layers"]:
            self.e_layers_area.insert(END,x_ln["input_folder"]+"\n")
        
        ttk.Button(self.frm, text="Save", command=self.save_settings).grid(column=2, row=999)
    
    def get_base_file(self):
        filename = fd.askopenfilename()
        self.e_base_file.delete(0,'end')
        self.e_base_file.insert(0,filename)
    
    def get_output_folder(self, entry):
        filename = fd.askdirectory()
        entry.delete(0,'end')
        entry.insert(0,filename)
    
    def save_settings(self):
        import json
        json_data = {}
        json_data["settings"] = {}
        json_data["settings"]["output_folder"] = self.e_output_folder.get()
        json_data["settings"]["base_file"] = self.e_base_file.get()
        json_data["settings"]["empty_layer"] = self.t_int_var2.get()
        try:
            json_data["settings"]["base_order"] = int(self.e_base_file_order.get())
        except:
            print("Sayı isteyen yere metin mi yazıyosun?")
            return

        json_data["layers"] = []
        for layer_ln in str.split(self.e_layers_area.get("1.0",END),"\n"):
            if(layer_ln != ""):
                json_data["layers"].append({
                    "input_folder": layer_ln
                })

        from pprint import pprint
        pprint(json_data)

        with open('settings.json', 'w') as json_file:
            json.dump(json_data, json_file)

        self.master.destroy()

def main(): 
    root = Tk()
    app = form_Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()