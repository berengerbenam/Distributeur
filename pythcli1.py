import socket
from tkinter import *
from tkinter.messagebox import *
from time import *

adresseIP = "127.0.0.1"	# Ici, le poste local
port = 50001	# Se connecter sur le port 50000

fen = Tk()

#POUR LES OPERATIONS
#def depot():
    #global montant
    #montant = str(montant.get())
    #client.send(("DEPOT " + nocompte + " " + montant).encode("utf-8"))
    #reponse = client.recv(255).decode("utf-8")
    #print(reponse)

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
    
def oper():
    global operation,montant,nocompteDestination
    operation = str(operation.get())
    #op.deiconify()
    #op1 = Toplevel()
    #op1.deiconify()
    #def callback():
       # if askyesno('Envoie','Êtes vous sûr de vouloir envoyer?'):
           # showwarning('Transfert','Transfert éffectué')
        #else:
            #showinfo('Transfert','Transfert Non éffectué')



    def transfert():
        global montant,nocompteDestination,nocompte
        montant = str(montant.get())
        nocompteDestination = str(nocompteDestination.get())
        #nocompte = str(nocompte.get())
        if askyesno('Envoie','Êtes vous sûr de vouloir envoyer?'):
            client.send(("TRANSFERT " + nocompte + " " + nocompteDestination + " " + montant).encode("utf-8"))
            reponse = client.recv(255).decode("utf-8")
            if reponse == "TRANSFERT OK":
                showinfo('Transfert',"Transfert effectué")
            else:
                showinfo('Transfert',"Transfert refusé")
        else:
            showinfo('annulé')
    def retrait():
        global montant,nocompte
        
        montant = str(- float(montant.get()))     # Le montant doit être négatif
        
        client.send(("RETRAIT " + nocompte + " " + montant).encode("utf-8"))
        reponse = client.recv(255).decode("utf-8")
        if reponse == "RETRAIT OK":
            showinfo('Retrait',"Retrait effectué")
        else:
            showinfo('Retrait',"Retrait refusé")

    def depot():
        global montant,nocompte
        montant = str(montant.get())
        client.send(("DEPOT " + nocompte + " " + montant).encode("utf-8"))
        reponse = client.recv(255).decode("utf-8")
        showinfo('Dépôt',reponse)
   

    if operation == "1":
        #montant = input("Entrez le montant à déposer : ")
        #op1 = Toplevel()
        #POUR LE MONTANT
        op1 = Toplevel()
        op1.geometry("400x80")
        op1.title("Depot")
        
   #" def depot():
    #    global montant
     #   montant = str(montant.get())
      #  print(nocompte)
       # print(montant)
       # client.send(("DEPOT " + nocompte + " " + montant).encode("utf-8"))
       # reponse = client.recv(255).decode("utf-8")
        #print(reponse)"

        montant = StringVar()
        Label(op1,text="Entrez le montant à déposer : ").place(x=0,y=0)
        text=Entry(op1,textvariable=montant,relief="raised")
        text.place(x=200,y=0)
        boutonSend=Button(op1,text="Déposer",activebackground="green",command=depot)
        

        boutonSend.place(x=300,y=40)
    
    

    
    elif operation == "2":
        op2=Toplevel()
        op2.geometry("400x80")
        op2.title("Retrait")
        montant = StringVar()
        Label(op2,text="Entrez le montant à retirer : ").place(x=0,y=0)

        #montant = str(- float(montant.get()))     # Le montant doit être négatif
        Entry(op2,textvariable=montant,relief="solid").place(x=200,y=0)
        boutonSend1=Button(op2,text="Retirer",activebackground="red",relief="raised",command=retrait)
        boutonSend1.place(x=300,y=40)
        #client.send(("RETRAIT " + nocompte + " " + montant).encode("utf-8"))
        #reponse = client.recv(255).decode("utf-8")
        #if reponse == "RETRAIT OK":
        #    print("Retrait effectué")
        #else:
            #print("Retrait refusé")
    elif operation == "3":
        op3=Toplevel()
        op3.geometry("500x150")
        op3.title("Transfert")
        montant = StringVar()
        nocompteDestination = StringVar()
        Label(op3,text="Entrez le montant à transferer : ").place(x=0,y=0)
        Entry(op3,textvariable=montant,relief="solid").place(x=230,y=0)
        Label(op3,text="Entrez le numéro de compte du bénéficiaire:").place(x=0,y=60)
        Entry(op3,textvariable=nocompteDestination).place(x=315,y=60)
        Button(op3,text="Transferer",relief="ridge",command=transfert).place(x=0,y=100)

        

        
        #client.send(("TRANSERT " + nocompte + " " + nocompteDestination + " " + montant).encode("utf-8"))
        #reponse = client.recv(255).decode("utf-8")
        #if reponse == "TRANSERT OK":
         #   print("Transfert effectué")
        #else:
        #    print("Transfert refusé")
    elif operation == "4":
        client.send(("HISTORIQUE " + nocompte).encode("utf-8"))
        historique = client.recv(4096).decode("utf-8").replace("HISTORIQUE ","")    # On transfert un grand volume de données
        showinfo('HISTORIQUE',historique)
    elif operation == "5":
        client.send(("SOLDE " + nocompte).encode("utf-8"))
        solde = client.recv(4096).decode("utf-8").replace("SOLDE ","")
        showinfo('solde',"Le solde du compte est de " + solde)
        
    
#SOUS PROGRAMME POUR LE NUMERO DE COMPTE ET LE CODE PIN
def send():
    global nocompte,pin
    fen.deiconify()
    nocompte=str(nocompte.get())
    pin=str(pin.get())
    client.send(("TESTPIN " + nocompte + " " + pin).encode("utf-8"))
    reponse = client.recv(255).decode("utf-8")
    fen.withdraw()
    op=Toplevel()
    op.geometry("500x500")
    if reponse == "TESTPIN OK":
        Label(op,text="Bienvenue !").place(x=250,y=0)
        Label(op,text="Opérations :\n").place(x=0,y=20)
        Label(op,text="1 - Dépôt\n").place(x=0,y=60)
        Label(op,text="2 - Retrait\n").place(x=0,y=120)
        Label(op,text="3 - Transfert\n").place(x=0,y=180)
        Label(op,text="4 - Historique des opérations\n").place(x=0,y=240)
        Label(op,text="5 - Solde du compte\n").place(x=0,y=300)
        Label(op,text="Entrez l'opération que vous souhaitez :").place(x=0,y=360)
        text3=Entry(op,textvariable=operation)
        text3.place(x=280,y=360)
        bouton1=Button(op,text="Valider",activebackground="blue",command=oper)
        bouton1.place(x=420,y=390)
        
        
    else:
        showinfo('alert',"Vos identifiants sont incorrects")
        showinfo("'BYE',Au revoir !")
    #client.close()


    

#fen.geometry("500X500")
while True:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((adresseIP, port))
    
    #print("Bienvenue dans la banque Python")
    lab1=Label(fen,text="GAB",font=(35),width=40,bg="silver",fg="blue")
    lab2=Label(fen,text="Entrez votre numéro de compte :")
   
    nocompte = StringVar()
    text1=Entry(fen, textvariable=nocompte,relief="groove")
    

    lab3=Label(fen, text="Entrez votre code PIN:")
    label = Label(fen,font=("ds-digittal",13),background="black",foreground="silver")
    label.place(x=0,y=75)
    time()
    pin = StringVar()
    text2=Entry(fen, textvariable=pin,relief="groove")
    bouton=Button(fen,text="Valider",command=send)    
    operation=StringVar()

    lab1.grid(row=0,column=2)
    lab2.grid(row=1,column=1)
    lab3.grid(row=2,column=1)
    text1.grid(row=1,column=2)
    text2.grid(row=2,column=2)
    
    bouton.grid(row=4,column=4)
    fen.mainloop()   
