'''
a.b.c
a--> major version
b--> minor version
c--> patch version

for given list of version, find the latest
latest_version[2.10.1 , 3.10.2 ]
op : 3.10.2
'''

def latest_version(v1,v2):
    
    ver1 = v1.split(".")

    ver2 = v2.split(".")

    if ver1[0] < ver2[0]:
        print(v2)
    else:
        if ver1[1] < ver2[1]:
            print(v2)
        else:
            if ver1[2] < ver2[2]:
                print(v2)
            else:
                print(v1)


latest_version("3.10.2" , "2.10.1")
