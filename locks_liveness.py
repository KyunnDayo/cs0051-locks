'''
Activity: Concurrent Counter
 Create a python program that will implement a concurrent counter that allows multiple threads to increment and decrement its value safely using a reentrant lock

 Instructions:
 	- Create a variable called 'counter' and intiliaze 0
 	- Create a reentrant lock using the function

Screen shot your codebased and output and paste it in our canvas account.Lock and Liveness

- Reentrant Lock
	- a reentrant lock also known as recursive lock or recursive mutex
		- it allows a thread to acquire the same lock multiple times without causing a deadlock. It maintain a count of the number if times if has been acquired and ensures that the thread that acquired the lock must release it the same number
'''
	count(){
		lock()
		counter++
		unlock()
	}

	def function(name):
		with lock:
			print(f'{name} acquired the lock.')
			count(name)

	def count(name):
		with lock:
			print(f'{name} acquired the lock again.')

	thread1 = threading.Thread(target=function, args = ('Thread 1'))
	thread2 = threading.Thread(target=function, args = ('Thread 2'))

'''
	Output:
	Thread 1 acquired the lock.
	Thread 1 acquired the lock again.
	Thread 2 acquired the lock.
	Thread 2 acquired the lock again.

- Try Lock
	- a try lock allows a thread to attempt acquiring a lock and it return immediately wiht a boolean value indicating whether the lock is acquired or not. This is useful when we want to acquire a lock it its available and perform an alternative action if it's not


	database record - updating   user 1 - ensure only one thread at a time
								 user 2
								 user 3
'''
	lock = threading.Lock()
	database_record = {
			"id": 101,
			"name": "Juan Dela Cruz",
			"age": 16
	}


	def update_database_record(new_name):
		if lock.acquire(blocking = False):
			try:
				print("Updating database record. . . ")
				database_record["name"] = new_name
				print("Database record updated: ", database_record)
			finally:
				lock.release()
		else:
			print("Unable to acquire the lock. Performng alternative action.")

thread1 = threading.Thread(target=database_record, args = ('Perla Bautista'))
'''
#the try mechanism allows threads to check if the lock is available without waiting and decide on an appropritate course of action
Output
	Updating database . . .
	Database recoed updated: {"id": 101, "name": "Perla Bautista", "age": 16}
	Unable to acquire the lock,. Performing alternative action.

- Read-write lock

Mini-Activity: Concurrent Counter
 Create a python program that will implement a concurrent counter that allows multiple threads to increment and decrement its value safely using a reentrant lock

 Instructions:
 	- Create a variable called 'counter' and intiliaze 0
 	- Create a reentrant lock using the function

Screen shot your codebased and output and paste it in our canvas account.
'''