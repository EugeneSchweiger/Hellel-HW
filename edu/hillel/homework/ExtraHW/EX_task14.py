
import os
def directory_size(path):
    size = 0
    for item in os.walk(path):
        for file in item[2]:
            size += os.path.getsize(os.path.join(item[0], file))
    if 0<size<1024:
       return str(size) +" bites"
    elif 1025<size<1048576:
        return str(round(size/1024,5)) +" k.bites"
    elif 1048577<size<1073741824:
        return str(round(size/1024/1024,5)) +" m.bites"

# from os.path import join, getsize
# def directory_size2(path):
#     size=0
#     for root, dirs, files in os.walk(path):
#             size+=sum([getsize(join(root, name)) for name in files])
#             if 'CVS' in dirs:
#                 dirs.remove('CVS')
#     return size
# path=input("enter path")
# print(float(directory_size(path))/1024/1024,"mb" )
# print(float(directory_size2(path))/1024/1024,"mb"  )

def traverse_dir(dir, indent_level=0):
    for name in os.listdir(dir):
        if not name.startswith("."):
            try:
                path = os.path.join(dir, name)
                prefix = indent_level*(" "*4)
                if os.path.isfile(path):
                    print("%s (%d bytes)" % (prefix + "╰─── " + name,
                                             os.path.getsize(path)))
                else:
                    print(prefix + name + ":"+"   (",directory_size(path),")")
                    traverse_dir(path, indent_level+1)
            except Exception as ex:
                print(ex)
path=input("enter path")
traverse_dir(path)