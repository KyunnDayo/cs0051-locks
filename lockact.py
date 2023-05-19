import threading
 
lock = threading.RLock()

counter = 0

def counteradd(n):
	global counter

	lock.acquire()
	try:
		if n > 0:
			counter += 1
			print('lock acquired')
			print('counter = ', counter)

			counteradd(n - 1)
	finally:
		lock.release()

threads = []
for _ in range(2):
	t = threading.Thread(target=counteradd, args=(2,))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print('final lock counter:', counter)