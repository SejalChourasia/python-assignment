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
        return f'My name is {self.name} and phone no. is {self.phone_no}'
def main():
    c=contact('Sejal','940726345','abc@gmail.com')
    c.set_name(input('Enter the name'))
    c.set_phone(input('Enter the phone no'))
    c.set_email(input('Enter the email address'))
    print(c.get_name(),c.get_phone(),c.get_email())
    print(c)
main()
