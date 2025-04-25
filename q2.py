def cutchocolate(k):
    half=k//2
    return(half*(k-half))

input=int(input("Enter the maximum number of cuts to make : "))
print(f"Maximmum number of pieces that can be made with {input} cuts is",cutchocolate(input))