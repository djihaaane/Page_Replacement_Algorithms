#FIFO page replacement algorithm implementation in python
from tkinter import *
class MemoireSimulation:
        def __init__(self):
            self.Mafenetre = Tk()
            self.Mafenetre.title("Memoire")
            self.Mafenetre.geometry("500x500")
            self.btnFIFO=Button(self.Mafenetre,text="FIFO",command=self.FIFO,bg="white")
            self.btnLRU=Button(self.Mafenetre,text="LRU",command=self.LRU,bg="white")
            self.btnOPT=Button(self.Mafenetre,text="OPTIMAL",command=self.OPTIMAL,bg="white")
            self.btnR=Button(self.Mafenetre,text="REINITIALISER",command=self.REINITIALISER,bg="white")
            Label(self.Mafenetre,text="la table de pagination").place(relx=0.1,rely=0.27)
            self.btnOPT.place(x=350,y=150)
            self.btnR.place(x=350,y=250)
            self.btnFIFO.place(x=350,y=100)
            self.btnLRU.place(x=350,y=200)
            self.capacity = 4
            self.s = [1,0,4,5,7,9,2,0,3,4]
            self.listbox = Listbox(self.Mafenetre)
            self.listbox.insert(1,1)
            self.listbox.insert(2,0)
            self.listbox.insert(3,4)
            self.listbox.insert(4,5)
            self.listbox.insert(5,7)
            self.listbox.insert(6,9)
            self.listbox.insert(7,2)
            self.listbox.insert(8,0)
            self.listbox.insert(9,3)
            self.listbox.insert(10,4)
            self.listbox.pack()
            self.listbox.place(x=20,y=200)
            self.Mafenetre.mainloop()

        def REINITIALISER(self):
            for ligne in range(len(self.s)):
                for colonne in range(self.capacity):
                    Label(self.Mafenetre, text=' ',borderwidth=7).grid(row=colonne, column=ligne)
        
        def FIFO(self):
            f,fault,top = [],0,0
            k=0
            for i in self.s:
                if i not in f:
                    if len(f)<self.capacity:
                        f.append(i)
                    else:
                        f[top] = i
                        top = (top+1)%self.capacity
                    fault += 1
                for x in f:
                    print(x,end=' ')
                for x in range(self.capacity-len(f)):
                    print(' ',end=' ')
                    f.append(' ')
                print(f)
                z=0
                for y in range(len(f)):
                    Label(self.Mafenetre, text='%s' %f[y],borderwidth=7).grid(row=z, column=k)   
                    z=z+1
                k=k+1
            print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(self.s),fault,(fault/len(self.s))*100))
        
        def OPTIMAL(self):
            f,fault= [],0
            k=0
            occurance = [None for i in range(self.capacity)]
            for i in range(len(self.s)):
                if self.s[i] not in f:
                    if len(f)<self.capacity:
                        f.append(self.s[i])
                    else:
                        for x in range(len(f)):
                            if f[x] not in self.s[i+1:]:
                                f[x] = self.s[i]
                                break
                            else:
                                occurance[x] = self.s[i+1:].index(f[x])
                        else:
                            f[occurance.index(max(occurance))] = self.s[i]
                    fault += 1
                print("   %d\t\t"%self.s[i],end='')
                for x in f:
                    print(x,end=' ')
                for x in range(self.capacity-len(f)):
                    print(' ',end=' ')
                print(f)
                z=0
                for y in range(len(f)):
                    Label(self.Mafenetre, text='%s' %f[y],borderwidth=7).grid(row=z, column=k)   
                    z=z+1
                k=k+1    
            print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(self.s),fault,(fault/len(self.s))*100))
        
        def LRU(self):
            k=0
            f,st,fault,top = [],[],0,0
            for i in self.s:
                if i not in f:
                    if len(f)<self.capacity:
                        f.append(i)
                        st.append(len(f)-1)
                    else:
                        ind = st.pop(0)
                        f[ind] = i
                        st.append(ind)
                    fault += 1
                else:
                    st.append(st.pop(st.index(f.index(i))))
                print("   %d\t\t"%i,end='')
                for x in f:
                    print(x,end=' ')
                for x in range(self.capacity-len(f)):
                    print(' ',end=' ')
                print(f)
                z=0 
                for y in range(len(f)):
                    Label(self.Mafenetre, text='%s' %f[y],borderwidth=7).grid(row=z, column=k)   
                    z=z+1
                k=k+1    
            print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(self.s),fault,(fault/len(self.s))*100))
app=MemoireSimulation()