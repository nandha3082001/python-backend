class bus:
	def __init__(self):
		self.bus_name=input("eneter bus name")
		self.bus_traget=input("enter the bus travel place")
		self.bus_no=int(input("enter the bus number"))
		self.bus_qty=int(input("enter the qty"))
		self.seat=['a','b','c','d','e','f','g','h','i','j','z']
		self.bus_seat=[ self.seat[i]  for  i in range(self.bus_qty)]
	def setbus_qty(self,bus_qty):
		self.bus_qty=bus_qty
	def setbus_seat(self,bus_seat):
		self.bus_seat=bus_seat
	def getbus_name(self):
		return self.bus_name
	def getbus_no(self):
		return self.bus_no
	def getbust_raget(self):
		return  self.bus_traget
	def getbus_qty(self):
		return self.bus_qty
	def getbut_seat(self):
		return self.bus_seat
class passanger(bus):
	def __init__(self):
		self.busname=input("enter the name")
		self.name=input("enter the your name")
		
		self.busno=int(input("enter the bus no"))
		self.qty=int(input("enter the  qty you need"))
		self.seatno=[]
	def setseatno(self ,seatno):
		self.seatno=seatno
	def getname(self):
		return self.name
	def getbusno(self):
		return self.busno
	def getseat(self):
		return self.seatno
	def getbusname(self):
		return self.busname
	def getqty(self):
		return self.qty
	
	

class ticket:
	
	def __init__(self):
		self.bl=[]
		self.pl=[]
	def addbus(self ,b):
		self.bl.append(b)
	def booking(self,p):
		for i in self.bl:
			if p.getbusno()==i.getbus_no(): 
				if i.getbus_qty()>0:
					
					bus_seat=i.getbut_seat()
					passanger_seat=[]
					for j in range(p.getqty()):
						print("enter the seat letter like in the list",bus_seat)
						a=input("enter")
						if a in bus_seat:
							passanger_seat.append(a)
							bus_seat.remove(a)
						else:
							print("enter correct seatlike in the list",bus_seat)
					
					
					p.setseatno(passanger_seat)
					i.setbus_seat(bus_seat)

					print("your ticket succffly booked..... make trip is peacefully with ",i.getbus_name())
					self.pl.append(p)
					q=i.getbus_qty()
					p=p.getqty()
					q=q-p
					i.setbus_qty(q)
					

					
		else:
			print("sorry this busno is invaid or invaid seat or seat is fill wether check your bus deatils")
	def get_ticket(self):
		get=input("enter the setplace like a,b,c,d")
		for i in self.pl:
			for j in i.getseat():
				if get==j:
					print(">>>>>>>>>> WELLCOME  TO ",i.getbusname()," bus <<<<<<<<<<")
					print(f"Name   :{i.getname()}")
					print(f"Bus no :{i.getbusno()}")
					
				
					print(f"seat   :{j}")
	def searchbyplace(self):
			place=input("enter the place")

			print("   |   BUSNO   |   NAME   |   PALCE  |   QUNAITY")
			for i in self.bl:
				if place==i.getbust_raget():
					print("   |   ",i.getbus_no(),"   |   ",i.getbus_name(),"   |   ",i.getbust_raget(),"   |   ",i.getbus_qty())
					print("aviable seat ")
					for j in i.getbut_seat():
						print("|",j,end="|")
					print()

					
				

	

	
	def ticket_view(self):
			print("   |   PASSAGER   |   BUS NO   |   SEAT NO  |")
			for i in self.pl:
				print("   |   ",i.getname(),"   |   ",i.getbusno(),"   |   ",i.getseat())
	def bus_view(self):
			print("   |   BUSNO   |   NAME   |   PALCE  |   QUNAITY")
			for i in self.bl:
				print("   |   ",i.getbus_no(),"   |   ",i.getbus_name(),"   |   ",i.getbust_raget(),"   |   ",i.getbus_qty())
				print("aviable seat ")
				for j in i.getbut_seat():
					print("|",j,end="|")
				print()
	
tk=ticket()
choose=1
while choose!=0:
	print("************!!!WeLLoMe  to  COIMBATORE ^^^BUS STAND !!!*************  ")
	print("ENTER 1...  IF  YOUR BUS OWNER FOR ADD BUS...IN BUS STAND  ")
	print("ENTER 2..BOOOK THE BUS FOR TRAVEL......")
	print("ENTER 3...VIEW ALL TICKET IN BUSTAND......IT NOT FOR CUSTAMER")
	print("ENTER 4...ALL  BUS IN BUSSTAND....... ")
	print("ENTER 5 .. FOR  GET TICKET ITS .. FOR HOW HAVE BOOKED THE BUS ")
	print("ENTER 6 ..FOR   SEARCH THE BUS TO TRAVEL  !!!ALERT ..SEARCH BY PLACE")
	print("ENTER 0...FOR EXIT IN APPLICATION")
	choose=int(input("Enter"))
	if choose==1:
		
		b=bus()
		tk.addbus(b)
	elif choose==2:
		p=passanger()
		tk.booking(p)
	elif choose==3:
		tk.ticket_view()
	elif choose==4:
		tk.bus_view()
	elif choose==5:
		tk.get_ticket()
	elif  choose==6:
		tk.searchbyplace()