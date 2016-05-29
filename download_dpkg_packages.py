#! /usr/bin/python2.7

import os

from os import system

prev_dir = os.getcwd()

system("sudo apt-get install curl")
try:
    main_dir = "all_downloaded_files/"

    if not os.path.exists(main_dir):
        os.makedirs(main_dir)

    # all dpkg packages
    programs_with_url = {"sublime.deb": "https://download.sublimetext.com/sublime-text_build-3114_amd64.deb",
                         "dropbox.deb": "https://www.dropbox.com/download?dl=packages/debian/dropbox_2015.10.28_amd64.deb",
                           "skype.deb": "https://get.skype.com/go/getskype-linux-beta-ubuntu-64"}

    os.chdir(main_dir)

    for program in programs_with_url:
        print("now downloading "+program)
        system("wget -O "+program+" "+programs_with_url[program])
        print("installing "+program)
        system("sudo dpkg -i "+program)
        print("remove "+program+" from computer")
        system("rm "+program)
        print(program+" installed succesfully")
except:
    print("Something was wrong...")

os.chdir(prev_dir)
