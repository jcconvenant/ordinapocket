#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
if sys.version_info >= (3,):
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox
else:
    from Tkinter import *
    import tkFileDialog
    import tkMessageBox
from time import sleep
import os

class Afficheur(Frame):
    'afficheur 7 segments ; respecter la proportion largeur x hauteur'

    def __init__(self, boss=None, la=140, ha=200):
        Frame.__init__(self, boss)
        self.configure(bg='grey40', bd=0, relief=FLAT)
        self.lst = []
        self.code = {1: (2, 3), 2: (1, 2, 7, 5, 4), 3: (1, 2, 7, 3, 4), 4: (6, 7, 2, 3), 5: (1, 6, 7, 3, 4), 6: (1, 6, 5, 4, 3, 7), 7: (1, 2, 3), 8: (1, 2, 3, 4, 5, 6, 7), 9: (6, 1, 2, 3, 4, 7), 0: (1, 2, 3, 4, 5, 6)}
        dic = {1: (40, 40, 100, 30), 2: (100, 40, 110, 90), 3: (100, 100, 110, 160), 4: (40, 160, 100, 170), 5: (30, 160, 40, 100), 6: (40, 90, 30, 40), 7: (40, 90, 100, 100)}
        self.can = Canvas(self, bg='black', relief=RAISED, width=la, height=ha)
        self.can.pack()
        liste = []
        dx, dy = la/140.0, ha/200.0
        for i in [1, 2, 3, 4, 5, 6, 7]:
            v = dic[i]
            liste.append(v)
            for w, x, y, z in liste:
                p = self.can.create_rectangle(w*dx, x*dy, y*dx, z*dy, fill='black')
                self.lst.append(p)
                liste = []
        self.allume = False
        self.chiffre = -1

    def __del__(self):
        self.can.delete(ALL)

    def affiche(self, arg=None):
        self.initialisation()
        v = list(self.code[arg])
        for i in v:
            self.can.itemconfig(i, fill='red')
        self.allume = True
        self.chiffre = arg

    def initialisation(self):
        for i in self.lst:
            self.can.itemconfig(i, fill='black')
        self.allume = False
        self.chiffre = -1

class Afficheur3chiffres(Frame):
    'triple afficheur 7 segments'

    def __init__(self, boss=None, la=140, ha=200):
        Frame.__init__(self, boss)
        dx, dy = la/140.0, ha/200.0
        self.configure(width=560*dx, height=280*dy, bg='grey80', relief=FLAT)
        self.chiffreu = Afficheur(self, la, ha)
        self.chiffred = Afficheur(self, la, ha)
        self.chiffrec = Afficheur(self, la, ha)
        self.chiffrec.place(x=35*dx, y=40*dy, anchor=NW)
        self.chiffred.place(x=210*dx, y=40*dy, anchor=NW)
        self.chiffreu.place(x=385*dx, y=40*dy, anchor=NW)

    def affiche(self, arg=None):
        if not self.chiffreu.allume:
            self.chiffreu.affiche(arg)
        elif not self.chiffred.allume:
            self.chiffred.affiche(self.chiffreu.chiffre)
            self.chiffreu.affiche(arg)
        elif not self.chiffrec.allume:
            self.chiffrec.affiche(self.chiffred.chiffre)
            self.chiffred.affiche(self.chiffreu.chiffre)
            self.chiffreu.affiche(arg)

    def affiche_nombre(self, arg=None):
        self.initialisation()
        nb = int(arg)
        c, d = (0, 0)
        if int(nb/100) != 0:
            c = int(nb/100)
            self.affiche(c)
            nb = nb - c*100
        if c != 0 or int(nb/10) != 0:
            d = int(nb/10)
            self.affiche(d)
            nb = nb - d*10
        self.affiche(nb)

    def initialisation(self):
        self.chiffreu.initialisation()
        self.chiffred.initialisation()
        self.chiffrec.initialisation()

    def get(self):
        nb = 0
        if self.chiffreu.chiffre != -1:
            nb = self.chiffreu.chiffre
        if self.chiffred.chiffre != -1:
            nb = nb + self.chiffred.chiffre*10
        if self.chiffrec.chiffre != -1:
            nb = nb + self.chiffrec.chiffre*100
        return nb

class Clavier(Frame):
    'clavier numerique'

    def __init__(self, boss=None, pafficheur=None):
        Frame.__init__(self, boss)
        self.configure(bd=0, relief=FLAT, bg='grey80')
        self.f1 = Frame(self, bd=0)
        self.f1.grid(row=0, column=1)
        self.led = pafficheur
        self.entree = IntVar()
        self.aff = StringVar()
        Label(self, width=3, relief='flat', bd=2, textvariable=self.aff, font='arial 10 italic').grid(row=1, column=1, columnspan=3, padx=2, pady=2)
        Button(self, text='1', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='1': self.saisie(arg)).grid(row=2, column=1, padx=2, pady=2)
        Button(self, text='2', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='2': self.saisie(arg)).grid(row=2, column=2, padx=2, pady=2)
        Button(self, text='3', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='3': self.saisie(arg)).grid(row=2, column=3, padx=2, pady=2)
        Button(self, text='4', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='4': self.saisie(arg)).grid(row=3, column=1, padx=2, pady=2)
        Button(self, text='5', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='5': self.saisie(arg)).grid(row=3, column=2, padx=2, pady=2)
        Button(self, text='6', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='6': self.saisie(arg)).grid(row=3, column=3, padx=2, pady=2)
        Button(self, text='7', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='7': self.saisie(arg)).grid(row=4, column=1, padx=2, pady=2)
        Button(self, text='8', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='8': self.saisie(arg)).grid(row=4, column=2, padx=2, pady=2)
        Button(self, text='9', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='9': self.saisie(arg)).grid(row=4, column=3, padx=2, pady=2)
        Button(self, text='0', font='arial 10 bold', bg='white', relief=FLAT, command=lambda arg='0': self.saisie(arg)).grid(row=5, column=1, padx=2, pady=2)
        Button(self, text='J', font='msam10 8 bold', width='5', height='1', bg='white', relief=FLAT, command=self.effacer).grid(row=5, column=2, columnspan=2, padx=2, pady=2)
        Button(self, text='      Entrée     ', font='arial 10 bold', bg='white', relief=FLAT, command=self.fin_saisie).grid(row=6, column=1, columnspan=3, padx=2, pady=2)
        self.bind('<Key>', self.touche)

    def touche(self, event=None):
        'capture du clavier pour utilisation sans cliquer sur les boutons'
        try:
            a = int(event.char)
        except:
            pass
        self.saisie(str(a))

    def saisie(self, pc):
        ch = self.aff.get()
        if len(ch) > 2:
            ch = ch[1:]
        self.aff.set(ch + pc)

    def fin_saisie(self):
        'fin de la saisie par la touche Entree'
        self.entree.set(int(self.aff.get()))

    def effacer(self):
        ch = self.aff.get()
        self.aff.set(ch[:-1])

    def reset(self):
        self.aff.set('')

class OPMenus(Frame):
    'barre des menus avec ses menus'

    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(relief=RAISED, borderwidth=2)
        self.pack(side=TOP, fill='x')
        self.mbfic = Menubutton(self, text='Fichier')
        self.mbfic.pack(side=LEFT)
        self.mbfic.menu = Menu(self.mbfic, tearoff=0)
        self.mbfic['menu'] = self.mbfic.menu
        self.mbfic.menu.add_command(label='Nouveau', underline=0, command=self.nouveau)
        self.mbfic.menu.add_command(label='Ouvrir', underline=0, command=self.ouvrir)
        self.mbfic.menu.add_command(label='Sauver', underline=0, command=self.sauver)
        self.mbfic.menu.add_separator()
        self.mbfic.menu.add_command(label='Quitter', underline=0, command=AskQuit)
        self.mbexe = Menubutton(self, text='Execution')
        self.mbexe.pack(side=LEFT)
        self.mbexe.menu = Menu(self.mbexe, tearoff=0)
        self.mbexe['menu'] = self.mbexe.menu
        self.mbexe.menu.add_command(label='Rapide', underline=0, command=lambda arg=False: OPProgramme(arg))
        self.mbexe.menu.add_command(label='Pas a pas', underline=0, command=lambda arg=True: OPProgramme(arg))
        self.mbdes = Menubutton(self, text='Desassemblage')
        self.mbdes.pack(side=LEFT)
        self.mbdes.menu = Menu(self.mbdes, tearoff=0)
        self.mbdes['menu'] = self.mbdes.menu
        self.mbdes.menu.add_command(label='Interne', underline=0, command=OPDesassembleI)
        self.mbdes.menu.add_command(label='Externe', underline=0, command=OPDesassembleE, state='disabled')
        self.mbhlp = Button(self, text='Aide', relief=FLAT, command=self.aide)
        self.mbhlp.pack(side=RIGHT)

    def nouveau(self):
        "rien pour l'instant"
        zm.initialisation()

    def ouvrir(self):
        "chargement d'un programme en memoire"
        if sys.version_info >= (3,):
            fic = filedialog.askopenfilename(filetypes=(('Ordinapoche', '*.ord'), ('Tout', '*.*')))
        else:
            fic = tkFileDialog.askopenfilename(filetypes=(('Ordinapoche', '*.ord'), ('Tout', '*.*')))
        if fic != '':
            try:
                fd = open(fic, 'r')
            except:
                print('[ERREUR] impossible de lire le programme')
                return
            i = 0
            for cell in fd:
                zm.mem[i].set(cell.rstrip('\n\r'))
                i = i + 1
            fd.close()

    def sauver(self):
        'sauvegarde de la RAM dans sa totalite'
        if sys.version_info >= (3,):
            fic = filedialog.asksaveasfilename(filetypes=(('Ordinapoche', '*.ord'), ('Tout', '*.*')))
        else:
            fic = tkFileDialog.asksaveasfilename(filetypes=(('Ordinapoche', '*.ord'), ('Tout', '*.*')))
        if fic != '':
            try:
                fd = open(fic, 'w')
            except:
                print('[ERREUR] impossible de sauver le programme')
                return
            for i in range(100):
                fd.write('%s\n' % zm.mem[i].get())
            fd.close()

    def aide(self):
        "fenetre d'aide"
        hlp = Toplevel()
        hlp.title('Aide en ligne')
        hlp.resizable(width=False, height=False)
        lcode = (' Code   Inst. Signification                                               ', "  0      INP   lecture d'une donnee depuis un peripherique d'entree", "  1      OUT   affichage d'une donnee sur un peripherique de sortie", "  2      CLA   mise a zero d'ACC et addition", "  3      STO   stockage de l'ACC en memoire centrale", "  4      ADD   addition du contenu de la memoire a l'ACC", "  5      SUB   soustraction du contenu de la memoire a l'ACC", "  6      SHT   decalage a gauche puis a droite du contenu de l'ACC", '  7      JMP   saut inconditionnel', '  8      TAC   saut conditionnel : si (ACC != 0) alors CO=adresse', '  9      HRS   fin de programme et remise a zero des registres')
        tbg = ['black', 'grey', 'grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'green4', 'green4', 'orange']
        tfg = ['white', 'black', 'black', 'DeepSkyBlue', 'DeepSkyBlue', 'DeepSkyBlue', 'DeepSkyBlue', 'DeepSkyBlue', 'PaleGreen1', 'PaleGreen1', 'red']
        i = 0
        for li in lcode:
            Label(hlp, width=60, text=li, relief='raised', bd=2, bg=tbg[i], fg=tfg[i], anchor='w').pack(side=TOP)
            i = i + 1

class OPCanvas(Frame):
    'Zone principale : UC+clavier+ecran / RAM'

    def __init__(self, master=None):
        'constructeur'
        Frame.__init__(self)
        self.c = Canvas(self, width=800, height=600, bg='grey40')
        self.c.pack()
        self.pack(side=LEFT)
        self.tracerprocesseur()
        self.tracerual()
        self.creeracc()
        self.creerri()
        self.creerdec()
        self.creerco()
        self.ecran = Afficheur3chiffres(self, 70, 100)
        self.c.create_window(60, 380, window=self.ecran, anchor=NW)
        self.clavier = Clavier(self, self.ecran)
        self.c.create_window(500, 380, window=self.clavier, anchor=NW)

    def tracerprocesseur(self):
        'dessin du processeur central'
        self.c.create_rectangle(0, 0, 799, 320, fill='green4')
        self.c.create_rectangle(50, 290, 740, 30, fill='black')
        self.c.create_line(395, 30, 395, 290, fill='dark grey', dash=(4, 4))
        self.c.create_text(390, 280, text='U.A.L.', fill='DeepSkyBlue', anchor=E)
        self.c.create_text(405, 280, text='U.C.', fill='PaleGreen1', anchor=W)
        for i in range(31, 690, 69):
            self.c.create_polygon(i + 50, 30, i + 50, 10, i + 58, 10, i + 58, 30, i + 50, 30, fill='grey', outline='black')
            self.c.create_polygon(i + 50, 290, i + 50, 310, i + 58, 310, i + 58, 290, i + 50, 290, fill='grey', outline='black')

    def tracerual(self):
        "dessin de l'architecture interne : l'UAL"
        self.c.create_polygon(148, 147, 212, 147, 260, 243, 212, 243, 180, 179, 148, 243, 100, 243, fill='blue')
        self.c.create_line(212, 115, 287, 115, 287, 270, 239, 270, 239, 243, fill='#84FF84', arrow='last', joinstyle='bevel')
        self.c.create_line(212, 120, 282, 120, 282, 265, 244, 265, 244, 243, fill='#84FF84', arrow='last', joinstyle='bevel')
        self.c.create_line(212, 125, 277, 125, 277, 260, 249, 260, 249, 243, fill='#84FF84', arrow='last', joinstyle='bevel')
        self.c.create_line(111, 243, 111, 260, 83, 260, 83, 60, 690, 60, 690, 97, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(116, 243, 116, 265, 78, 265, 78, 55, 695, 55, 695, 92, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(121, 243, 121, 270, 73, 270, 73, 50, 700, 50, 700, 87, fill='#84FF84', joinstyle='bevel')

    def creeracc(self):
        'registre ACC'
        self.facc = Frame(self, relief='ridge', borderwidth=4, bg='blue')
        self.lacc = Label(self.facc, text='ACC', bg='blue', fg='DeepSkyBlue')
        self.acc = StringVar()
        self.eacc = Entry(self.facc, width=4, relief='flat', bd=2, textvariable=self.acc)
        self.lacc.pack(side=LEFT, padx='1m', pady='1m')
        self.eacc.pack(side=LEFT, padx='1m', pady='1m')
        self.c.create_window(180, 120, window=self.facc)
        self.c.create_line(180, 115, 83, 115, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(180, 120, 78, 120, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(180, 125, 73, 125, fill='#84FF84', joinstyle='bevel')

    def creertmp(self):
        'registre TMP'
        self.ftmp = Frame(self, relief='ridge', borderwidth=4, bg='blue')
        self.ltmp = Label(self.ftmp, text='TMP', bg='blue', fg='DeepSkyBlue')
        self.tmp = StringVar()
        self.etmp = Entry(self.ftmp, width=4, relief='flat', bd=2, textvariable=self.tmp)
        self.ltmp.pack(side=LEFT, padx='1m', pady='1m')
        self.etmp.pack(side=LEFT, padx='1m', pady='1m')
        self.c.create_window(180, 82, window=self.ftmp)
        self.c.create_line(180, 77, 83, 77, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(180, 82, 78, 82, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(180, 87, 73, 87, fill='#84FF84', joinstyle='bevel')

    def creerri(self):
        'registre RI'
        self.fri = Frame(self, relief='ridge', borderwidth=4, bg='green4')
        self.lri = Label(self.fri, text='RI', bg='green4', fg='PaleGreen1')
        self.ri = StringVar()
        self.eri = Entry(self.fri, width=4, relief='flat', bd=2, textvariable=self.ri)
        self.lri.pack(side=LEFT, padx='1m', pady='1m')
        self.eri.pack(side=LEFT, padx='1m', pady='1m')
        self.c.create_window(580, 92, window=self.fri)
        self.c.create_line(600, 87, 800, 87, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(600, 92, 800, 92, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(600, 97, 800, 97, fill='#84FF84', joinstyle='bevel')

    def creerdec(self):
        'decodeur'
        self.fdec = Frame(self, relief='ridge', borderwidth=4, bg='green4')
        self.dec = StringVar()
        self.dec.set('')
        self.ldec = Label(self.fdec, width=25, height=3, relief='flat', bd=2, textvariable=self.dec, wraplength=160, justify=LEFT, font='courier 8 italic')
        self.ldec.pack(side=TOP, padx='1m', pady='1m')
        self.c.create_window(580, 145, window=self.fdec)
        self.c.create_line(575, 100, 575, 120, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(580, 100, 580, 120, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(585, 100, 585, 120, fill='#84FF84', joinstyle='bevel')

    def creerco(self):
        'registre CO'
        self.fco = Frame(self, relief='ridge', borderwidth=4, bg='green4')
        self.lco = Label(self.fco, text='CO', bg='green4', fg='PaleGreen1')
        self.co = StringVar()
        self.eco = Entry(self.fco, width=4, relief='flat', bd=2, textvariable=self.co)
        self.lco.pack(side=LEFT, padx='1m', pady='1m')
        self.eco.pack(side=LEFT, padx='1m', pady='1m')
        self.c.create_window(580, 255, window=self.fco)
        self.c.create_line(600, 253, 800, 253, fill='#84FF84', joinstyle='bevel')
        self.c.create_line(600, 258, 800, 258, fill='#84FF84', joinstyle='bevel')

class OPMemoire(Frame):
    'Zone secondaire : RAM'

    def __init__(self, master=None):
        'constructeur'
        Frame.__init__(self)
        self.pack(side=LEFT)
        self.txt = Label(self, text='Mémoire')
        self.txt.pack(side=TOP)
        self.bidon = Label(self)
        self.bidon.pack(side=TOP)
        self.f1 = Frame(self)
        self.f1.pack(side=TOP)
        self.f1.cmem = Canvas(self, width=96, height=550, scrollregion='0 0 0 3600', yscrollincrement=36)
        self.f1.smem = Scrollbar(self, command=self.f1.cmem.yview)
        self.f1.smem.pack(side=RIGHT, fill=Y)
        self.f1.cmem.config(yscrollcommand=self.f1.smem.set)
        self.f1.cmem.pack(side=LEFT, fill=X)
        self.mem = [0]*100
        self.fmem = [0]*100
        j = 0
        for i in range(0, 3600, 36):
            self.fmem[j] = Frame(self, relief=RIDGE, borderwidth=4)
            labj = str(j)
            if j < 10:
                labj = '0' + labj
            Label(self.fmem[j], text=labj).pack(side=LEFT, padx='1m', pady='1m')
            self.mem[j] = StringVar()
            Entry(self.fmem[j], width=4, relief=SUNKEN, bd=2, textvariable=self.mem[j]).pack(side=LEFT, padx='1m', pady='1m')
            self.f1.cmem.create_window(45, i, window=self.fmem[j], anchor=N)
            j = j + 1
        self.oldadr = 0

    def initialisation(self):
        'reset du contenu de la memoire centrale'
        for i in range(0, 100):
            self.mem[i].set('')
            self.fmem[i].configure(bg='#d9d9d9')
            self.f1.cmem.yview('moveto', 0)

    def surligner(self, padr):
        "on met en evidence la cellule memoire d'adresse padr"
        self.fmem[self.oldadr].configure(bg='#d9d9d9')
        self.oldadr = padr
        self.fmem[padr].configure(bg='yellow')
        self.f1.cmem.yview('moveto', padr/100.0 - 0.0123)

    def nonsurligner(self):
        self.fmem[self.oldadr].configure(bg='#d9d9d9')

def OPErreur(pmesg, padr=None):
    zc.ldec.configure(fg='red')
    if padr != None:
        zc.dec.set(padr + ': ' + pmesg)
    else:
        zc.dec.set(pmesg)

def OPDecodage(pmesg):
    zc.ldec.configure(fg='black')
    zc.dec.set(pmesg)

def PasSuivant(padr):
    if sys.version_info >= (3,):
        rep = messagebox.askokcancel('Pas a pas', "Prochaine instruction executee a l'adresse " + str(padr).zfill(2) + '. Continuer ?')
    else:
        rep = tkMessageBox.askokcancel('Pas a pas', "Prochaine instruction executee a l'adresse " + str(padr).zfill(2) + '. Continuer ?')
    if rep:
        zm.surligner(padr)
    else:
        zm.nonsurligner()
    return rep

def OPProgramme(ppas):
    zc.acc.set('')
    zc.ri.set('')
    zc.ecran.initialisation()
    pas_suivant = True
    cpt_boucle = 0
    co = 0
    while 1:
        if ppas:
            pas_suivant = PasSuivant(co)
            if not pas_suivant:
                break
        cpt_boucle = cpt_boucle + 1
        if cpt_boucle > 100000.0:
            OPErreur("detection d'une boucle infinie (plus de 100000 pas de programme)")
            pas_suivant = False
        else:
            if co < 0 or co > 99:
                OPErreur('debordement memoire')
                pas_suivant = False
            zc.co.set(co)
            zc.ri.set(zm.mem[co].get())
            try:
                tmp = int(zm.mem[co].get())
            except:
                OPErreur('contenu inconnu', str(co))
                pas_suivant = False
                break
            mem = zm.mem[co].get()
            try:
                code = int(mem[0])
            except:
                OPErreur('code instruction ' + mem[0] + ' inconnu')
                pas_suivant = False
                break
            if code < 0 or code > 9:
                OPErreur('code ' + str(code) + ' inconnu')
                pas_suivant = False
                break
            try:
                adr = int(mem[1:])
            except:
                OPErreur('adresse ' + mem[1:] + ' absente ou invalide')
                pas_suivant = False
                break
            if adr < 0 or adr > 99:
                OPErreur('adresse ' + str(adr) + ' inconnue')
                pas_suivant = False
                break
            if code == 0:
                OPInput(adr)
            elif code == 1:
                pas_suivant = OPOutput(adr)
            elif code == 2:
                pas_suivant = OPAccum(adr)
            elif code == 3:
                pas_suivant = OPStock(adr)
            elif code == 4:
                pas_suivant = OPAdd(adr)
            elif code == 5:
                pas_suivant = OPSub(adr)
            elif code == 6:
                pas_suivant = OPShift(adr)
            elif code == 7:
                pas_suivant, co = OPJump(adr)
            elif code == 8:
                pas_suivant, co = OPTestAcc(adr, co)
            elif code == 9:
                pas_suivant = OPHalt()
            else:
                OPErreur('code ' + str(code) + ' inconnu')
                pas_suivant = False
            co = co + 1

def Desassembleur(plcode):
    'Desassembleur du code Ordinapoche'
    des = Toplevel()
    des.title('Desassembleur')
    des.resizable(width=False, height=False)
    i = 0
    for li in plcode:
        Label(des, width=10, text=li, relief='flat', bd=2, bg='white', fg='black', anchor='w').pack(side=TOP)
        i = i + 1

def OPDesassembleI():
    linst = ['INP', 'OUT', 'CLA', 'STO', 'ADD', 'SUB', 'SHT', 'JMP', 'TAC', 'HRS']
    lcode = []
    pas_suivant = True
    co = 0
    while pas_suivant:
        try:
            tmp = int(zm.mem[co].get())
        except:
            break
        mem = zm.mem[co].get()
        try:
            code = int(mem[0])
        except:
            code = '???'
            pas_suivant = False
        code = linst[code]
        try:
            adr = int(mem[1:])
        except:
            adr = '??'
            pas_suivant = False
        adr = str(adr)
        if code != 'HRS':
            lcode.append(str(co).zfill(2) + '  ' + code + ' ' + adr.zfill(2))
        else:
            lcode.append(str(co).zfill(2) + '  ' + code)
        co = co + 1
    Desassembleur(lcode)

def OPDesassembleE():
    pass

def OPInput(padr):
    'code = 0 : INP'
    OPDecodage("Saisie d'une valeur depuis le peripherique d'entree")
    zc.clavier.reset()
    zc.clavier.configure(highlightthickness=2)
    zc.clavier.focus()
    zc.clavier.wait_variable(zc.clavier.entree)
    zc.clavier.configure(highlightthickness=0)
    zm.mem[padr].set(zc.clavier.entree.get())

def OPOutput(padr):
    'code = 1 : OUT'
    OPDecodage("Affichage de la donnee d'adresse " + str(padr) + ' sur le peripherique de sortie')
    try:
        nb = int(zm.mem[padr].get())
    except:
        OPErreur('donnee non numerique', str(padr))
        return False
    zc.ecran.affiche_nombre(nb)
    return True

def OPAccum(padr):
    'code = 2 : CLA'
    OPDecodage('Mise a zero du contenu du registre ACC et addition')
    try:
        nb = int(zm.mem[padr].get())
    except:
        OPErreur('donnee non numerique', str(padr))
        return False
    zc.acc.set(nb)
    return True

def OPStock(padr):
    'code = 3 : STO'
    OPDecodage("Stockage du contenu du registre ACC a l'adresse " + str(padr))
    try:
        nb = int(zc.acc.get())
    except:
        OPErreur('STO : donnee non numerique')
        return False
    zm.mem[padr].set(nb)
    return True

def OPAdd(padr):
    'code = 4 : ADD'
    OPDecodage("Addition du contenu du registre ACC et de l'adresse " + str(padr))
    try:
        nb1 = int(zc.acc.get())
    except:
        OPErreur('ADD :donnee non numerique')
        return False
    try:
        nb2 = int(zm.mem[padr].get())
    except:
        OPErreur('donnee non numerique', str(padr))
        return False
    res = nb1 + nb2
    while res > 999:
        res = res - 1000
    zc.acc.set(res)
    return True

def OPSub(padr):
    'code = 5 : SUB'
    OPDecodage("Soustraction du contenu du registre ACC et de l'adresse " + str(padr))
    try:
        nb1 = int(zc.acc.get())
    except:
        OPErreur('SUB : donnee non numerique')
        return False
    try:
        nb2 = int(zm.mem[padr].get())
    except:
        OPErreur('donnee non numerique', str(padr))
        return False
    res = nb1 - nb2
    if res < 0:
        res = 1000 - abs(res) % 1000
    zc.acc.set(res)
    return True

def OPShift(psht):
    'code = 6 : SHT'
    OPDecodage("Decalage a gauche puis a droite de l'ACC")
    try:
        nb = int(zc.acc.get())
    except:
        OPErreur('SHT : donnee non numerique')
        return False
    if psht > 99:
        OPErreur('SHT : decalage hors des bornes')
        return False
    gauche = psht/10
    droite = psht - gauche*10
    nb = nb*10**gauche % 1000
    nb = nb/10**droite
    zc.acc.set(nb)
    return True

def OPJump(padr):
    'code = 7 : JMP'
    OPDecodage("Saut inconditionnel a l'adresse " + str(padr))
    if padr < 0 or padr > 99:
        OPErreur('JMP : ' + str(padr) + ' ne correspond a aucune adresse')
        return False
    zc.co.set(padr - 1)
    return True, padr - 1

def OPTestAcc(padr, pco):
    'code = 8 : TAC'
    OPDecodage("Saut conditionnel a l'adresse " + str(padr))
    if padr < 0 or padr > 99:
        OPErreur('TAC : ' + str(padr) + ' ne correspond a aucune adresse')
        return False
    try:
        nb = int(zc.acc.get())
    except:
        OPErreur('TAC : donnee non numerique')
        return False
    if nb != 0:
        tmp = padr - 1
        zc.co.set(tmp)
    else:
        tmp = pco
    return True, tmp

def OPHalt():
    'code = 9 : HRS'
    OPDecodage('Fin de programme')
    return False

def AskQuit():
    if sys.version_info >= (3,):
        if messagebox.askokcancel('Quitter', 'Voulez-vous vraiment quitter ?'):
            fenp.destroy()
    elif tkMessageBox.askokcancel('Quitter', 'Voulez-vous vraiment quitter ?'):
        fenp.destroy()

if __name__ == '__main__':
    fenp = Tk()
    fenp.title('Ordinapoche')
    fenp.resizable(width=False, height=False)
    fenp.protocol('WM_DELETE_WINDOW', AskQuit)
    OPMenus()
    zc = OPCanvas()
    zm = OPMemoire()
    fenp.mainloop()
