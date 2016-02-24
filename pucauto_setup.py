#!/usr/bin/env python

import json

def write_config(object,variable,value):
	object[0][variable]=value
	return object
	
def make_json(object):
	with open('config.test.json','w') as outfile:
		json.dump(config[0], outfile, sort_keys = True, indent = 4)
	return True

def setup_email():
	print("Will now set up and send a test email\n")
	import imp
	email = imp.load_source('python_gmail', '../python_gmail/python_gmail.py')
	with open("config.json") as config:
		CONFIG = json.load(config)
	email.email(CONFIG.get("send_email_to"),"Pucauto Test Email","Your email is working!")
	return True
	
if __name__ == "__main__":
	config = [{}]
	
	print ("\nThis will guide you through setting up and configuring Pucauto\n")
        
        setup_config = raw_input("Would you like to setup the config file? (Y/n): ")

        if setup_config:
            config = write_config(config,"username",raw_input("Pucatrade Username: "))

            #encrpyt pw?
            config = write_config(config,"password",raw_input("Pucatrade Password: "))

            config = write_config(config,"min_value",input("Minimum bundle value for trades: "))

            config = write_config(config,"hours_to_run",input("Hours to run before restarting (0 for no restart): "))

            use_timestamp = raw_input("Would you like to display timestamps? (Y/n): ")
            if use_timestamp=="Y" or use_timestamp=="y":
		config = write_config(config,"use_timestamp",True)
            else:
		config = write_config(config,"use_timestamp",False)
            
            find_add_ons = raw_input("Would you like to find add on trades? (Y/n): ")
            if find_add_ons=="Y" or find_add_ons=="y":
		config = write_config(config,"find_add_ons",True)
		config = write_config(config,"minutes_between_add_ons_check",input("Minutes between addons check: "))
            else:
		config = write_config(config,"find_add_ons",False)
            
            send_email = raw_input("Would you like to send notification emails? (Y/n): ")
            if send_email=="Y" or send_email=="y":
		send_email = "true"
		config = write_config(config,"send_email",True)
		config = write_config(config,"send_email_to",raw_input("Send email to: "))
		config = write_config(config,"email_subject",raw_input("Email subject: "))
            else:
		send_email = "false"
		config = write_config(config,"send_email",False)
        
            print("\nCreating config.json...")
            make_json(config)

	install_packages = raw_input("Would you like to install packages? (Y/n): ")
	if install_packages=="Y" or install_packages=="y":
		import pip
		pip.main(["install",'-r',"requirements.txt"])
		if send_email:
			pip.main(["install","--upgrade","google-api-python-client"])

	# Set up email
	if send_email:
		setup_email()
