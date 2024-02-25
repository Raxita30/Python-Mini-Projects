print("Let's add a information about a laptop")

Laptop=input("Laptop Name")
Screen_size=input("Enter screen size in inches")
RAM_size=input("RAM Size")
SSD_size=input("SSD Capacity")
Graphic_card=input("Graphic Card")
Processor=input("Processor")
Battery_backup_hr=input("Battery backup hour")
Warrenty_year=input("Warrenty for")


madlib=f"Hello, the {Laptop} laptop you are looking for has the screen size of \
{Screen_size} inch with the {RAM_size} GB RAM, {SSD_size} GB SSD, \
the graphic card is {Graphic_card} and the processor is {Processor}.\
Provides battery backup upto {Battery_backup_hr} and has the warrenty of {Warrenty_year} years."
print(madlib)
