import pickle
class Faculty:
    def add_faculty(self):
        self.fname=input("Enter name:   ")
        self.id=input("Enter ID:   ")
        self.num_books_issued=0
        self.issued_bdetail=[]
        if(len(self.id)==5):
            return 1
        else:
            return 0
        
        
    def faculty_detail(self):
        print(f"{self.id}\t{self.fname}\t{self.num_books_issued}\t\t\t{self.issued_bdetail}\n")
        
    def load_data(self):
        with open('f_details.pkl','rb') as f:
            print("ID\tName\tNo of books issued\tBooks issue details\n")
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.faculty_detail()
                except EOFError:
                    print("data read is completed")
                    break
    def check(self):
        with open('f_details.pkl','rb') as f:
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if(i.id==self.id):
                            return 1
                            break
                except EOFError:
                    return 0
                    break
      
    
    def Issue_book(self):
        idd=input("Enter ID:   ")
        isbno=input("Enter ISBN NO   ")
        obf=Faculty()
        obf.id=idd
        if(obf.check()==1):
            with open('b_details.pkl','rb') as f:
                fg=0
                tl1=[]
                while(True):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.isbn==isbno):
                                if(i.num_of_copies>0):
                                    print("CAN ISSUE BOOK")
                                    fg=1
                            tl1.append(i)
                                   
                    except EOFError:
                        if(fg==0):
                            print("BOOK NOT AVAILABLE")
                        break
                        
            if(fg==1):
                for i in tl1:
                    if(i.isbn==isbno):
                        i.num_of_copies-=1
                        break
                with open('b_details.pkl','wb') as f:
                    pass
                with open('b_details.pkl','ab') as f:
                    pickle.dump(tl1,f)  

                with open('f_details.pkl','rb') as f:
                    tl2=[]
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                tl2.append(i)
                        except EOFError:
                            break
                        
                for i in tl2:
                    if(i.id==idd):
                        i.num_books_issued+=1
                        i.issued_bdetail.append(isbno)
                        break
                with open('f_details.pkl','wb') as f:
                    pass
                with open('f_details.pkl','ab') as f:
                    pickle.dump(tl2,f)    
        else:
            print("ID NOT PRESENT")
    
    
    def Return_book(self):
        idd=input("Enter ID:   ")
        isbno=input("Enter ISBN NO   ")
        obf=Faculty()
        obf.id=idd
        if(obf.check()==1):
            with open('b_details.pkl','rb') as f:
                fg=0
                tl1=[]
                while(True):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.isbn==isbno):
                                if(i.num_of_copies>0):
                                    print("CAN RETURN BOOK")
                                    fg=1
                            tl1.append(i)

                    except EOFError:
                        if(fg==0):
                            print("BOOK NOT AVAILABLE")
                        break
            if(fg==1):
                for i in tl1:
                    if(i.isbn==isbno):
                        i.num_of_copies+=1
                        break
                with open('b_details.pkl','wb') as f:
                    pass
                with open('b_details.pkl','ab') as f:
                    pickle.dump(tl1,f)  

                with open('f_details.pkl','rb') as f:
                    tl2=[]
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                tl2.append(i)
                        except EOFError:
                            break   

                for i in tl2:
                    if isbno in i.issued_bdetail:
                        i.num_books_issued-=1
                        i.issued_bdetail.remove(isbno)
                        break
                with open('f_details.pkl','wb') as f:
                    pass
                with open('f_details.pkl','ab') as f:
                    pickle.dump(tl2,f)        
        else:
            print("ID NOT PRESENT")
    
    
               