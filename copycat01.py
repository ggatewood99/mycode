#!/usr/bin/env python3

#import additional code
import shutil
import os

def main():
    #moves to directory
    os.chdir("/home/student/mycode/")
    
    #copies file1 to file2
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copies the directory
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
