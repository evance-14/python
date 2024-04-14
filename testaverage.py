# we are importing our previous myfunctions.py which had
#def average(x,y):
    #return(x+y)/2


#from myfunctions import average

#a = 2 
#b = 3

#c = average(a,b)

#print(c)

# CREATING A FUNCTION THAT RETURNS MULTIPLE VALUES
def stat(x):
    totalsum = 0
    #find the sum of all the data
    for x in data:
        totalsum = totalsum + x
        #find the mean or average.
        N = len(data)
        mean = totalsum/N

        return totalsum, mean
    data = [1,5,6,3,12,3]
    totalsum,mean = stat(data)

    print(totalsum,mean)
   

