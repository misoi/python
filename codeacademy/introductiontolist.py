numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

#appendind list
suitcase = []
suitcase.append("sunglasses")


suitcase.append("toothpaste")# Your code here!
suitcase.append("toothbrush")
suitcase.append("jelly")


list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#list slicing

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]              # Third and fourth items (index two and three)
last   = suitcase [4:len(suitcase)]              # The last two items (index four and five)

#slicing list a characters

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]

#more with for

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
   square_list.append(number**2) # Your code here!
square_list.sort()

print square_list
