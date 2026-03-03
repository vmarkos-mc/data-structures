from queue import PriorityQueue
customers = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list. 
customers.put((2, "Harry", "123456")) # insert(x)
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((2, "Stacy"))
customers.put((2, "Abid"))
while not customers.empty():
     print(customers.get())

