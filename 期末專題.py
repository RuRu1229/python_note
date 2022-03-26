# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 19:26:13 2021

@author: ADMIN
"""
import os
import json
import tkinter as tk
import pandas as pd

def first_screen():
    c=tk.Tk()#建立頁面
    c.geometry('500x800+100+300')
    c.title("first")
    c.configure(bg='#95CACA')
    lb=tk.Label(c,text='HI，請選擇要執行的事件',width=20,font=50,pady=10,fg='black',bg='#95CACA',compound='center')
    lb.pack()
#視窗選項
    but=tk.Button(c,text='記帳',command=object_screen)
    but.place (x = 200, y = 50, width=120, height=25)#,command=spend_screen)
    but2=tk.Button(c,text='查詢已有物品',command=spend_screen)
    but2.place(x = 200, y = 90, width=120, height=25)

    def del_Screen():
        c.destroy()
    
    but3=tk.Button(c,text='離開', command=del_Screen)
    but3.place(x = 200, y = 130, width=120, height=25)

    c.mainloop()
 

def object_screen():
    global Counts
    Counts = 0
    i= tk.Tk()
    i.title('object')
    i.geometry('500x500')
    i.configure(bg='#95CACA')
    #f=open('spend.txt','a')
    mylabel = tk.Label(i, text='目前所擁有物品',bg='#4F9D9D')
    mylabel.place(x=190,y=0)
    mylabel2 = tk.Label(i, text='請輸入物品及功能',bg='#4F9D9D')
    mylabel2.place(x=180,y=30)
    mylabel3 = tk.Label(i, text='物品',width=5,bg='#4F9D9D')
    mylabel3.place(x=100,y=60)
    e = tk.Entry(i,bd=4)
    e.place(x=150,y=60)
    mylabel3 = tk.Label(i, text='功能',width=5,bg='#4F9D9D')
    mylabel3.place(x=100,y=90)
    h = tk.Entry(i,bd=4)
    h.place(x=150,y=90)
    ## Create a dictionary to store string-value pair
    all_items = {}
    ## Read json file and make it a dict
    t = tk.Text(i,width=20, height=5)
    w= tk.Text(i,width=20 ,height=5)

    #k=0
    #讀黨
    try:
        with open('object.json',"r+") as f:
            try:
                all_items = json.loads(f.read())            
                for key in all_items:
                    t.insert('insert',key)
                    t.insert('insert','.')
                    t.insert('insert',all_items[key][0])
                    t.insert('insert',':')
                    t.insert('insert',all_items[key][1])
                    t.insert(tk.INSERT,'\n')
              #  k= k + all_items[key][1]
                    Counts = int(key)+1
            except :
                pass
    except OSError:
        print('No file found')
 #輸入按鈕   
    def insert_point():
        global Counts
        #print(type(Counts))
        var = e.get()
        var2 = h.get()
        t.insert('insert',Counts)
        t.insert('insert','.')
        t.insert('insert', var)
        t.insert('insert', ':')
        t.insert('insert', var2)
        t.insert(tk.INSERT, '\n')
        e.delete(0,len(var))
        h.delete(0,len(var2))
    #all_items[var] = int(var2)
        all_items[str(Counts)] = [var,var2]
        Counts = Counts + 1
   # z = k + int(var2)
    #k=z
   
#刪除按鈕    
    def delete_point():    
        mkey = de.get()
        de.delete(0,len(mkey))
        try:
        
            global Counts
            del all_items[mkey] 
            t.delete("1.0", tk.END)   
            for key in all_items:
                t.insert('insert',key)
                t.insert('insert','.')
                t.insert('insert',all_items[key][0])
                t.insert('insert','-')
                t.insert('insert',all_items[key][1])
                t.insert(tk.INSERT,'\n')
                Counts = int(key) + 1
        except:
            pass
    
    
    def found_point():    
        fkey = y.get()
        de.delete(0,len(fkey))
        w.delete("1.0", tk.END)  
        if(fkey==all_items[key][0]):
            w.insert('insert',key)
            w.insert('insert','.')
            w.insert('insert',all_items[key][0])
            w.insert('insert','-')
            w.insert('insert',all_items[key][1])

    

    b1 = tk.Button(i, text='輸入', width=5,height=1,command=insert_point)
    b1.place(x=200,y=120)

    d= tk.Label(i, text='刪除物品',bg='#4F9D9D')
    d.place(x=90,y=150)
    de = tk.Entry(i,bd=4)
    de.place(x=150,y=150)

    b2 =tk.Button(i,text='刪除',width=5,height=1,command=delete_point)
    b2.place(x=200,y=180)

    mylabel4 = tk.Label(i, text='查詢物品',bg='#4F9D9D')
    mylabel4.place(x=90,y=220)
    y=tk.Entry(i,bd=4)
    y.place(x=150,y=220)

    f=tk.Button(i, text='查詢' ,width=5,height=1,command=found_point)
    f.place(x=200,y=250)

    t.place(x=150,y=280)
    f1=tk.Label(i, text='查詢結果' ,bg='#4F9D9D')
    f1.place(x=400,y=60)
    w.place(x=350,y=100)
    lv=tk.Button(i, text='返回' ,width=5,height=1,command=first_screen)
    lv.place(x=200,y=360)
  #  lv.place(x=150,y=300)
    def output_Point():
        df = pd.read_json(r'object.json')
        df.to_csv(r'spend.txt', index = False)
        
    oub=tk.Button(i, text='匯出' ,width=5,height=1,command=output_Point)
    oub.place(x=150,y=360)
    exi=tk.Button(i,text='離開',width=5, height=1, command=del_Screen)
    exi.place(x=250,y=360)
   
    
    i.mainloop()


## Store dictionary into json files
    with open('object.json','w') as f:
        json.dump(all_items,f)
#f.close()    
def spend_screen():
    global Counts
    global k
    k=0
    Counts=0
    i= tk.Tk()
    i.title('SPEND')
    i.geometry('500x500')
    i.configure(bg='#95CACA')
    #f=open('spend.txt','a')
    mylabel = tk.Label(i, text='記帳本',bg='#4F9D9D')
    mylabel.place(x=10,y=10,width=50,heigh=50)
    mylabel2 = tk.Label(i, text='請輸入物品及金額',bg='#4F9D9D')
    mylabel2.place(x=180,y=0)
    mylabel3 = tk.Label(i, text='物品',width=5,bg='#4F9D9D')
    mylabel3.place(x=80,y=40)
    e = tk.Entry(i,bd=4)
    e.place(x=150,y=40)
    mylabel3 = tk.Label(i, text='金額',width=5,bg='#4F9D9D')
    mylabel3.place(x=80,y=90)
    h = tk.Entry(i,bd=4)
    h.place(x=150,y=90)
    m= tk.Label(i, text='目前所花金額',bg='#4F9D9D')
    m.place(x=350,y=20)
    ## Create a dictionary to store string-value pair
    all_items = {}

    t = tk.Text(i,width=20, height=5)
    c = tk.Text(i,bg='white',width=10, height=5)
    


 
    #讀取jason檔案中的資料
    try:
        with open('spend.json',"r+") as f:
            try:
                all_items = json.loads(f.read())            
                for key in all_items:
                    t.insert('insert',key)
                    t.insert('insert','.')
                    t.insert('insert',all_items[key][0])
                    t.insert('insert','-')
                    t.insert('insert',all_items[key][1])
                    t.insert(tk.INSERT,'\n')
                    k= k + all_items[key][1]
                    Counts = int(key)+1
            except :
                pass
    except OSError:
        print('No file found')
        #輸入按鈕    
    def insert_point():
        global Counts
        global k
            #顯示
        var = e.get()
        var2 = h.get()
        t.insert('insert',Counts)
        t.insert('insert','.')
        t.insert('insert', var)
        t.insert('insert', '-')
        t.insert('insert', var2)
        t.insert(tk.INSERT, '\n')
        e.delete(0,len(var))
        h.delete(0,len(var2))
        all_items[str(Counts)] = [var,int(var2)]
        Counts = Counts + 1
        z = k + int(var2)
        k=z
        c.delete("1.0", tk.END)#刷新視窗
        c.insert('insert',z)
        #刪除按鈕    
    def delete_point():    
        mkey = de.get()
        de.delete(0,len(mkey))
        try:
            global k
            global Counts
            k = k - all_items[mkey][1]
            del all_items[mkey] 
            t.delete("1.0", tk.END)#視窗刷新
            c.delete("1.0", tk.END)
            c.insert('insert',k)
            for key in all_items:
                t.insert('insert',key)
                t.insert('insert','.')
                t.insert('insert',all_items[key][0])
                t.insert('insert','-')
                t.insert('insert',all_items[key][1])
                t.insert(tk.INSERT,'\n')
                Counts = int(key) + 1
        except:
                pass
    
    
    #c.delete("1.0", tk.END)
    c.insert('insert',k)
    c.place(x=335,y=40,width=100,heigh=20)


    b1 = tk.Button(i, text='輸入', width=5,
               height=1, command=insert_point)
    b1.place(x=200,y=120)

    d= tk.Label(i, text='刪除物品',width=8,bg='#4F9D9D')
    d.place(x=80,y=150)
    de = tk.Entry(i,bd=4)
    de.place(x=150,y=150)

    b2 =tk.Button(i,text='刪除',width=5,height=1,command=delete_point)
    b2.place(x=200,y=180)

    t.place(x=150,y=220)
    lv=tk.Button(i, text='返回' ,width=5,height=1,command=first_screen)
    lv.place(x=150,y=300)
    def output_Screen():
        df = pd.read_json(r'spend.json')
        df.to_csv(r'spend.txt', index = False)
        
    ou=tk.Button(i, text='匯出' ,width=5,height=1,command=output_Screen)
    ou.place(x=200,y=300)
    def del_Screen():
        i.destroy()

    exi=tk.Button(i,text='離開',width=5, height=1, command=del_Screen)
    exi.place(x=250,y=300)
    i.mainloop()

## Store dictionary into json files
    with open('spend.json','w') as f:
        json.dump(all_items,f)
#f.close()
    
c=tk.Tk()#建立頁面
c.geometry('500x800+100+300')
c.title("first")
c.configure(bg='#95CACA')
lb=tk.Label(c,text='HI，請選擇要執行的事件',width=20,font=50,pady=10,fg='black',bg='#95CACA',compound='center')
lb.pack()
#視窗選項
but=tk.Button(c,text='記帳',command=spend_screen)
but.place (x = 200, y = 50, width=120, height=25)#,command=spend_screen)
but2=tk.Button(c,text='查詢已有物品',command=object_screen)
but2.place(x = 200, y = 90, width=120, height=25)

def del_Screen():
    c.destroy()
    
but3=tk.Button(c,text='離開', command=del_Screen)
but3.place(x = 200, y = 130, width=120, height=25)

c.mainloop()


