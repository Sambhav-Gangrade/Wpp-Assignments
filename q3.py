def checkpangram(str):
    newstr=str.lower()
    lst=[]
    count=0
    lst=list(newstr)
    seclist=[]
    for i in lst:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            if i in seclist:
                continue
            else :
                seclist.append(i)
                count+=1
    if count==26:
        print("pangram")
    else:
        print("Not a pangram")
str=input("Enter a string : ")
checkpangram(str)