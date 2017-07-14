#import nltk # Natural language toolkit


# Establish database scheme via ORM
# =================================


# Ask the user for the name of the file they want to load. Clean and load text file into memory, or re-prompt for file name is first file was not found, was empty, or was in the wrong format. Learning platform outputs to *.txt files, which must be in "logs" directory
messages = []
while len(messages) == 0:
    print "\n\n Welcome to the command-line chat log analysis utility suite."
    filename = raw_input("\nEnter the name of the logfile you want to load and press enter: logs/")
    try:
        logfile = open('logs/'+filename, 'r')
        messages = logfile.readlines()
    except:
        print "I'm sorry, that file is either empty, not a .txt file, or not in the logs folder."


count = 0
dirtycount = 0
for m in messages:
    try:
        timestamp = m.split("From")[0].strip()
        user = m.split("From ")[1].split(" : ")[0]
        message = m.split(" : ")[1].strip()
        count+=1
    except:
        print m
        dirtycount+=1

print count, "total messages extracted successfully.", dirtycount, " messages had errors."

logfile.close()


# Offer analysis options

# (1) Keyphrase search plus context printer (e.g. search for "libertarian" or "mobilizing" and output chat message it occurs in, plus its user and date)
# (2) Engagement metrics (Pull top commentors, plus who is talking and how often?)
# (3) Threads (pull out and analyze threads where users are talking to each other)
# (4) Conceptual development (chronolical threads of use of X term by Y user over time)
