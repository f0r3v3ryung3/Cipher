from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import messagebox

window = Tk()  
window.title("Попробуй расшифруй")  
window.geometry('750x500')  

rlbck = []
rslt = ''

lv = ''
lvley1 = ''
lvkey2 = ''
lvkey3 = ''
lvkey4 = ''
lvbtn1 = Button(window, text='')  
lvbtn2 = Button(window, text='')  
lvbtn3 = Button(window, text='')  
lvbtn4 = Button(window, text='')  
lvbtnSl = ''
lvbtnRt = ''
btns = []

def shifr(txt, key):
    shif = dict()
    res = ''
    a = len(key) % len(txt) - 1
    
    for i in range(0, len(key)):
        if txt[a] != ' ' and txt[a] not in shif and key[i] not in shif:
            shif[txt[a]] = key[i]
            shif[key[i]] = txt[a]
            a = (a + len(key)) % len(txt)
        else:
            a += 1
            a %= len(txt)
    
    txt = list(txt.split())
    
    for j in txt:
        wrd = ''
        for k in range(0, len(j)):
            ltt = j[k]
            if ltt in shif:
                wrd += shif[ltt]
            else:
                wrd += ltt
        res += wrd + ' '
    return res[:-1], shif

def rasshifr(txt, shif):
    res = ''
    txt = list(txt.split())
    
    for j in txt:
        wrd = ''
        for k in range(0, len(j)):
            ltt = j[k]
            if ltt in shif:
                wrd += shif[ltt]
            else:
                wrd += ltt
        res += wrd + ' '
    return res[:-1]

def HideKey(shif, lastKey):
    res = ''
    for i in lastKey:
        if i in shif:
            res += shif[i]
        else:
            res += ' '
    return res

def lvl1():
    global lv, lvkey1, lvkey2, lvbtn1, lvbtn2, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'hello how are you'
    a = shifr('hello how are you', 'fgh')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'fgh')
    a = shifr(lv, 'klj')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'klj')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn1.grid(column=3, row=4)  
    
    lvbtn2 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn2.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)

    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2)
    
    btns += [lvbtn1, lvbtn2, lvbtnSl, lvbtnRt]
        
    
def lvl2():
    global lv, lvkey1, lvkey2, lvbtn1, lvbtn2, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'i dont know'
    a = shifr('i dont know', 'rpg')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'rpg')
    a = shifr(lv, 'nvf')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'nvf')
    lbl.configure(text=lv)

    lvbtn1 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn2.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)

    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2)
    
    btns += [lvbtn1, lvbtn2, lvbtnSl, lvbtnRt]

def lvl3():
    global lv, lvkey1, lvkey2, lvbtn1, lvbtn2, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'please wait me'
    a = shifr('please wait me', 'hlt')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'hlt')
    a = shifr(lv, 'slp')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'slp')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn2.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)

    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2)
    
    btns += [lvbtn1, lvbtn2, lvbtnSl, lvbtnRt]

def lvl4():
    global lv, lvkey1, lvkey2, lvbtn1, lvbtn2, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'glad to see you'
    a = shifr('glad to see you', 'lkdf')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'lkdf')
    a = shifr(lv, 'asdf')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'asdf')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn2.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)

    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2)
    
    btns += [lvbtn1, lvbtn2, lvbtnSl, lvbtnRt]

def lvl5():
    global lv, lvkey1, lvkey2, lvkey3, lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'privet poka ura'
    a = shifr('privet poka ura', 'kola')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'kola')
    
    a = shifr(lv, 'priv')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'priv')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'snlp')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'snlp')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn2.grid(column=5, row=4)
    
    lvbtn3 = Button(window, text=lvkey3, command=lvcom3)  
    lvbtn3.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2) 
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt]

def lvl6():
    global lv, lvkey1, lvkey2, lvkey3, lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'ne mogu pridumat'
    a = shifr('ne mogu pridumat', 'hello')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'hello')
    
    a = shifr(lv, 'good')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'good')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'bad')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'bad')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey3, command=lvcom3)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn2.grid(column=5, row=4)
    
    lvbtn3 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn3.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2) 
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt] 

def lvl7():
    global lv, lvkey1, lvkey2, lvkey3, lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'read anything'
    a = shifr('read anything', 'uf')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'uf')
    
    a = shifr(lv, 'mb')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'mb')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'ds')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'ds')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn2.grid(column=5, row=4)
    
    lvbtn3 = Button(window, text=lvkey3, command=lvcom3)  
    lvbtn3.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2) 
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt]

def lvl8():
    global lv, lvkey1, lvkey2, lvkey3, lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'i am so tired'
    a = shifr('i am so tired', 'more')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'more')
    
    a = shifr(lv, 'taki')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'taki')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'ufhg')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'ufhg')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey3, command=lvcom3)  
    lvbtn2.grid(column=5, row=4)
    
    lvbtn3 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn3.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2)
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt]

def lvl9():
    global lv, lvkey1, lvkey2, lvkey3, lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'pop punk the best'
    a = shifr('pop punk the best', 'mgk')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'mgk')
    
    a = shifr(lv, 'yung')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'yung')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'blud')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'blud')
    lbl.configure(text=lv)
    
    lvbtn1 = Button(window, text=lvkey3, command=lvcom3)  
    lvbtn1.grid(column=3, row=4)
    
    lvbtn2 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn2.grid(column=5, row=4)
    
    lvbtn3 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn3.grid(column=7, row=4)
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2) 
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtnSl, lvbtnRt]  

def lvl10():
    global lv, lvkey1, lvkey2, lvkey3, lvkey4, lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'i want sleep help me'
    a = shifr('i want sleep help me', 'pjh')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'pjh')
    
    a = shifr(lv, 'mlt')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'mlt')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'xyz')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'xyz')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'ops')
    lv = a[0]
    lvkey4 = HideKey(a[1], 'ops')
    lbl.configure(text=lv)    
    
    lvbtn1 = Button(window, text=lvkey1, command=lvcom1)  
    lvbtn1.grid(column=2, row=4)
    
    lvbtn2 = Button(window, text=lvkey2, command=lvcom2)  
    lvbtn2.grid(column=4, row=4)
    
    lvbtn3 = Button(window, text=lvkey3, command=lvcom3)  
    lvbtn3.grid(column=6, row=4)
    
    lvbtn4 = Button(window, text=lvkey4, command=lvcom4)  
    lvbtn4.grid(column=8, row=4)    
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2) 
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt] 

def lvl11():
    global lv, lvkey1, lvkey2, lvkey3, lvkey4, lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt, btns, rslt, rlbck
    rlbck = []
    for i in btns:
        i.grid_remove()
    rslt = 'you are the bestest'
    a = shifr('you are the bestest', 'fgh')
    lv = a[0]
    lvkey1 = HideKey(a[1], 'fgh')
    
    a = shifr(lv, 'rmt')
    lv = a[0]
    lvkey2 = HideKey(a[1], 'rmt')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'last')
    lv = a[0]
    lvkey3 = HideKey(a[1], 'last')
    lbl.configure(text=lv)
    
    a = shifr(lv, 'lmn')
    lv = a[0]
    lvkey4 = HideKey(a[1], 'lmn')
    lbl.configure(text=lv)    
    
    lvbtn1 = Button(window, text=lvkey1, command=lvcom2)  
    lvbtn1.grid(column=2, row=4)
    
    lvbtn2 = Button(window, text=lvkey2, command=lvcom4)  
    lvbtn2.grid(column=4, row=4)
    
    lvbtn3 = Button(window, text=lvkey3, command=lvcom1)  
    lvbtn3.grid(column=6, row=4)
    
    lvbtn4 = Button(window, text=lvkey4, command=lvcom3)  
    lvbtn4.grid(column=8, row=4)    
    
    lvbtnSl = Button(window, text='Сдаться', command=lvds) 
    lvbtnSl.grid(column=5, row=5)
    
    lvbtnRt = Button(window, text='Назад', command=rtrn) 
    lvbtnRt.grid(column=2, row=2) 
    
    btns += [lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt] 
    
def lvcom1():
    global lv, lvkey1, lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt, rlbck, rslt
    rlbck.insert(0, lv)
    lv = shifr(lv, lvkey1)
    lbl.configure(text=lv[0])
    lv = lv[0]
    if lv == rslt:
        messagebox.showinfo('Поздраление', 'You are winner') 
        lvbtn1.grid_remove()
        lvbtn2.grid_remove()
        lvbtn3.grid_remove()
        lvbtn4.grid_remove()     
        lvbtnSl.grid_remove()
        lvbtnRt.grid_remove() 
    
def lvcom2():
    global lv, lvkey2, lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt, rlbck, rslt
    rlbck.insert(0, lv)
    lv = shifr(lv, lvkey2)
    lbl.configure(text=lv[0])
    lv = lv[0]
    if lv == rslt:
        messagebox.showinfo('Поздраление', 'You are winner') 
        lvbtn1.grid_remove()
        lvbtn2.grid_remove()
        lvbtn3.grid_remove()
        lvbtn4.grid_remove()     
        lvbtnSl.grid_remove()
        lvbtnRt.grid_remove() 

def lvcom3():
    global lv, lvkey3, lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt, rlbck, rslt
    rlbck.insert(0, lv)
    lv = shifr(lv, lvkey3)
    lbl.configure(text=lv[0])
    lv = lv[0]
    if lv == rslt:
        messagebox.showinfo('Поздраление', 'You are winner') 
        lvbtn1.grid_remove()
        lvbtn3.grid_remove()
        lvbtn2.grid_remove()
        lvbtn4.grid_remove()     
        lvbtnSl.grid_remove()
        lvbtnRt.grid_remove() 
        
def lvcom4():
    global lv, lvkey4, lvbtn1, lvbtn2, lvbtn3, lvbtn4, lvbtnSl, lvbtnRt, rlbck, rslt
    rlbck.insert(0, lv)
    lv = shifr(lv, lvkey4)
    lbl.configure(text=lv[0])
    lv = lv[0]
    if lv == rslt:
        messagebox.showinfo('Поздраление', 'You are winner') 
        lvbtn1.grid_remove()
        lvbtn3.grid_remove()
        lvbtn2.grid_remove()
        lvbtn4.grid_remove()        
        lvbtnSl.grid_remove()
        lvbtnRt.grid_remove() 
        
def rtrn():
    global rlbck, lv
    if len(rlbck) > 0:
        lbl.configure(text=rlbck[0])
        lv = rlbck[0]
        del rlbck[0]

def lvds():
    global lv, lvkey2, lvbtn1, lvbtn2, lvbtn3, lvkey4, lvbtn4, lvbtnSl, lvbtnRt
    messagebox.showinfo('Слабак', 'You loser')
    lvbtn2.grid_remove()
    lvbtn1.grid_remove()  
    lvbtn3.grid_remove()
    lvbtn4.grid_remove()   
    lvbtnSl.grid_remove()
    lvbtnRt.grid_remove() 

lbl = Label(window, text="Привет", font=("Arial Bold", 15))
messagebox.showinfo('Длинный, нудный очень "нужный" текст', 'Здесь я объясню вам, как в это играть(правда зачем, вы все равно будете тыкать на все кнопки, и да я сново потерял смысл того что я делаю, короче). У вас есть предложение, например "goodbye" и ключ, например "two". Длина ключа равна 3, т.к. в нем 3 символа(это означает, что в ключах типо "f l " 4 символа), и каждый 3-ий (длина ключа) символ предложения меняется на соответсвующую букву ключа, а буква ключа в предложении на букву в слове(тут важно учесть, что если символ ключа это " ", то на него буква не заменяется, а просто пропускаем этот симбол в ключе и букву в предложении и идем к следающему, так же если буква в предложении равна " ", то она не заменяется, а пропускается, и механизм движется дальше), в нашем примере t - o, o - t, y - w, w - y, o - o (ну последнее особо красоты не делает), в итоге у нас получится "gttbuw". Так с алгоритмом шифровки разобрались(если что перечитаете), а ваша задача зашифровать предложение так чтобы его можно было прочитать. Так же, тем кто дочитал я дам подсказку, каждый уровень решается за нажатие каждой кнопки по разу.')

messagebox.showinfo('И еще!!!', 'И будьте внимательно, оказалось что пробелы капец какие тонкие')

lbl.grid(column=2, row = 3, columnspan=7, sticky=S) 
rad1 = Radiobutton(window, text='1 level', value=1, command = lvl1)  
rad2 = Radiobutton(window, text='2 level', value=2, command = lvl2)  
rad3 = Radiobutton(window, text='3 level', value=3, command = lvl3)  
rad4 = Radiobutton(window, text='4 level', value=4, command = lvl4)  
rad5 = Radiobutton(window, text='5 level', value=5, command = lvl5)  
rad6 = Radiobutton(window, text='6 level', value=6, command = lvl6)  
rad7 = Radiobutton(window, text='7 level', value=7, command = lvl7)  
rad8 = Radiobutton(window, text='8 level', value=8, command = lvl8)  
rad9 = Radiobutton(window, text='9 level', value=9, command = lvl9)  
rad10 = Radiobutton(window, text='10 level', value=10, command = lvl10)  
rad11 = Radiobutton(window, text='11 level', value=11, command = lvl11) 
rad1.grid(column=0, row=0, pady = 10, padx = 5)  
rad2.grid(column=1, row=0, pady = 10, padx = 5)  
rad3.grid(column=2, row=0, pady = 10, padx = 5)  
rad4.grid(column=3, row=0, pady = 10, padx = 5)  
rad5.grid(column=4, row=0, pady = 10, padx = 5)  
rad6.grid(column=5, row=0, pady = 10, padx = 5) 
rad7.grid(column=6, row=0, pady = 10, padx = 5)  
rad8.grid(column=7, row=0, pady = 10, padx = 5)  
rad9.grid(column=8, row=0, pady = 10, padx = 5)   
rad10.grid(column=9, row=0, pady = 10, padx = 5) 
rad11.grid(column=10, row=0, pady = 10, padx = 5)

window.mainloop()