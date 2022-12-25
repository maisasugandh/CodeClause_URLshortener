import pyshorteners

link= input("Enter the url for shorting :")
shortener=pyshorteners.Shortener()

newlink=shortener.tinyurl.short(link)

print("newlink:",newlink)
