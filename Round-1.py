user_in=input()
arr=[int(a) for a in user_in.split()]
print(arr)

if arr[::1]!=arr[::-1]:
    fmax=arr[0]
    smax=arr[1]
    for i in range (0,len(arr)):
        if (arr[i]>fmax):
            fmax=arr[i]
    print ("First Largest element is: ",fmax)

    for i in range (0,len(arr)):
        if (arr[i]<fmax and arr[i]>smax):
            smax=arr[i]
    print("Second Largest element is: ",smax)
else:
    print("there is no different values")
