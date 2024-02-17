import os
import cat_service
import platform
import subprocess
def main():
    print_header()
    folder=get_or_create_outpat_folder() 
    print("Found or created folder: "+ folder)
    download_cats(folder)
    display_cats(folder)
    
    
def print_header():
    print("--------------------------------")
    print("\t Cat Factory")
    print("--------------------------------")
    
def get_or_create_outpat_folder():
    folder= 'Cat_Pictures'
    full_path= os.path.join(".",folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)
    return full_path

def download_cats(folder):
    cat_count=8
    for i in range(1,cat_count+1):
        # print(i, end=', ')
        name = 'lolcat_{}'.format(i)
        print("downloading cat"+ name)
        cat_service.get_cat(folder,name)
    print("done")

def display_cats(folder):
    print('Displaying cats in os windows.')
    if platform.system()== 'Darwin':
        subprocess.call(['open',folder])
    elif platform.system()=='Windows':
        subprocess.call(['explorer',folder])
    elif platform.system()== 'Linux':
        subprocess.call(['xdg-open',folder])
    else:
        print("Sorry we dont support your os: "+ platform.system() )
    # subprocess.Popen('explorer {}'.format(folder))
if __name__=="__main__":
    main()