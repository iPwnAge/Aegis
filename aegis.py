#!/usr/bin/python
import sys, os, json
from utils.term_colors import bcolors

class Aegis:
    def __init__(self, workingdir):
        #Class vars, I'm not sure what else I'll want to remain global to class.
        self.aegis_config = {
        "servers": [],
        "version": 1,
        }
        self.data_directory = workingdir

    def initialize_aegis(self):
        #Aegis first-time initialization. Here is where the aegis.json configuration is created within the user's home directory.
        print bcolors.OKBLUE + "Welcome to Aegis! Let's get started." + bcolors.ENDC
        print bcolors.OKBLUE + "First, I need to know where your server directory is. If you have multiple, you'll be able to add more after the first server is setup." + bcolors.ENDC
        self.add_server()

        #Server add loop if a user wants to bulk add servers to Aegis.
        add_more_loop = True
        while(add_more_loop):
            add_more_branch = str(raw_input("Would you like to add another server? [y|N] "))
            if len(add_more_branch) > 0 and add_more_branch.lower()[0] is "y":
                self.add_server()
            else:
                #User is done adding servers. Write current self.aegis_config to file, enter aegis_runtime().
                add_more_loop = False
                os.makedirs(self.data_directory)
                with open(self.data_directory + "aegis.json", "w+") as aegis_config_file:
                    json.dump(self.aegis_config, aegis_config_file)
                print bcolors.OKGREEN + "Aegis is fully configured. Now returning you to main menu." + bcolors.ENDC
                self.aegis_runtime()


    def add_server(self):
        ## USER INPUT: string of their server's directory root
        server_directory_string = str(raw_input(bcolors.OKBLUE + "Enter your server directory: " + bcolors.ENDC))
        if not server_directory_string.endswith('/'):
            server_directory_string += "/"

        #Check to see if it's a valid server root by checking for the existence of server.properties
        if os.path.exists(server_directory_string + "server.properties"):

        #Scan for server maps by walking all sub-folders and checking for level.dat (this should be expanded for further checks, i.e. the playerdata and region folders)
            import fnmatch
            matches = []
            for root, dirnames, filenames in os.walk(server_directory_string):
                for filename in fnmatch.filter(filenames, 'level.dat'):
                    matches.append(os.path.join(root, filename))
            #Cool, we found some maps
            if len(matches) > 0:
                print "Great. I've found " + str(len(matches)) + " maps. Here's the list:"
                for discovered_map in matches:
                    print discovered_map[len(server_directory_string):-9] #Get map "name" by only grabbing the directory substring between the length of the server directory, and before the level.dat.
            #Aegis couldn't discover any maps within the server dir. Perhaps non-standard configuration, move user to manual declaration branch.
            else:
                print bcolors.FAIL + "Hm, I couldn't find any Minecraft maps in your server folder. " + bcolors.ENDC

            #Add a lot more try/catch and general exception handling. As of right now the script throws an exception and quits out.
            #Ask user what they wish to back up
            #Ask user interval
            #Ask user email notifications (should this be added to the initialize_aegis fun?)
            #Ask user where to store backups
            #Ask user how many backups to store (time interval or data size)
            #Ask user name for server
            #Write to self.aegis_config
        else:
            print bcolors.FAIL +  "Hm, I couldn't find a server.properties within the folder you've provided. Try again?" + bcolors.ENDC
            self.add_server()


        #Scan for server.properties, get map folder name
        #Prompt user for correctness, name server configuration and ask what needs to be backed up (map, plugins, configurations, logs, whole, etc.)
        #Reloop adding more servers

    def aegis_runtime(self):
        pass
        #Sieve for sys.argv; figuring out what user wants to do, (backup, restore, stats)

    def email_update(self):
        pass
        #Email admin on backup with stats, configged during initialize_aegis

    def update_config(self):
        pass
        #Update configuration values of aegis.json

    def restore(self):
        pass
        #This should probably have its own class/file

    def backup(self):
        pass
        #This should probably have its own class/file



#Should Aegis support messaging the in-game server during a backup (i.e. notify staff channel?).
#Sounds like feature creep and since Aegis is an external script supporting that functionality would be hard
#(are they using screen? tmux? maybe a configureable command run on execution will suffice)

#Email updates will go a little like this: 'Hey, your backups increased/decreased by X. MD5 checks of all backups are A-OK. (warning, your disk is getting pretty full)'




if __name__ == "__main__":

    #Get user's home directory (with some semblance of cross-platform support)
    home = os.path.expanduser("~")
    if not home.endswith("/"):
        home += "/"
    new_aegis = Aegis(home + ".aegis_mc/")

    #Determine if Aegis has started before
    if not os.path.isdir(home + ".aegis_mc/"):
        new_aegis.initialize_aegis()
    else:
        new_aegis.aegis_runtime()
