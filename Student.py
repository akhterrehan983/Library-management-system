import pickle
class Student:
    def load_data(self):
        with open('s_details.pkl','rb') as f:
            print("Enrollment No\tName\tBranch\tAdmission Id\tYear of Admission\tBooks Issued\tISBN OF BOOKS_ISSUED\n")
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.student_detail()
                except EOFError:
                    print("data read is completed")
                    break
    def student_detail(self):
        print(f"{self.roll_no}\t{self.sname}\t{self.branch}\t{self.admn_id_no}\t\t{self.year_of_admn}\t\t\t{self.num_books_issued}\t\t{self.issued_bdetail}\n")
    
    def add_student(self, sname, year_of_admn, branch, admn_id_no,roll_no,num_books_issued):
        self.sname=sname
        self.year_of_admn=year_of_admn
        self.branch=branch
        self.admn_id_no=admn_id_no
        self.roll_no=roll=roll_no
        self.num_books_issued=num_books_issued
        issued_bdetail=[]
        self.issued_bdetail=issued_bdetail
    
    def check(self,adms_id):
        with open('s_details.pkl','rb') as f:
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if(i.admn_id_no==adms_id):
                            return 0
                            break
                except EOFError:
                    break
    
    def book_limit(self,adms_id):
        with open('s_details.pkl','rb') as f:
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if(i.admn_id_no==adms_id):
                            if(i.num_books_issued<5):
                                return 1
                            else:
                                print("Student has reached book limit")
                                return 0
                            break
                except EOFError:
                    return 2
                    break
                    
    def Issue_book(self):
        roll=input("Enter enrollment no")
        adm_id=roll[-4:]
        ob=Student()
        val=ob.book_limit(adm_id)
        if(val==1):#can issue
            isbno=input("Enter ISBN NO:   ")
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
                    
                
                with open('s_details.pkl','rb') as f:
                    tl2=[]
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                tl2.append(i)
                        except EOFError:
                            break
                        
                for i in tl2:
                    if(i.admn_id_no==adm_id):
                        i.num_books_issued+=1
                        i.issued_bdetail.append(isbno)
                        break
                with open('s_details.pkl','wb') as f:
                    pass
                with open('s_details.pkl','ab') as f:
                    pickle.dump(tl2,f)
                    
        elif(val==2):
            print("Student not available")
            
    def Return_book(self):
        roll=input("Enter enrollment no")
        adm_id=roll[-4:]
        ob=Student()
        val=ob.book_limit(adm_id)
        if(val==1):#can return
            isbno=input("Enter ISBN NO:   ")
            with open('s_details.pkl','rb') as f:
                fg=0
                tl1=[]
                while(True):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if isbno in i.issued_bdetail :
                                    print("CAN RETURN BOOK")
                                    fg=1
                            tl1.append(i)

                    except EOFError:
                        if(fg==0):
                            print("BOOK NOT AVAILABLE")
                        break
            if(fg==1):
                for i in tl1:
                    if isbno in i.issued_bdetail:
                        i.num_books_issued-=1
                        i.issued_bdetail.remove(isbno)
                        break
                with open('s_details.pkl','wb') as f:
                    pass
                with open('s_details.pkl','ab') as f:
                    pickle.dump(tl1,f) 
                
            with open('b_details.pkl','rb') as f:
                    tl2=[]
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                tl2.append(i)
                        except EOFError:
                            break
                        
            for i in tl2:
                if(i.isbn==isbno):
                    i.num_of_copies+=1
                    break
            with open('b_details.pkl','wb') as f:
                pass
            with open('b_details.pkl','ab') as f:
                pickle.dump(tl2,f)
                        
        elif(val==2):
            print("Student not available")
    
