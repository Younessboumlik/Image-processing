from MiniProjet import *
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk ,Image
from tkinter import messagebox
import ctypes as ct

fen = Tk()
fen.geometry("1360x764")
#titre de la fenetre(nom au dessus de la fenetre)
fen.title("traitement d'image ")
#icone de la fenetre
ico = Image.open("icon.jpg ")
photo = ImageTk.PhotoImage(ico)
fen.wm_iconphoto(False, photo)
#image background de la fenetre
img = Image.open("fff.jpg")
bg = ImageTk.PhotoImage(img)
label = Label(fen, image=bg)
label.place(x = -1,y = 0)
#fonction de fullscreen mode :
def fullscreen():
     fen.attributes('-fullscreen',True)
def normalscreen():
     fen.attributes('-fullscreen',False)
#fonctionne qui genere l'aide dans le programme.
def help(a):
     Fact=""
     #declaration du fichier
     f = open("help.txt","r")
     #afichage des lignes d'aide de chaque fonction.
     for i in f.readlines():
         if i[0]==a:
          Fact += i[1:]
     f.close     
     #utilisation du message box pour l'affichage de l'aide.
     messagebox.showinfo(title="function information",message=Fact)

a =1
# fonction qui change le theme de background et la couleur  des boutthon entre le noir et le blanc
def white_to_black():
   global a 
   if a == 1:
     a =0
     bg = ImageTk.PhotoImage(Image.open("fff2.jpg"))
     label.config(image=bg)
     label.place(x = -1,y = 0)
     #label.pack()
     menurgb.config(background='white', fg='black',tearoff = 0)
     menuglasial.config(background='white', fg='black',tearoff = 0)
     menuhelp.config(background='white', fg='black',tearoff = 0) 
     menuquit.config(background='white', fg='black',tearoff = 0) 
     MyEntryBox.config(bg="black",fg="white",insertbackground="white")
     MyEntryBox1.config(bg="black",fg="white",insertbackground="white")
     MyEntryBox2.config(bg="black",fg="white",insertbackground="white")
     MyEntryBox3.config(bg="black",fg="white",insertbackground="white")
     MyEntryBox4.config(bg="black",fg="white",insertbackground="white")
     MyEntryBox5.config(bg="black",fg="white",insertbackground="white") 
     MyEntryBox6.config(bg="black",fg="white",insertbackground="white") 
     MyEntryBox7.config(bg="black",fg="white",insertbackground="white") 
     MyTkButton5.config(bg="black",fg="white")
     MyTkButton6.config(bg="black",fg="white")
     MyTkButton7.config(bg="black",fg="white")
     MyTkButton2.config(bg="black",fg="white")
     MyTkButton9.config(bg="black",fg="white")
     fen.update()
     DWMWA_USE_IMMERSIVE_DARK_MODE = 20
     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
     get_parent = ct.windll.user32.GetParent
     hwnd = get_parent(fen.winfo_id())
     rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
     value = 2
     value = ct.c_int(value)
     black = ImageTk.PhotoImage(Image.open("darkmod.png"))
     butoon_whitetoblack.config(image=black)
     set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
     
     fen.mainloop()
   else :
     a =1
     black = ImageTk.PhotoImage(Image.open("daymod.png"))
     butoon_whitetoblack.config(image=black)
     fen.update()
     DWMWA_USE_IMMERSIVE_DARK_MODE = 21
     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
     get_parent = ct.windll.user32.GetParent
     hwnd = get_parent(fen.winfo_id())
     rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
     value = 3
     value = ct.c_int(value)
     menurgb.config(background='black', fg='white')
     menuglasial.config(background='black', fg='white')
     menuhelp.config(background='black', fg='white') 
     menuquit.config(background='black', fg='white') 

   
     MyEntryBox.config(bg="white",fg="black",insertbackground="black")
     MyEntryBox1.config(bg="white",fg="black",insertbackground="black")
     MyEntryBox2.config(bg="white",fg="black",insertbackground="black")
     MyEntryBox3.config(bg="white",fg="black",insertbackground="black")
     MyEntryBox4.config(bg="white",fg="black",insertbackground="black")
     MyEntryBox5.config(bg="white",fg="black",insertbackground="black") 
     MyEntryBox6.config(bg="white",fg="black",insertbackground="black") 
     MyEntryBox7.config(bg="white",fg="black",insertbackground="black") 
     MyTkButton5.config(bg="white",fg="black")
     MyTkButton6.config(bg="white",fg="black")
     MyTkButton7.config(bg="white",fg="black")
     MyTkButton2.config(bg="white",fg="black")
     MyTkButton9.config(bg="white",fg="black")
     bg = ImageTk.PhotoImage(Image.open("fff.jpg"))
     label.config(image=bg)
     label.place(x = -1,y = 0)
     #label.pack()
     fen.mainloop()    
# l'affichage d'une image de ton pc  
def ouvrir():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
 AfficherImg(ouvrirImage(fileName))
# l'affichage d'une d;une image apres la transforme en gris   
def ouvrir_rgbtoglasial():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
 AfficherImg(grayscale(ouvrirImage(fileName))) 
# la symetrie horizontale d'une image gris  
def ouvrir_inversehorizontale():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
 AfficherImg(symetrieH(ouvrirImage(fileName))) 
# la symetrie verticale d'une gris 
def ouvrir_verticale():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
 AfficherImg(symetrieV(ouvrirImage(fileName))) 
 
def ouvrire_inverser():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
 AfficherImg(inverser(ouvrirImage(fileName))) 
#l'affichge de linvere d'une image gris 
def ouvrire_iph():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
 AfficherImg(flipH(ouvrirImage(fileName))) 
def ouvrire_poserH():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))
 AfficherImg(poserH(flipH(ouvrirImage(fileName)),inverser(ouvrirImage(fileName))))
def ouvrire_poserV():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))
 AfficherImg(poserV(inverser(ouvrirImage(fileName)),flipH(ouvrirImage(fileName))) ) 
def ouvrire_constrast():
 fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))
 messagebox.showinfo(title="function information",message="la luminance de cette image est : "+str(constrast(ouvrirImage(fileName))))
def ouvrir_luminance():
     fileName = filedialog.askopenfilename(initialdir="/",title="choise a file ",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
     messagebox.showinfo(title="function information",message="la luminance de cette image est : "+str(luminance(ouvrirImage(fileName))))  
# affichage d'un message pour l'aide 
def ouvrir_help1():
     help("1")
def ouvrir_help2():
     help("2")
def ouvrir_help3():
     help("3")
def ouvrir_help4():
     help("4")
def ouvrir_help5():
     help("5")
def ouvrir_help6():
     help("6")
def ouvrir_help7():
     help("7")
def ouvrir_help8():
     help("8")
def ouvrir_help9():
     help("9")
def ouvrir_help10():
     help("%")
def ouvrir_help11():
     help("#")
def ouvrir_help12():
     help("*")
def ouvrir_help13():
     help("((")
def ouvrir_help14():
     help("0")
def ouvrir_apropos():
     help("!")     
                                                                    

#des fonctions qui renvois tous ce qui est ecrits dans  
def Get_MyInputValue():
     getresult = MyEntryBox.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les")=='ok'
     elif  int(getresult)<1000:
      return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
         

def Get_MyInputValue1():
     getresult = MyEntryBox1.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les cases.")=='ok'
     elif  int(getresult)<1000:
          return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
         
def Get_MyInputValue2():
     getresult = MyEntryBox2.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les cases.")=='ok'
     elif  int(getresult)<1000:
          return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
         
def Get_MyInputValue3():
     getresult = MyEntryBox3.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les cases.")=='ok'
     elif  int(getresult)<1000:
          return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
         
def Get_MyInputValue4():
     getresult = MyEntryBox4.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les cases.")=='ok'
     elif  int(getresult)<1000:
          return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
         
def Get_MyInputValue5():
     getresult = MyEntryBox5.get()
   
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les cases.")=='ok'
     elif  int(getresult)<1000:
             return int(getresult)         
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
def Get_MyInputValue6():
     getresult = MyEntryBox6.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les")=='ok'
     elif  int(getresult)<1000:
      return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
def Get_MyInputValue7():
     getresult = MyEntryBox7.get()
     if str(getresult)=='':
          messagebox.showerror("Erreur", "Erreur\nIl faut remplir les")=='ok'
     elif  int(getresult)<1000:
      return int(getresult)
     else:
          if messagebox.askquestion("Attention", "La valeur entree est un peu grande.\nEst ce que tu veux continuer??")=='yes':
               return int(getresult)
                                     
def ouvrire_creeimagealea():
    a = [[[0]*3 for j in range(6)]for i in range(3)]
    AfficherImg( image_noire(Get_MyInputValue(),Get_MyInputValue1()))
    MyEntryBox.delete(0, END)
    MyEntryBox1.delete(0,END)
def ouvrire_creeimagealeacouleur():
    a = [[[0]*3 for j in range(Get_MyInputValue2())]for i in range(Get_MyInputValue3())]
    AfficherImg(initImageRGB(a)) 
    MyEntryBox2.delete(0, END)
    MyEntryBox3.delete(0,END)
def ouvrire_creeimage_blan_noir():
    AfficherImg(creerImgBlancNoir(Get_MyInputValue4(),Get_MyInputValue5()))
    
def ouvrir_negative():
         AfficherImg(negatif(creerImgBlancNoir(Get_MyInputValue4(),Get_MyInputValue5())))
         MyEntryBox4.delete(0, END)
         MyEntryBox5.delete(0,END)
def ouvrir_blanche():
     AfficherImg(image_blanche(Get_MyInputValue6(),Get_MyInputValue7()))
     MyEntryBox6.delete(0, END)
     MyEntryBox7.delete(0,END)
from random import choice
a = choice(["green","red","blue"])
Label(fen, text="Entrer L ligne et C colone de l'image noire",bg="black",fg="white",font=15).place(x=75, y=30)    
Label(fen, text="Entrer L ligne et C colone de l'image en couleur aleatoire",bg=a,fg="black",font=15).place(x=40, y=260)    
Label(fen, text="cree image noir et blanc",font=15).place(x=140, y=460) 
Label(fen, text="cree image blanc",font=15).place(x=750, y=460)    
MyEntryBox = Entry(fen, width=20)
MyEntryBox.place(x=80, y=70)
MyEntryBox1 = Entry(fen, width=20)
MyEntryBox1.place(x=232, y=70)    

 
MyTkButton2 = Button(fen, height=2, width=20, text="cree", command= ouvrire_creeimagealea)
MyTkButton2.place(x=140, y = 100)    
MyEntryBox2 = Entry(fen, width=20)
MyEntryBox2.place(x=80, y=300)
MyEntryBox3 = Entry(fen, width=20)
MyEntryBox3.place(x=232, y=300)    

MyTkButton5 = Button(fen, height=2, width=20, text="cree", command= ouvrire_creeimagealeacouleur)
MyTkButton5.place(x=140, y = 330) 
MyEntryBox4 = Entry(fen, width=20)
MyEntryBox4.place(x=80, y=500)
MyEntryBox5 = Entry(fen, width=20)
MyEntryBox5.place(x=232, y=500)
MyTkButton6 = Button(fen, height=2, width=20, text="cree", command= ouvrire_creeimage_blan_noir)
MyTkButton6.place(x=140, y = 540)   
MyTkButton7 = Button(fen, height=2, width=20, text="cree le negative", command= ouvrir_negative)
MyTkButton7.place(x=140, y = 600)
MyEntryBox6 = Entry(fen, width=20)
MyEntryBox6.place(x=672, y=500)
MyEntryBox7 = Entry(fen, width=20)
MyEntryBox7.place(x=820, y=500)
MyTkButton9 = Button(fen, height=2, width=20, text="cree", command= ouvrir_blanche)
MyTkButton9.place(x=740, y = 540)
black= ImageTk.PhotoImage(Image.open("daymod.png"))
butoon_whitetoblack = Button(fen,height=70,image=black,borderwidth=0,width=145,text="cree",command=white_to_black)
butoon_whitetoblack.place(x=1200,y=30)



menubar = Menu(fen)
menurgb = Menu(menubar,background='black', fg='white',tearoff=0)
menuglasial = Menu(menubar,background='black', fg='white',tearoff=0)
menuhelp = Menu(menubar,background='black', fg='white',tearoff=0)
menuquit = Menu(menubar,background='black', fg='white',tearoff=0)
#menu bar:
menubar.add_cascade(label="Image en couleur",menu=menurgb)
menubar.add_cascade(label="Image en niveau de gris ",menu=menuglasial)
menubar.add_cascade(label="?",menu=menuhelp)
menubar.add_cascade(label="Quiter",menu=menuquit)
#les commandes de chaque menu bar:
menurgb.add_command(label = "Affichier image rgb",command =ouvrir)
menurgb.add_command(label = "Retourner une image au en niveau de gris ",command =ouvrir_rgbtoglasial)
menurgb.add_command(label = "Inverser l'image horizontalement",command =ouvrir_inversehorizontale)
menurgb.add_command(label = "Verticale",command =ouvrir_verticale)
menuglasial.add_command(label="Enverse de degre de gris",command =ouvrire_inverser)
menuglasial.add_command(label="inverse limage verticalement ",command =ouvrire_iph)
menuglasial.add_command(label="poserH",command =ouvrire_poserH)
menuglasial.add_command(label="poserV",command =ouvrire_poserV)
menuglasial.add_command(label="Calculer luminance",command =ouvrir_luminance)
menuglasial.add_command(label="Calculer contrast",command =ouvrire_constrast)
menuhelp.add_command(label="image_noire()",command=ouvrir_help1)
menuhelp.add_command(label="image_blanch()",command=ouvrir_help2)
menuhelp.add_command(label="creeimageblanchNoir()",command=ouvrir_help3)
menuhelp.add_command(label="negative()",command=ouvrir_help4)
menuhelp.add_command(label="luminance()",command=ouvrir_help5)
menuhelp.add_command(label="canstract()",command=ouvrir_help6)
menuhelp.add_command(label="profondeur()",command=ouvrir_help7)
menuhelp.add_command(label="inverser()",command=ouvrir_help8)
menuhelp.add_command(label="flpih()",command=ouvrir_help9)
menuhelp.add_command(label="iposerV()",command=ouvrir_help10)
menuhelp.add_command(label="poserH()",command=ouvrir_help11)
menuhelp.add_command(label="init_imageRGB()",command=ouvrir_help12)
menuhelp.add_command(label="symetrie()",command=ouvrir_help13)
menuhelp.add_command(label="gryscale()",command=ouvrir_help14)
menuhelp.add_separator()
menuhelp.add_command(label="fullscreen mode",command=fullscreen)
menuhelp.add_command(label="normal mode",command=normalscreen)
menuhelp.add_command(label="About ",command=ouvrir_apropos)


def quit1():
      if messagebox.askquestion("askquestion", "Are you sure?")=='yes':
          fen.quit()
menuquit.add_command(label = "Quiter la fenetre ",command=quit1)
#shortucts:
def fullscreen(event):
    fen.attributes('-fullscreen',True)
def normalscreen(event):
     fen.attributes('-fullscreen',False)
fen.bind('<Control-x>',quit)
fen.bind('<Control-f>',fullscreen)
fen.bind('<Control-n>',normalscreen)
fen.config(menu=menubar)
fen.mainloop()