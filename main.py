#1
import tkinter as tk
pencere=tk.Tk()
pencere.title("ders")
pencere.geometry("300x300")
yaz=tk.Label(pencere,text="salam,dunya!")
yaz.pack()
pencere.mainloop()
#2
import tkinter as tk
p=tk.Tk()
p.title("ev tapsiriqi")
p.geometry("400x400")
def basildi():
    yazi.config(text="butona basdin")
yazi=tk.Label(p,text="duymeye bas")
yazi.pack()
duyme=tk.Button(p,text="duymeyi bas",command=basildi)
duyme.pack()
p.mainloop()
#3
import tkinter as tk
pe=tk.Tk()
pe.title("salam")
pe.geometry("600x600")
def bas():
    ya.config(text="basisan")
def basda():
    ya.config(text="basda")
def basdada():
    ya.config(text="basdada")
ya=tk.Label(pe,text="is")
ya.pack()
d=tk.Button(pe,text="duymeye bas",command=bas)
du=tk.Button(pe,text="bas duymeye",command=basda)
duy=tk.Button(pe,text="duymeye basda",command=basdada)
d.pack()
du.pack()
duy.pack()
pe.mainloop()






































































