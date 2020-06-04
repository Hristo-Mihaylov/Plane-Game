import datetime, os
from difflib import SequenceMatcher
start_time = datetime.datetime.now() # We define the start time of the process, in order to calculate the elapsed time

def sentence(): # We define a function about spellchecking a sentence


	sent = input("─────────> Enter a sentence to spellcheck: ")  # The user enters his sentence

	sent1 = sent.lower() # Transforms the sentence in small letters only
	words = sent1.split() # Splits the words in the sentence
	list_of_words = list() # Create an empty list

	with open("EnglishWords.txt") as file:
		list_of_words = [line.rstrip() for line in file]  # We put every word in
                                                              #EnglishWords.txt in the list list_of_words

	count_words, count_correct, count_not_correct = 0, 0, 0 # Counters
	print("┌───────────────────────────────────────────────────────┐")
	for word in words:
		count_words +=1
		alpha_word = "" # A variable which will contain only small letters (a-z)
		for letter in word:
			asc = ord(letter)
			if asc in range (ord('a'), ord('z') + 1): # We check the ASCII code of every char
				alpha_word = alpha_word + chr(asc)
		if (alpha_word in list_of_words):
			print ("│ " + str(alpha_word) + " spelt correctly" +" "*(38-len(str(alpha_word))) + "│")
			count_correct +=1
		elif (alpha_word == ""):
			count_words = count_words - 1 # When the alpha_word is simply " ", not to count it as a word
										  # For example, if we have a number, it will be transformed to " "
			continue
		else:
			print ("│ " + str(alpha_word) + " not found in dictionary" + " "*(30-len(str(alpha_word)))+ "│")
			count_not_correct +=1

	print("└───────────────────────────────────────────────────────┘")
	end_time = datetime.datetime.now()
	elapsed_time = end_time - start_time  # Calculating the elapsed time
	print ("┌────────────────────────────────────────────────────────────────────────────────┐")
	print ("│  Number of words: " + str(count_words) + " "*(61-len(str(count_words))) + "│")
	print ("│  Number of correctly spelt words: " + str(count_correct) + " "*(45-len(str(count_correct))) + "│")
	print ("│  Number of incorrectly spelt words: " + str(count_not_correct) + " "*(43-len(str(count_correct))) + "│")
	print ("│                                                                                │")
	print ("│  Time elapsed: " + str(elapsed_time.microseconds) + " microseconds" + " "*(51-len(str(elapsed_time.microseconds))) + "│" )
	print ("└────────────────────────────────────────────────────────────────────────────────┘")


	end = input("──────> Press [q] to quit or any other key to continue: ")


	if (end != 'q'):
		menu()


def file(): # We define a function about spellchecking a file


	file_name = input("─────────> Enter a file name to spellcheck: ")

	while (not os.path.isfile(file_name)):
		file_name = input("─────────> !!! Enter an existing file name to spellcheck: ") # Check if the file name exists
	with open(file_name) as file_:
		text = file_.read()
	text1 = text.lower()       # By analogy with the previous function
	words = text1.split()
	list_of_words = list()

	with open("EnglishWords.txt") as file:
		list_of_words = [line.rstrip() for line in file]

	dict_count = 0 					# We define a variable for the number of words in "EnglishWords.txt"
	for a_word in list_of_words:
		dict_count += 1

	count_words, count_correct, count_not_correct = 0, 0, 0
	ignore_count, mark_count, add_count = 0, 0, 0 	# Define counters
	newtext = "" # We define a string, which will be the sentence we write in the new file

	for word in words:
		count_words +=1
		alpha_word = ""
		for letter in word:
			asc = ord(letter)							# The same procedures as above
			if asc in range (ord('a'), ord('z') + 1):
				alpha_word = alpha_word + chr(asc)
		if (alpha_word in list_of_words):
			count_correct +=1
			newtext += alpha_word + " "
		elif (alpha_word == ""):
			count_words = count_words - 1
			continue
		else:
			count_not_correct += 1
			print ()
			print ("!!! ────> " + str(alpha_word) + " not found in dictionary\n")
			score = SequenceMatcher(None, alpha_word, list_of_words[0]).ratio()  # We let the variable score be equal to
																				 # the ration of the given word and the
																				 # first word in the dictionary
			for member in range (1, dict_count): # A loop through all of the words in "EnglishWords.txt"
												 # using their number
				current = SequenceMatcher(None, alpha_word, list_of_words[member]).ratio() # A variable for the ratio
				if (current > score):  # check if the ration is bigger. If it is, the score becomes the new ratio
					score = current
					newword = list_of_words[member] # We also save the word in a new variable, so that we can output it
			print ("┌─────────────────────────────┐")
			print ("│ " + alpha_word + " "*(28-len(alpha_word)) + "│")
			print ("│                             │")
			print ("│ did you mean                │")
			print ("│                             │")
			print ("│ " + newword + " "*(28-len(newword)) + "│")
			print ("└─────────────────────────────┘")

			while (True):
				print()
				answer = input ("──────> Enter [y] for yes or [n] for no: ")
				if (answer == "y"):
					alpha_word = newword			# If yes, the word is removed and the correct word is written
					newtext = newtext + alpha_word + " "
					count_not_correct = count_not_correct - 1
					count_correct += 1							# Also write that it is a corectly spellt word
					break
				elif (answer == "n"):
					print ("┌─────────────────────────────────┐")
					print ("│ 1. Ignore the word              │")
					print ("│ 2. Mark the word as incorrect   │")
					print ("│ 3. Add word to dictionary       │")
					print ("└─────────────────────────────────┘")

					print()
					choice = input("──────> Enter choice: ")


					while (choice not in ["1", "2", "3"]):  # Validates the input
						choice = input("───────> !!! Invalid input. Please select either 1, 2 or 3: ")
					if (str(choice) == "1"):
						ignore_count += 1
						newtext = newtext + "!" + alpha_word + "!" + " "  # When the user selects 1

					elif (str(choice) == "2"):
						mark_count += 1
						newtext = newtext + "?" + alpha_word + "?" + " "  # When the user selects 2

					elif (str(choice) == "3"):
						add_count += 1
						newtext = newtext + "*" + alpha_word + "*" + " "  # When the user selects 3
						with open ("EnglishWords.txt", "a") as file:
							file.write("\n" + alpha_word)				  # Appends the word to the dictionary
					break

				else:
					print ("!!! ───────> Invalid input. Please try again: ")


	end_time = datetime.datetime.now()			# Output
	elapsed_time = end_time - start_time
	print ("┌─────────────────────────────────────────────────────────────────────────────┐")
	print ("│ Number of words: " + str(count_words) + " "*(59-len(str(count_words))) + "│")
	print ("│ Number of correctly spelt words: " + str(count_correct) + " "*(43-len(str(count_correct)))+"│")
	print ("│ Number of incorrectly spelt words: " + str(count_not_correct) + " "*(41-len(str(count_not_correct)))+"│")
	print ("│   Number ignored: " + str(ignore_count) + " "*(58-len(str(ignore_count))) + "│")
	print ("│   Number marked: " + str(mark_count) + " "*(59-len(str(mark_count))) + "│")
	print ("│   Number added to dictionary: " + str(add_count) + " "*(46-len(str(add_count))) + "│")
	print ("│                                                                             │")
	print ("│ Time elapsed: " + str(elapsed_time.microseconds) + " microseconds" + " "*(49-len(str(elapsed_time.microseconds))) + "│")
	print ("└─────────────────────────────────────────────────────────────────────────────┘")


	with open ("_201_checkMe.txt", "w") as file:			# Create a new file and write in it
		file.write(datetime.datetime.now().strftime("%c"))	# Date and time
		file.write("\nNumber of words: " + str(count_words))
		file.write("\nNumber of correctly spelt words: " + str(count_correct))
		file.write("\nNumber of incorrectly spelt words: " + str(count_not_correct) + "\n")
		file.write("	Number ignored : " + str(ignore_count) + "\n")
		file.write("	Number marked: " + str(mark_count) + "\n")
		file.write("	Number added to dictionary: " + str(add_count) + "\n")
		file.write("\n")
		file.write(newtext)

	end = input("──────> Press [q] to quit or any other key to continue: ")


	if (end != 'q'):
		menu()


def menu(): # We define a function about the menu, i.e the main output when you run the program
	print ("┌──────────────────────────────┐")
	print ("│S P E L L   C H E C K E R     │")
	print ("│" + " " * 30 + "│")
	print ("│1. Check a file               │")
	print ("│2. Check a sentence           │")
	print ("│" + " " * 30 + "│")
	print ("│0. Quit                       │")
	print ("└──────────────────────────────┘")
	while True:
		num = input("─────────> Enter your number: ")
		if (str(num) == "1"):
			file()				# If the user selects 1, we call the file spellchecking function
			return
		elif (str(num) == "2"):
			sentence()			# If the user selects 2, we call the sentence spellchecking function
			return
		elif (str(num) == "0"):
			return				# If the user selects 0, it exits the program
		else:
			print("┌─────────────────────────────────────────────────┐")
			print("│ Invalid input. Please, choose either 0, 1 or 2  │") # Validate the input
			print("└─────────────────────────────────────────────────┘")

menu() 		# We call the menu() function
