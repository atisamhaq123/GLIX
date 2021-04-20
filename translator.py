from tkinter import *
from tkinter import ttk
from urllib import request, parse


#Creating a main window




def main():
    window=Tk()
    window.title("GLIX")
    window.minsize(900,550)
    window.maxsize(900,550)
        
    def translation():
        window.destroy()

        win1 = Tk()
        
        win1.title("GLIX-TRANSLATOR")
        win1.minsize(900,550)
        win1.maxsize(900,550)
        win1.configure(background='grey')
        def exittrans():
            win1.destroy()
            main()

        
        #Adding a label
        a=Label(win1, text="Enter the text for translation", relief=FLAT, bd=5, bg="black", fg="white", font="bellmt 18")
        a.place(x=100, y=50)
        Button(win1,text="BACK",bg="#3c3c3c",fg="white",command=exittrans).place(x=10,y=10)


        #Adding entry to take user input
        global entry1
        entry1=Entry(win1, width=63, bg='white',relief=FLAT, bd=5, font='bellmt 15')
        entry1.place(x=100, y=90)


        #Adding another label
        b=Label(win1, text='Select language', bd=5, bg="black", fg='white', font='bellmt 18')
        b.place(x=100, y=140)


        #Drop down menu
        global language
        language=ttk.Combobox(win1, values="English Urdu Punjabi Arabic Hindi Russian Japanese Chinese Bengali Italian Greek Spanish Indonesian Korean French Turkish Scottish Latin German", font="bellmt 15", state="readonly")
        language.place(x=553 , y=140)


        #Translate Button
        button=Button(win1, text="GLIX", activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue', command=translate, bd=5)
        button.place(x=370, y=190)


        scroll = Scrollbar(win1)
        scroll.pack(side=RIGHT, fill=Y)

        #Displaying output
        global output1
        output1=Text(win1, width=63, height=8, bd=5,relief=FLAT, font="belltm 15", wrap=WORD, yscrollcommand=scroll.set)
        output1.place(x=100, y=260)

        #Glix Label
        glabel = Label(win1, text='GLIX', fg='white', bg='black', bd=5, font='bellmt 18', width=10)
        glabel.place(x=400, y=5)


        def exit():
            win1.destroy()
        
        
        Button(win1, text="Exit", bd=5, relief=RAISED, font="bellmt 12", command=exit, bg='red', width=7).place(x=790, y=500)    

        helpbutton = Button(win1, text="?", font="bellmt 8 bold", width=3, bg='light blue', fg="black", relief=RAISED, bd=5, command=hbutton)
        helpbutton.place(x=825, y=30)







        

        

        
        

   

#Help button
    def hbutton():
        helpwindow=Tk()
        helpwindow.geometry('500x200')

        #Adding scrollbar
        scroll = Scrollbar(helpwindow)
        scroll.pack(side=RIGHT, fill=Y)

        text=""
            
        helpwindow.title("Help")
        label = Text(helpwindow, yscrollcommand=scroll.set, font="bellmt 15", wrap=WORD)
        label.pack()
        label.insert(END, text)




    def translate():
        text = entry1.get()
        output1.delete(0.0, END)
        l = language.get()

        #Converting the language name to languae code.
        if l=="Urdu":
            lang="ur"

        elif l=='English':
            lang='en'
            
        elif l=="Russian":
            lang="ru"
            
        elif l=="Arabic":
            lang="ar"
            
        elif l=="Bengali":
            lang="bn"
            
        elif l=="Greek":
            lang="el"
            
        elif l=="Italian":
            lang="it"
            
        elif l=="Spanish":
            lang="es"
            
        elif l=="Indonesian":
            lang="id"
            
        elif l=="Chinese":
            lang="zh"
            
        elif l=="Korean":
            lang='ko'
            
        elif l=="Latin":
            lang='la'
            
        elif l=="Japanese":
            lang='ja'
            
        elif l=="Scottish":
            lang='gd'

        elif l=="Hindi":
            lang='hi'

        elif l=="French":
            lang='fr'

        elif l=="Turkish":
            lang='tr'

        elif l=="Punjabi":
            lang='pa'

        elif l=="German":
            lang="de"

        
        text = parse.quote_plus(text)
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20181202T162108Z.b051f5dc92d73f20" \
              ".1dccb218c5f04d3b1c9a448ce4ff0cc17fcd08d6&text=" + text + "&lang=" + lang

        test = request.urlopen(url=url)
        tes = test.read().decode()
        tes = eval(tes)
        translation = tes["text"]

        output1.insert(END, "Translation:\n\t{}".format(translation))

    #######
        







    #For the definition part:    
    def define():

        text=entry2.get()
        output2.delete(0.0, END)
        
        
        url = request.urlopen(url="https://www.dictionary.com/browse/" + text)
        #page = request.urlopen(url=url)
        first = url.read().decode()
        s = first.find('<span class="one-click-content css-9sn2pa e1q3nk1v4">')
        r = first.find('</span></li><div class="css-1xdhyk6 et6eviy0"><section class="no-collapse css-hh4f95 e1eb38er0"><aside class="css-6xt45o e1bbcgok0"><a href="https://www.dictionary.com/e/" data-linkid="2azoy5" class="css-1pny6db e1bbcgok2">')
        v = first[s:r]
        z = v
           
        for i in range(z.count("<")):
            for char in range(len(z)):
                if z[char] == "<":
                    for char_1 in range(len(z[char:-1])):
                        if z[char:-1][char_1] == ">":
                            z = z.replace(z[char:char_1+len(z[0:char])+1], '')
                            break
                    break

        

        output2.insert(END,"Definition:\n\t{}".format(z))


    #Synonym
    def synonym():
        word=entry3.get()
        output3.delete(0.0, END)

        f=request.urlopen('https://www.synonym.com/synonyms/?term=' + word)

        x = f.read().decode()

        s = x.find('<ul class="synonyms">')
        r = x.find('</ul>')
        s2 = s+20
        v = x[s2:r]
        z = v

        for i in range(z.count("<")):
            for char in range(len(z)):
                if z[char] == "<":
                    for char_1 in range(len(z[char:-1])):
                        if z[char:-1][char_1] == ">":
                            z = z.replace(z[char:char_1 + len(z[0:char]) + 1], '')
                            break
                    break
        y = z.replace("\t", '')
        

        output3.insert(END,y)

        
    #Antonym    
    def antonym():
        word=entry4.get()
        output4.delete(0.0, END)
       
          
        f=request.urlopen('https://www.antonym.com/antonyms/?term=' + word)

        x = f.read().decode()

        s = x.find('<ul class="antonyms">')
        r = x.find('Synonyms:')
        s2 = s+20
        v = x[s2:r]
        z = v
        for i in range(z.count("<")):
            for char in range(len(z)):
                if z[char] == "<":
                    for char_1 in range(len(z[char:-1])):
                        if z[char:-1][char_1] == ">":
                            z = z.replace(z[char:char_1 + len(z[0:char]) + 1], '')
                            break
                    break
        y = z.replace("\n", '')
        

        output4.insert(END, y)


        
        















    def definition():
        window.destroy()
        win2 = Tk()
        
        win2.title("GLIX-DICTIONARY")
        win2.minsize(900,550)
        win2.maxsize(900,550)
        win2.configure(background='grey')
        def exitdef():
            win2.destroy()
            main()
            
            



        #Glix Label
        glabel = Label(win2, text='GLIX', fg='white', bg='black', bd=5, font='bellmt 18', width=10)
        glabel.place(x=400, y=5)
        Button(win2,text="BACK",bg="#3c3c3c",fg="white",command=exitdef).place(x=10,y=10)

        #Label
        label1 = Label(win2, text='Enter a word', bd=5, bg='black', fg='white', font='bellmt 18')
        label1.place(x=100, y=90)


        #Adding entry to take user input
        global entry2
        entry2=Entry(win2, width=63, bg='white',relief=FLAT, bd=5, font='bellmt 15')
        entry2.place(x=100, y=140)

        #Displaying output

        scroll = Scrollbar(win2)
        scroll.pack(side=RIGHT, fill=Y)

        
        global output2
        output2=Text(win2, width=63, height=8, bd=5,relief=FLAT, font="belltm 15", wrap=WORD, yscrollcommand=scroll.set)
        output2.place(x=100, y=260)
        


        #Exit
        def exit():
            win2.destroy()
        Button(win2, text="Exit", bd=5, relief=RAISED, font="bellmt 12", command=exit, bg='red', width=7).place(x=790, y=500)


        #Help button
        helpbutton = Button(win2, text="?", font="bellmt 8 bold", width=3, bg='light blue', fg="black", relief=RAISED, bd=5, command=hbutton)
        helpbutton.place(x=825, y=30)


        #Button
        button=Button(win2, text="GLIX", activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue', command=define, bd=5)
        button.place(x=370, y=190)
        









    def syn():
        window.destroy()
        win3 = Tk()
        
        win3.title("GLIX-SYNONYM")
        win3.minsize(900,550)
        win3.maxsize(900,550)
        win3.configure(background='grey')
        def exitsyn():
            win3.destroy()
            main()



        #Glix Label
        glabel = Label(win3, text='GLIX', fg='white', bg='black', bd=5, font='bellmt 18', width=10)
        glabel.place(x=400, y=5)
        Button(win3,text="BACK",bg="#3c3c3c",fg="white",command=exitsyn).place(x=10,y=10)


        #Label
        label1 = Label(win3, text='Enter a word', bd=5, bg='black', fg='white', font='bellmt 18')
        label1.place(x=100, y=90)


        #Adding entry to take user input
        global entry3
        entry3=Entry(win3, width=63, bg='white',relief=FLAT, bd=5, font='bellmt 15')
        entry3.place(x=100, y=140)

        #Button
        button=Button(win3, text="GLIX", activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue', command=synonym, bd=5)
        button.place(x=370, y=190)


        #Displaying output

        scroll = Scrollbar(win3)
        scroll.pack(side=RIGHT, fill=Y)

        
        global output3
        output3=Text(win3, width=63, height=8, bd=5,relief=FLAT, font="belltm 15", wrap=WORD, yscrollcommand=scroll.set)
        output3.place(x=100, y=260)


        #Exit
        def exit():
            win3.destroy()
        Button(win3, text="Exit", bd=5, relief=RAISED, font="bellmt 12", command=exit, bg='red', width=7).place(x=790, y=500)


        #Help button
        helpbutton = Button(win3, text="?", font="bellmt 8 bold", width=3, bg='light blue', fg="black", relief=RAISED, bd=5, command=hbutton)
        helpbutton.place(x=825, y=30)


        



    def anto():
        window.destroy()
        win4 = Tk()
        
        win4.title("GLIX-ANTONYM")
        win4.minsize(900,550)
        win4.maxsize(900,550)
        win4.configure(background='grey')
        def exitanto():
            win4.destroy()
            main()



        #Glix Label
        glabel = Label(win4, text='GLIX', fg='white', bg='black', bd=5, font='bellmt 18', width=10)
        glabel.place(x=400, y=5)
        Button(win4,text="Back",bg="#3c3c3c",fg="white",command=exitanto).place(x=10,y=10)


        #Label
        label1 = Label(win4, text='Enter a word', bd=5, bg='black', fg='white', font='bellmt 18')
        label1.place(x=100, y=90)


        #Adding entry to take user input
        global entry4
        entry4=Entry(win4, width=63, bg='white',relief=FLAT, bd=5, font='bellmt 15')
        entry4.place(x=100, y=140)

        #Button
        button=Button(win4, text="GLIX", activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue', command=antonym, bd=5)
        button.place(x=370, y=190)


        #Displaying output

        scroll = Scrollbar(win4)
        scroll.pack(side=RIGHT, fill=Y)

        
        global output4
        output4=Text(win4, width=63, height=8, bd=5,relief=FLAT, font="belltm 15", wrap=WORD, yscrollcommand=scroll.set)
        output4.place(x=100, y=260)


        #Exit
        def exit():
            win4.destroy()
        Button(win4, text="Exit", bd=5, relief=RAISED, font="bellmt 12", command=exit, bg='red', width=7).place(x=790, y=500)


        #Help button
        helpbutton = Button(win4, text="?", font="bellmt 8 bold", width=3, bg='light blue', fg="black", relief=RAISED, bd=5, command=hbutton)
        helpbutton.place(x=825, y=30)

             
    #Add photo to the window
    p=PhotoImage(file="logo3.png")
    Label(window, image=p).place(x=0, y=0)



    #buttons
    button1 = Button(window, text='Translation', activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue', bd=5,width=15, command=translation)
    button1.place(x=70,y=170)

    button2 = Button(window, text='Definition', activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue',bd=5, width=15, command=definition)
    button2.place(x=620, y=170)

    button3 = Button(window, text='Synonyms', activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue',bd=5, width=15, command=syn)
    button3.place(x=70, y=400)

    button3 = Button(window, text='Antonyms', activebackground='blue', relief=RAISED, font="bellmt 18", bg='light blue',bd=5, width=15, command=anto)
    button3.place(x=620, y=400)



    #"Exit" Option
    def exit():
        window.destroy()
        
    exitbutton = Button(window, text="Exit", bd=5, relief=RAISED, font="bellmt 12", command=exit, bg='red', width=7)
    exitbutton.place(x=790, y=500)


        
    helpbutton = Button(window, text="?", font="bellmt 8 bold", width=3, bg='light blue', fg="black", relief=RAISED, bd=5, command=hbutton)
    helpbutton.place(x=825, y=30)



    window.mainloop()


   

        



        



main()
