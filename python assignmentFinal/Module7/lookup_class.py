import pickle
class Info:
	
	def __init__(self,name,phone_no,email_address):
		self.name=name
		self.phone_no=phone_no
		self.email_address=email_address
		
	def set_name(self,n):
		self.name=n
		
 		
		
	def set_phone(self,p):
		self.phone_no=p
		
	def set_email(self,e):
		self.email_address=e
		
	def get_name(self):
		return self.name
	def get_email(self):
		return self.email_address
		
	def get_phone(self):
		return self.phone_no
		

		

	def __str__(self):

		return f"Name:{self.name}, Phone_NO.:{self.phone_no}, Email_Address: {self.email_address}"


def main():
	
	while(True):
		ch=int(input("1.Search 2.Add 3. Display 4.Quit"))
		if ch==2:
			
			dict={}
			i=Info("sim","3456","@gmail.com")
			dict["name"]=input("Enter your name : ")
			dict["Email"]=input("Enter your Email_ id : ")
			dict["PH No."]=input("Enter your phone_number : ")
			i.set_name(dict["name"])
			i.set_email(dict["Email"])
			i.set_phone(dict["PH No."])
			with open('contact.txt','a') as f:
				for i,j in dict.items():
					f.write("".join(["{0} : {1}".format(i, j)]))
					f.write('\n')	
					
		if ch==3:
			r=open('contact.txt','r')
			p=r.readline()
			while p!='':
				print(p)
				p=r.readline()

		
		if ch==1:
			name=input('Enter the name of the Person')
			r=open('contact.txt','r')
			p=r.readline()
			while p!='':
            				if name in p:
                					print(p)
                					break
            				else:
                					p=r.readline()
			
		if ch==4:
			exit()
	

	

	
	

main()