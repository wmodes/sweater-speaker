# We import the os module to access 'say'
# old insecure way
#	import os
# new secure way
import subprocess

# rather than generate a random response, ala
#	from random import randint
#	print(randint(0,9))
# instead we use the hash function and mod to 
# generate a consistent number based on the string

# CONSTANTS
# 	All user serviceable parts should be up here

# to use a voice, make sure you download it for your system
SAY_ARGS = ""		# default voice
SAY_ARGS = "-vTessa" # English female
SAY_ARGS = "-vTessa" # English female

# we define our sweater list
SWEATERS =  ["wool", "cahsmere", "vest", "cotton", "plaid"]

# here's our welcome & goodbye messages
WELCOME = "Let's plan the sweaters we want to wear!"
INSTRUCT = "Type 'exit' to exit."
GOODBYE = "With all the sweaters in our future, " + \
	"I'm looking forward to the next several days."

# here's our ask message
ASK = "What kind of sweaters will you wear {0}? "

# responses. Choose from these using hash() and modulus
RESPONSES = [
	"Oh god, We love {0}!",
	"Sure, we like {0}.",
	"Well, {0} are okay.",
	"Honestly? I'm not so fond of {0}.",
	"I've always wanted one of those {0}.",
	"I didn't know you had any {0}.",
	"Really? {0}. Bold choice.",
	"Cool! I'll wear one of my {0} too."]

day_count = 0

def say(str):
	print str
	# we use a system call to run the say command
	# old insecure way
	#	os.system('say  "' + str + '"')
	# new secure way
	subprocess.call(["say", SAY_ARGS, str])

# say our welcome message
say(WELCOME)
print(INSTRUCT)

# loop forever
while (True):
	# let's get tricky with how we say the day
	if (day_count == 0):
		day_str = "today"
	elif (day_count == 1):
		day_str = "tomorrow"
	else:
		day_str = "on day " + str(day_count)
	# we use the newer version of string interpolation...
	# 	"found {0} things".format(5) 
	# replaces
	# 	"found %s things" % 5
	ask_str = ASK.format(day_str)
	say(ask_str)
	sweater = raw_input()
	if (sweater.lower() == "exit"):
		break
	else:
		# if sweater is not already in the input, add it to the end
		if "sweater" not in sweater:
			sweater += " sweaters"
		say(sweater)
		response_index = hash(sweater) % len(RESPONSES)
		response_str = RESPONSES[response_index].format(sweater)
		say(response_str)
	day_count += 1

say(GOODBYE)