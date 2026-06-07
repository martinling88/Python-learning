retrytime = 0

while retrytime >= 0:
	
	correctpw ="114514⁷"
	
	userpassword = input("ENTER YOUR PASSWORD:")

	
	if userpassword == correctpw:
		print("CORRECT PASSWORD!")
		
		break
		
	else:
		retrytime+=1
		
		print("WRONG PASSWORD!YOU HAS RETRY TIME=",(5-retrytime))
		
		import time
										
		time.sleep(1)
		
		print("TRY AGAIN!")
		
		if retrytime >= 5:
				print("YOUR ACCOUNT HAS BEEN LOCKED!")
				
				break
				
				
	
	