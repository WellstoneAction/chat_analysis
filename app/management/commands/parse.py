from django.core.management.base import BaseCommand, CommandError
from app.models import Person, Message, Training, Lesson, Series

# =============================================
# Parse and store messages from chat log plaintext files
# =============================================

# To run this command, from the app's main directory type: python manage.py parse <logfile>

class Command(BaseCommand):
    help = 'Parses the specified chat log and adds components to database'

    def handle(*args, **options):
        messages = []
        print "\n\n\n\n\nWelcome to the command-line chat log analysis tool suite."
        while len(messages) == 0:

            # Ask the user for the name of the file they want to load. Clean and load text file into memory, or re-prompt for file name if first file was not found, was empty, or was in the wrong format. Learning platform outputs to *.txt files, which must be in "logs" directory

            #filename = raw_input("\nEnter the name of the logfile you want to load and press enter: logs/")
            filename = 'chat.txt'
     
            count = 0
            users = []
            dirty_lines = []

            try:
                logfile = open('logs/'+filename, 'rb')
                messages = logfile.readlines()

                for m in messages:
                    try:
                        raw_line = m.split("From ")
                        timestamp = raw_line[0].strip("\t")
                        raw_message = raw_line[1].split(" : ")
                        screenname = raw_message[0]
                        if screenname not in users:
                            users.append(screenname)
                        print screenname
                        text = raw_message[1].strip("\n")
                        count+=1
                    except:
                        dirty_lines.append(m)
                logfile.close()
            except:
                print "I'm sorry, that file is either empty, not a .txt file, or not in the logs folder."
        
            
            print count, "total messages extracted successfully.", len(dirty_lines), " messages had errors."
            print len(users), "users"

