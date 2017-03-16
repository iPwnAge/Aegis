#!/usr/bin/python
import sys,os

class Aegis:
    def __init__(self):
        #Class vars, I'm not sure what else I'll want to remain global to class.
        self.aegis_config = {}

    def initialize_aegis(self):
        #Aegis initialization. Here is where the aegis.json configuration is created within the user's home directory.
        print "Welcome to Aegis! Let's get started."
        print "First, I need to know where your server directory is. If you have multiple, you'll be able to add more after the first server is setup."
        initial_server = str(raw_input("Enter your server directory: "))
        #Check for trailing /
        #Scan for server.properties, get map folder name
        #Prompt user for correctness, name server configuration and ask what needs to be backed up (map, plugins, configurations, logs, whole, etc.)
        #Reloop adding more servers

    def aegis_runtime(self):
        #Sieve for sys.argv; figuring out what user wants to do, (backup, restore, stats)

    def email_update(self):
        #Email admin on backup with stats, configged during initialize_aegis

    def update_config(self):
        #Update configuration values of aegis.json

    def restore(self):
        #This should probably have its own class/file

    def backup(self):
        #This should probably have its own class/file



#Should Aegis support messaging the in-game server during a backup (i.e. notify staff channel?).
#Sounds like feature creep and since Aegis is an external script supporting that functionality would be hard
#(are they using screen? tmux? maybe a configureable command run on execution will suffice)

#Email updates will go a little like this: 'Hey, your backups increased/decreased by X. MD5 checks of all backups are A-OK. (warning, your disk is getting pretty full)'




if __name__ == "__main__":
    new_aegis = Aegis()
    if not os.path.isdir("~/.aegis_mc/"):
        new_aegis.initialize_aegis()
    else:
        new_aegis.aegis_runtime()
