import pickle
class contact:
    def __init__(self,name,phone_no,email_add):
        self.name=name
        self.phone_no=phone_no
        self.email_add=email_add
        
    def set_name(self,name):
        self.name=name
        
    def set_phone(self,phone_no):
        self.phone_no=phone_no
        
    def set_email(self,email_add):
        self.email_add=email_add
        
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone_no
    def get_email(self):
        return self.email_add
    def __str__(self):
        return f'My name is {self.name}\nMy phone no. is {self.phone_no}\n'
def main():
    c=contact('Sejal','940726345','abc@gmail.com')
    ch=input("Press 1 to add new record\nPress 2 to lookup the record\nPress 3 to change the contact\nPress 4 to delete the contact\nPress 5 to quit\n")
    if ch==1:
        out_file=open('contactMe.txt','wb')
        d={}
        d['name']=c.set_name(input('Enter the name'))
        d['phone_no']=c.set_email(input('Enter the address'))
        d['email address']=c.set_phone(input('Enter the phone_no.'))
        pickle.dump(d,out_file)
        out_file.close()
    elif ch==2:
        inf=open('contactMe.txt','rb')
        print(pickle.load(inf))
    
    
main()

        
