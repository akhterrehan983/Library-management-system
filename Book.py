import pickle
class Book:
    def add_book(self,isbn):
        self.isbn=isbn
        self.title=input("Enter title:   ")
        self.author=input("Enter authour name:   ")
        self.num_of_copies=int(input("Enter no of copies"))
        
        
    def book_detail(self):
            print(f"{self.isbn}\t\t{self.title}\t\t\t{self.author}\t\t\t{self.num_of_copies}\n")
            
    def load_data(self):
        with open('b_details.pkl','rb') as f:
            print("ISBN NO\t\t\tBook Name\t\tAuthor Name\t\tNumber of copies\n")
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.book_detail()
                except EOFError:
                    print("data read is completed")
                    break
                   
    def check(self,isbn):
        with open('b_details.pkl','rb') as f:
            tl=[]
            fg=0
            while(True):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.isbn==isbn):
                                fg=1
                            tl.append(i)
                    except EOFError:
                        break
            
        if(fg==1):
            for i in tl:
                if(i.isbn==isbn):
                    i.num_of_copies+=self.num_of_copies
                    break
            with open('b_details.pkl','wb') as f:
                pass
            with open('b_details.pkl','ab') as f:
                pickle.dump(tl,f) 
                return 1
        else:  
            return 0
    def search_book(self):
        se=input("Enter a parameter to search accordingly.\nEnter ISBN NO  or Title or Author Name of BOOK:   ")
        with open('b_details.pkl','rb') as f:
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if(i.isbn==se or i.title==se or i.author==se):
                            print("ISBN NO\t\t\tBook Name\t\tAuthor Name\t\tNumber of copies\n")
                            i.book_detail()
                            break
                except EOFError:
                    print("BOOK NOT AVAILABLE")
                    break
                
                
                 
                            
                