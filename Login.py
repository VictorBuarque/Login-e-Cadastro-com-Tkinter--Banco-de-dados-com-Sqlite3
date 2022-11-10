import tkinter
from tkinter import PhotoImage, messagebox
from tkinter.tix import COLUMN
from Cadastro import abrir_janela
#Janela
window = tkinter.Tk()
window.title('Portal do Aluno')
window.geometry('800x600+400+50')
window.resizable(width = 1, height = 1)
window.configure(bg="DarkOrchid2")
    
def login ():
    username = 'victor'
    password = '12345'
    if user_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title='Realizando login', message='Login realizado com sucesso')
    else:
        messagebox.showerror(title='Erro',message='Nome de usuário ou senha incorretos!')



#Frame = a um container que vai criar um box para uma box maior, tem que substituir o window do label para utilizar!
frame = tkinter.Frame(bg="DarkOrchid2")
frame.pack()
login_info_frame = tkinter.LabelFrame(frame, text="LOGIN",bg='DarkOrchid2', font=(15))
login_info_frame.grid(row= 0 , column= 0, sticky="news", padx=20, pady=20)

#Criando widgets
login_label = tkinter.Label(login_info_frame,bg='DarkOrchid2', text='Iprof',fg='black', font=('Arial',30))
user_label = tkinter.Label(login_info_frame,bg='DarkOrchid2', text='Username / Nome de Usuário',fg='black', font=('Arial',16))
user_entry = tkinter.Entry(login_info_frame,font=('Arial',30))
password_label = tkinter.Label(
    login_info_frame,bg='DarkOrchid2', text='Password / Senha',fg='black', font=('Arial',16))
password_entry = tkinter.Entry(login_info_frame, show='*', font=('Arial',30))
login_button = tkinter.Button(
    login_info_frame, text='Login',bg='DarkOrchid2',fg='black', font=('Arial',16),command=login)
register_button = tkinter.Button(login_info_frame, bg='DarkOrchid2', text="Cadastre-se",
fg='black', font=('Arial',16), command=abrir_janela)

#Colocando widgets na janela
login_label.grid(row=0, column=0, columnspan=2, sticky='news',pady=40) #news = North, East,West and South
user_label.grid(row=1,column=0)                                        #pady = Espaçamento na vertical eixo Y
user_entry.grid(row=1,column=1,pady=20,padx=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady=20,padx=5)
login_button.grid(row=3, column=0, columnspan=2,pady=30)
register_button.grid(row=3, column=1, columnspan=2, pady=30)

window.mainloop()