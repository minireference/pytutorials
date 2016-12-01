def check(id_, value):
	checker = _checkers[id_]
	checker(value)

_p1_dict = dict((
		(
			'alice@domain.org bob@domain.org Alice\'s Subject This is my one line message!',
			("""Great start! 
We could use some more newlines "\\n" though. Try to make it look like:
""",
"alice@domain.org\nbob@domain.org\nAlice\'s Subject\nThis is my one line message!")
		),

		(
			'alice@domain.org\nbob@domain.org\nAlice\'s Subject\nThis is my one line message!',
			("""Great job, all on different lines. 
Let\'s add some headers like "Subject: Subject" Something like this:
""",
"From: alice@domain.org\nTo: bob@domain.org\nSubject: Alice\'s Subject\nMessage: This is my one line message!")
		),
		(
			'From: alice@domain.org\nTo: bob@domain.org\nSubject: Alice\'s Subject\nMessage: This is my one line message!',
			("""Awesome, almost there.
Since the message can be long and have multiple lines let put it on a newline after "Message:" Try to make it like this:
""",
"From: alice@domain.org\nTo: bob@domain.org\nSubject: Alice\'s Subject\nMessage:\nThis is my one line message!")
		),
		(
			'From: alice@domain.org\nTo: bob@domain.org\nSubject: Alice\'s Subject\nMessage:\nThis is my one line message!',
			("""Looking pretty good.
Let\'s try one more thing. You don\'t really need the "Message:" header and let's put a bit more space between the headers and the body of the message like this:
""",
"From: alice@domain.org\nTo: bob@domain.org\nSubject: Alice\'s Subject\n\nThis is my one line message!")
		),
		(
			'From: alice@domain.org\nTo: bob@domain.org\nSubject: Alice\'s Subject\n\nThis is my one line message!',
			("""Perfect! SUCCESS!""",
			"Nothing, you are done!")
		),
	)
)

_p1_next = "alice@domain.org\nbob@domain.org\nAlice\'s Subject\nThis is my one line message!"

def p1_checker():
	global _p1_dict
	
	answer_dict = _p1_dict
	def checker(value):
		global _p1_next
		print("Your output:\n")
		print(value)
		print('\n' + '-'*40)
		if value in answer_dict:
			comment, next = answer_dict[value]
			_p1_next = next
			print("\n".join((comment, next)))
		else:

			print("I don't think that is quite right.\nTry again!\n\nWe want it to look like:\n\n{0}".format(_p1_next))
	return checker


def p3_checker(values):
	number, boolean, string = values
	if number <= 10:
		print("number has the value {0} which is smaller or equal to 10.".format(number))
		return

	if boolean == False:
		print("boolean_literal is {0} which isn't True.".format(boolean))
		return

	if not "cows" in string:
		print('The string_literal could use a few more "cows".')
		return

def p4_checker(list):
	if list == []:
		print("Your list is empty, try putting some numbers in it like 4 or 3")
		return False
	for i,v in enumerate(list):
		if i != v:
			print("The {0}th element has the value {1} not {2}".format(i,v,i))
			return False
	if i == 4:
		print("Success!")
	elif i < 4:
		print("Your list might need a few more items.")
	else:
		print("Your list might have too many items.")
	return True


_checkers = {
	"p1": p1_checker(),
	"p3": p3_checker,
	"p4": p4_checker,
}
