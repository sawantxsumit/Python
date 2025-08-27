import os

def rename_file(old_file , new_file):
    try:
        os.rename(old_file, new_file )
        return True
    except OSError as e:
        print(f"error renaming file {e}")
        return False
    
    
old= "new_test.txt"
new= "test.txt"

if(rename_file(old , new)): #default for true
    print("renamed succesfully")
else:
    print("renaming unsuccesful")
    