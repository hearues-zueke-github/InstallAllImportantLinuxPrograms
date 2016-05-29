#! /usr/bin/python2.7

import os

from os import system

# add all apt repositorys and install afterwards

def update():
    system("sudo apt-get update")

# do the command "sudo add-apt-repository %repo"
repos_with_programs = {"ppa:nilarimogard/webupd8": ["grive"],
                       "ppa:webupd8team/java": ["oracle-java6-installer", "oracle-java7-installer", "oracle-java8-installer"]}

command_add_repo = "sudo add-apt-repository -y "

for repo in repos_with_programs:
    print("add new repo "+repo)
    system(command_add_repo+repo)

print("now do a update")
system("sudo apt-get update")

for repo in repos_with_programs:
    for program in repos_with_programs[repo]:
        print("now installing "+program)
        system("sudo apt-get install -y "+program)

system("sudo update-java-alternatives -s java-8-oracle")
