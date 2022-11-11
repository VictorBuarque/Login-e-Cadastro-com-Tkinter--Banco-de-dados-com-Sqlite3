import sqlite3
import tkinter
from tkinter import Button, ttk, messagebox
window = tkinter.Tk()
window.title('Portal do Aluno')
window.geometry('800x600+400+50')
window.resizable(width = 1, height = 1)
window.configure(bg="DarkOrchid2")
def janela1 ():
    def janela2():
        def salvar ():
        #Validação
            window.withdraw() 
            terms = terms_reg_status_var.get()
            if terms == "Concordo":
            #Dados
                firstname = name_entry.get()
                lastname = last_name_entry.get()
                title = title_combobox.get()
                age = age_spinbox.get()
                nationality = nationality_combobox.get()
                email = email_entry.get()
                confirm_email = confirm_email_entry.get()
                cpf = cpf_entry.get()
                cellphone = cellphone_entry.get()
                password = password_entry.get()
                confirm_password =confirm_password_entry.get()
                if email != confirm_email :
                    tkinter.messagebox.showwarning(title="Erro", message="E-mail incorreto!")
                    return None
                else:
                    pass
                if password == confirm_password :
                    pass
                else:
                    tkinter.messagebox.showwarning(title="Erro", message="Senha incorreta")
                    return None
                if firstname and lastname and title and age and nationality and email and confirm_email and cpf and cellphone and password and confirm_password:
                    cep = cep_entry.get()
                    adress = adress_entry.get()
                    adress_number = adress_number_entry.get()
                    city = city_name_entry.get()
                    complement = complement_adress_entry.get()
                    distrit = distrit_name_entry.get()
                else:
                    tkinter.messagebox.showwarning(title="Erro", message="Dados incompletos!")
                print("-"*50)
                print("Pronome: ", title, ", Primeiro Nome: ", firstname, ", Cpf: ", cpf)
                print("Nacionalidade: ", nationality, ", Celular: ", cellphone, ", Idade: ", age)
                print("E-mail: ", email, ", Confirmar E-mail: ", confirm_email,)
                print("-"*50)

                #Criando a tabela de dados
                conn = sqlite3.connect('Data.db')
                table_create_query = '''CREATE TABLE IF NOT EXISTS Dados(
                    firstname TEXT, lastname TEXT, title TEXT, age INT, 
                    nationality TEXT, email TEXT,password TEXT, cpf INT,cellphone INT )'''
                conn.execute(table_create_query)
                #Adicionando dados, sempre colocar os mesmos numeros de variaveis e de interrogações em values 
                data_insert_query = '''INSERT INTO Dados(firstname,lastname,title,age,
                nationality,email,password,cpf,cellphone)VALUES(?,?,?,?,?,?,?,?,?)'''
                #Colocar apenas as variáveis na tupla!
                data_insert_tuple = (firstname,lastname,title,age,nationality,email,password,cpf,cellphone)
                #Este deve sempre deixar entre o conn.execute e o conn.close
                cursor = conn.cursor()
                #Cursor irá fazer com que seja executado a adição no banco de dados
                cursor.execute(data_insert_query,data_insert_tuple)
                #Commit irá garantir que os dados serão salvos no banco
                conn.commit()
                #Encerrará a conexão
                conn.close()
                confirmation = messagebox.askyesno(title="Confirmação?", message="Confirma os dados inseridos?")
                if confirmation == True:
                    return messagebox.showinfo(title="Parabéns", message="Seus dados foram salvos com sucesso")
                else:
                    return messagebox.showinfo(title="Que pena", message="Revise seus dados novamente!")
                    return None
            else:
                tkinter.messagebox.showwarning(title="Erro", message="Você não aceitou os termos!")

        def salvar_pagamento():
            #Pagamento
            registration = reg_status_var.get()
            if registration == "Registrado":
                creditcard = creditcard_entry.get()
                creditcard_code = creditcard_code_entry.get()
                creditcard_year = creditcard_year_entry.get()
                name_credit = name_credit_entry.get()
                print("-"*50)
                print("Registro: ", registration, ", Cartão de Crédito: ",creditcard)
                print("CVV: ", creditcard_code, "Ano: ", creditcard_year, "Nome Cartão: ", name_credit)
                print("-"*50)
                conn = sqlite3.connect('DataC.db')
                table_create_query = '''CREATE TABLE IF NOT EXISTS DadosC(
                    creditcard INT, creditcard_code INT, creditcard_year INT, name_credit TEXT)'''
                conn.execute(table_create_query) 
                data_insert_query = '''INSERT INTO DadosC(creditcard, creditcard_code, creditcard_year, name_credit)VALUES(?,?,?,?)'''
                data_insert_tuple = (creditcard,creditcard_code,creditcard_year,name_credit)
                cursor = conn.cursor()
                cursor.execute(data_insert_query,data_insert_tuple)
                conn.commit()
                conn.close()
            else:
                pass
         
        
        def voltar():
            window.deiconify()
            window1.withdraw()    
        def mostrar_senha ():
            if password_entry.cget ("show") == '*' and confirm_password_entry.cget ("show") == '*':
                password_entry.config(show='')
                confirm_password_entry.config(show='')
            else:
                password_entry.config(show='*')
                confirm_password_entry.config(show='*')
        
        #Janela principal
        
        window1 = tkinter.Tk()
        window1.title("Ficha de Cadastro",)
        window1.geometry('800x680+400+50')
        window1.resizable(width=0, height=0)
        window1.configure(bg="DarkOrchid2")

        #Divisão da janela = Frame
        frame = tkinter.Frame(window1,)
        frame.pack(padx=20,pady=20)

        #LabelFrame serve para fazer uma divisão em volta, uma caixa
        user_info_frame = tkinter.LabelFrame(frame, text="Dados do usuário")
        user_info_frame.grid(row= 0 , column= 0, sticky="news", padx=20, pady=10)

        #Titulo, Combobox = caixa com varias opções
        title_label = tkinter.Label(user_info_frame, text="Pronome: ")
        title_label.grid(row=0, column=0)
        title_combobox = ttk.Combobox(user_info_frame, values=["","Sr.", "Sra.", "Dr.", "Dra." ])
        title_combobox.grid(row = 1, column=0)

        #Etiquetas de nome
        name_label = tkinter.Label(user_info_frame, text= "Primeiro Nome: ", justify='left')
        name_label.grid(row=0, column=1)
        last_name_label = tkinter.Label(user_info_frame, text= "Ultimo Nome:")
        last_name_label.grid(row=0, column=2)

        #Espaço para nome
        name_entry = tkinter.Entry(user_info_frame)
        name_entry.grid(row=1, column=1)
        last_name_entry = tkinter.Entry(user_info_frame)
        last_name_entry.grid (row=1, column=2)

        #CPF
        cpf_label = tkinter.Label(user_info_frame, text="CPF: ")
        cpf_label.grid(row=0, column=3)
        cpf_entry = tkinter.Entry(user_info_frame)
        cpf_entry.grid(row=1, column=3)

        #Nacionalidade 
        nationality_label = tkinter.Label(user_info_frame,text="País: ")
        nationality_combobox = ttk.Combobox(user_info_frame, values=["Argentina","Bolivia","Brasil","Chile",
        "Colômbia","Equador","Guiana","Paraguai","Peru","Venezuela","Suriname","Outra País"])
        nationality_label.grid(row=2, column=0)
        nationality_combobox.grid(row=3, column=0)

        #Nº Celular
        cellphone_label = tkinter.Label(user_info_frame, text="Celular: ")
        cellphone_label.grid(row=2, column=1)
        cellphone_entry = tkinter.Entry(user_info_frame)
        cellphone_entry.grid(row=3, column=1)

        #E-mail
        email_label = tkinter.Label(user_info_frame, text="E-mail: ")
        email_label.grid(row=2, column=2)
        email_entry = tkinter.Entry(user_info_frame)
        email_entry.grid(row=3, column=2)

        #Confirmar E-mail
        confirm_email_label = tkinter.Label(user_info_frame, text="Confirmar E-mail: ")
        confirm_email_label.grid(row=2, column=3)
        confirm_email_entry = tkinter.Entry(user_info_frame)
        confirm_email_entry.grid(row=3, column=3)

        #Idade, Spinbox é uma caixa de entrada com diminuir e aumentar
        age_label = tkinter.Label(user_info_frame, text="Idade: ")
        age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110)
        age_label.grid(row=4, column=0)
        age_spinbox.grid(row=5, column=0, padx=5, pady=5)

        #Senha
        password_label = tkinter.Label(user_info_frame, text="Senha: ")
        password_label.grid(row=4, column=1)
        password_entry = tkinter.Entry(user_info_frame, show="*")
        password_entry.grid (row=5, column=1)

        #Confirmar Senha
        confirm_password_label = tkinter.Label(user_info_frame, text="Confirmar Senha: ")
        confirm_password_label.grid(row=4, column=2)
        confirm_password_entry = tkinter.Entry(user_info_frame, show="*")
        confirm_password_entry.grid (row=5, column=2)

        #Mostrar senha check button
        show_pass_var = tkinter.StringVar(value="Não mostrar")
        show_check = tkinter.Checkbutton(user_info_frame, text="Mostrar Senha",variable=show_pass_var, onvalue="Mostrar", offvalue="Não mostrar", command=mostrar_senha )
        show_check.grid(row=5, column=3)

        #dica de como ajeitar de vez o espaço corretamente
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5) #Desta forma irá configurar toda a janela de vez

        #Frame de Endereço
        adress_frame = tkinter.LabelFrame(frame, text="Endereço")
        adress_frame.grid(row=1, column=0, sticky="news",padx=20,pady=10)

        # Endereço
        cep_label = tkinter.Label(adress_frame, text="CEP: ")
        cep_label.grid(row=0, column=0)
        cep_entry = tkinter.Entry(adress_frame)
        cep_entry.grid(row=0, column=1)
        adress_label = tkinter.Label(adress_frame, text="Endereço: ")
        adress_label.grid (row=0, column=2)
        adress_entry = tkinter.Entry(adress_frame)
        adress_entry.grid(row=0, column=3)
        adress_number_label = tkinter.Label(adress_frame, text="Nº: ")
        adress_number_label.grid(row=0, column=4)
        adress_number_entry = tkinter.Entry(adress_frame)
        adress_number_entry.grid(row=0, column=5)
        complement_adress_label = tkinter.Label(adress_frame, text="Complemento: ")
        complement_adress_label.grid(row=1, column= 0)
        complement_adress_entry = tkinter.Entry(adress_frame)
        complement_adress_entry.grid(row=1, column= 1)
        city_name_label = tkinter.Label(adress_frame, text="Cidade: ")
        city_name_label.grid(row=1, column=2)
        city_name_entry = tkinter.Entry(adress_frame)
        city_name_entry.grid(row=1, column=3)
        distrit_name_label = tkinter.Label(adress_frame, text="Bairro: ")
        distrit_name_label.grid(row=1, column=4)
        distrit_name_entry = tkinter.Entry(adress_frame)
        distrit_name_entry.grid(row=1, column=5)

        for widget in adress_frame.winfo_children():
            widget.grid_configure(padx=10,pady=5) 

        #ABA DE PAGAMENTO FRAME 2
        payment_frame = tkinter.LabelFrame(frame, text="Dados para Pagamento")
        payment_frame.grid(row=2, column=0, sticky="news",padx=20,pady=10 ) #Sticky é para expandir para todas as coordenadas
        # Cartão de crédito
        creditcard_label = tkinter.Label(payment_frame, text="Número do cartão de crédito: ")
        creditcard_label.grid(row=0, column=0)
        creditcard_entry = tkinter.Entry(payment_frame)
        creditcard_entry.grid(row=0, column=1)
        creditcard_code_label = tkinter.Label(payment_frame, text="CVV:")
        creditcard_code_label.grid(row=1, column= 0)
        creditcard_code_entry = tkinter.Entry(payment_frame)
        creditcard_code_entry.grid(row=1, column= 1)
        creditcard_year_label = tkinter.Label(payment_frame, text="Ano de vencimento:")
        creditcard_year_label.grid(row=2, column=0)
        creditcard_year_entry = tkinter.Entry(payment_frame)
        creditcard_year_entry.grid(row=2, column=1)
        name_credit_label = tkinter.Label(payment_frame, text="Nome do titular do cartão de crédito: ")
        name_credit_label.grid(row=3, column=0)
        name_credit_entry = tkinter.Entry(payment_frame)
        name_credit_entry.grid(row=3, column=1)

        reg_status_var = tkinter.StringVar(value="Não registrado!")
        registered_check = tkinter.Checkbutton(payment_frame, text="Deixar salvo para uma próxima transação?", 
        variable=reg_status_var, onvalue="Registrado", offvalue="Não registrado", command=salvar_pagamento)
        registered_check.grid(row=3, column=2)

        for widget in payment_frame.winfo_children():
            widget.grid_configure(padx=5,pady=5) 

        #Termos e condições
        terms_frame = tkinter.LabelFrame(frame)
        terms_frame.grid(row=3, column=0, sticky="news",padx=20,pady=10 ) #Sticky é para expandir para todas as coordenadas
        terms_reg_status_var = tkinter.StringVar(value="Nao concordo")
        terms_reg_check = tkinter.Checkbutton(terms_frame,text="Eu aceito os termos e condições de uso presentes no contrato.", 
        variable=terms_reg_status_var, onvalue="Concordo", offvalue="Nao concordo",command=salvar)
        terms_reg_check.pack()
        
        #Botões
        save_button = tkinter.Button(frame, text="Salvar", command= salvar)
        save_button.grid (row=4, column=0, sticky="news", padx=20, pady=10)
        cancel_button = tkinter.Button(frame, text="Cancelar", command=voltar)
        cancel_button.grid (row=5, column=0,sticky="news", padx=20, pady=10)

        window1.mainloop()
        
  
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
    fg='black', font=('Arial',16),command=janela2)

    #Colocando widgets na janela
    login_label.grid(row=0, column=0, columnspan=2, sticky='news',pady=40) #news = North, East,West and South
    user_label.grid(row=1,column=0)                                        #pady = Espaçamento na vertical eixo Y
    user_entry.grid(row=1,column=1,pady=20,padx=5)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1,pady=20,padx=5)
    login_button.grid(row=3, column=0, columnspan=2,pady=30)
    register_button.grid(row=3, column=1, columnspan=2, pady=30 )
janela1()
window.mainloop()