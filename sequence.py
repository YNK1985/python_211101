#sequence.py

s='abcd Efa bcdef'
print(s[:2])
print(s[1])
print(s[-2:])

b=s #or b=str(s)
print(b.capitalize())
print(b.count("c",3))
print(b.strip())

print(len(b))
print(b.endswith("e"))

names=["A","b","c"]
for name in names:
    f=open("c:\\work\\demo.cvs","a")
    f.write("\nhello, good to see you. {0}sir\n".format(name))
    f.write("*"*30)
    f.close()
    print("hello, good to see you. {0}sir".format(name))
    print("*"*30)






