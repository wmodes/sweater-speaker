"""say_sweaters.py: A program to help you choose sweaters."""
__author__      = "Wes Modes"
__copyright__   = "2016, CC-NC"

# We import the os module to access 'say'
import subprocess
import os
# import random for random numbers/choices
import random

# rather than generate a random response, ala
#	from random import randint
#	print(randint(0,9))
# instead we use the hash function and mod to 
# generate a consistent number based on the string

##########
# CONSTANTS
# 	All user-serviceable parts should be up here

# we define our sweater list
SWEATERS =  ["wool", "cahsmere", "vest", "cotton", "plaid"]

# here's our welcome & goodbye messages
WELCOME = "Let's plan our sweaters for the next week!"
INSTRUCT = "Type 'exit' to exit."
GOODBYE = "With all the sweaters in our future, " + \
	"I'm looking forward to the next several days."
INTRO = "Hello, I'm {0}."

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

##########
# GLOBALS
# 	Any global variables are here


##########
# FUNCTIONS
# 	Here we do all the heavy-lifting

def get_voices():
	# fancy linux command that returns the list of english 
	# 	voices on this machine
	voice_cmd = "say -v '?' | grep 'en_'|  cut -d ' ' -f 1"
	return os.popen(voice_cmd).read().split('\n')

def say(str, voice):
	print str
	if (voice):
		say_args = "-v" + voice
	else:
		say_args = ""
	# we use a system call to run the say command
	# new secure way
	subprocess.call(["say", say_args, str])
	# old insecure way
	#	os.system('say  "' + str + '"')

def main():
	# choose a random voice from one installed on this system
	voice_list = get_voices()
	voice = random.choice(voice_list)
	# we use the newer version of string interpolation, e.g.,
	# 	"all {0} things".format(5) 
	# replaces
	# 	"all %s things" % 5
	voice_str = INTRO.format(voice)
	say(voice_str, voice)

	# say our welcome message
	say(WELCOME, voice)
	print(INSTRUCT)

	day_count = 0

	# loop forever
	while (True):
		# let's get tricky with how we say the day
		if (day_count == 0):
			day_str = "today"
		elif (day_count == 1):
			day_str = "tomorrow"
		else:
			day_str = "on day " + str(day_count)
		ask_str = ASK.format(day_str)
		say(ask_str, voice)
		sweater = raw_input()
		if (sweater.lower() == "exit"):
			break
		else:
			# if sweater is not already in the input, add it to the end
			if "sweater" not in sweater:
				sweater += " sweaters"
			say(sweater, voice)
			response_index = hash(sweater) % len(RESPONSES)
			response_str = RESPONSES[response_index].format(sweater)
			say(response_str, voice)
		day_count += 1

	say(GOODBYE, voice)

if __name__ == "__main__":
	main()