
class contact:
    def __init__(self,name,phone_no,email_add):
        self.name=name
        self.phone_no=phone_no
        self.email_add=email_add
        
    def set_name(self,name,out_file):
        out_file.write(name+'\n')
    def set_phone(self,phone_no,out_file):
        out_file.write(phone_no+'\n')
    def set_email(self,email_add,out_file):
        out_file.write(email_add+'\n')
    def get_name(self,out_file):
        out_file.seek(0)
        return out_file.readline()
    def get_phone(self,out_file):
        return out_file.readline()
    def get_email(self,out_file):
        return out_file.readline()
    def __str__(self):
        return f'My name is {self.name}\nMy phone no. is {self.phone_no}\n'
def main():
    c=contact('Sejal','940726345','abc@gmail.com')
    out_file=open('contactMe.txt','r+')
    #out_file.write(c.__str__())
    
    c.set_name(input('Enter the name'),out_file)
    c.set_phone(input('Enter the phone no'),out_file)
    c.set_email(input('Enter the email address'),out_file)
    print(c.get_name(out_file),c.get_phone(out_file),c.get_email(out_file))
    out_file.close()
    
    
main()
