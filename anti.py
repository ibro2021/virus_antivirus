



# import required module
import hashlib
import os
# assign directory
directory = os.getcwd()
hashedvirus= "19869690e7dfa834d50707ad0cc8a071"
# itrate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        hashedfile= hashlib.md5(open(f,'rb').read()).hexdigest()
       # print(f)
        print(hashedfile)
        if(hashedfile==hashedvirus):
           print(f)
            # os.remove(f)
