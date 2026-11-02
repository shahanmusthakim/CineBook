class Hall:
    def __init__(self,hall_no,row,col):
        self.row=row
        self.col=col
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]
      
    def enter_show(self,show_id,movie_name,time):
        self.tuple=(show_id,movie_name,time)
        self.show_list.append(self.tuple) 
        self.seat_list=[]
        for i in range(self.row):
            row=[]
            for j in range(self.col):
                row.append('Free')
            self.seat_list.append(row)
        self.seats[show_id]=self.seat_list
        
    def view_show_list(self):
        for x in self.show_list:
            print(f'Show ID: {x[0]}\tMovie Name: {x[1]}\tTime: {x[2]}')
            
    def view_avilable_seats(self,id):
        if id not in self.seats:
            print("\nWrong ID....\n")
        else:
            for i in self.show_list:
                if(id==i[0]):
                    print(f'\nMovie Name: {i[1]}\t\tTime: Today {i[2]}\n')
            for x in range(self.row):
                for y in range(self.col):
                    if self.seats[id][x][y]=='Free':
                        print(f'{chr(x+65)}{y+1}',end='\t')
                    else:
                        print('X',end="\t")
                print('\n')
    
    def book_ticket(self,id,name,phone,booking_seats):
        self.booked_tickets=[]
        flag=0
        if id not in self.seats:
                    print("\nWrong ID....\n")
        elif len(booking_seats)==0:
            print("Please Select At Least One Seat.\n")
        else:
            for i in booking_seats:
                try:
                    r = ord(i[0].upper())-65
                    c = int(i[1:])-1
                except (ValueError, IndexError):
                    print(f"{i} is an Invalid Seat.")
                    continue               
                if r>=self.row or c>=self.col or r<0 or c<0:
                    print("Seat Doesn't Exists")
                elif self.seats[id][r][c]!='Free':
                    print(f"{i} is Already Booked.")
                else:
                    self.seats[id][r][c]='X'
                    self.booked_tickets.append(i)
                    flag=1
            if flag==1:        
                print(f'\n*****########## Ticket Booked Successfully ##########*****\n')
                print("--------------------------------------------------------------------------------\n")
                print("Name: ",name)
                print("Phone: ",phone)
                for i in self.show_list:
                    if i[0]==id:
                        print(f'Movie Name: {i[1]} \t Time: {i[2]}')
                print("Tickets: ",end=" ")
                for i in self.booked_tickets:
                    print(i,end=" ")
                print("\nHall No: ",self.hall_no)
                print("Price: ",500*len(self.booked_tickets),"TK")

        
my_hall=Hall(1,6,8)
my_hall.enter_show(147,"Domm","10:00 AM")
my_hall.enter_show(205,"Bonolota","01:00 PM")
my_hall.enter_show(241,"Rakkosh","04:00 PM")
my_hall.enter_show(334,"Pressure Cooker","09:00 PM")

while True:
    print("\n--------------------------------------------------------------------------------\n")
    print("1. View all show today.")
    print("2. View available seats.")
    print("3. Book tickets.")
    print("4. Exit.")

    option=int(input("\nEnter Your Option: "))
    if option==1:
        print("\n--------------------------------------------------------------------------------\n")
        my_hall.view_show_list()
    elif option==2:
        id=int(input("Enter Show ID: "))
        my_hall.view_avilable_seats(id)
    elif option==3:
        id=int(input("Enter Show ID: "))
        name=input("Enter Your name: ")
        phone=input("Enter Your Phone: ")
        tickets=int(input("Enter Number of Tickets: "))
        booking_seats=[]
        for i in range(tickets):
            booking_seats.append(input("Enter  Seat Number: "))
        my_hall.book_ticket(id,name,phone,booking_seats)
    elif option==4:
        print("Exit Successfully.")
        break
            
    else:
        print("\nWrong option. Choose Again.")