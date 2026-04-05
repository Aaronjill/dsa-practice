#Problem 5 — Challenge 💪
#Topic: Stack — first introduction
#Target: 18–22 min
#Your pipeline config files use nested brackets to define processing rules. You need to verify that all brackets are properly opened and closed in the right order.
#Write a function is_valid_config(s) that returns True if all brackets are valid, False otherwise.
def is_valid_config(string):
		stack=[]
		matching = {")":"(","]":"[","}":"{"}
		for char in string:
			if char in "{[(":
				stack.append(char)
			elif char in ")}]":
				if not stack:
					return False
				if stack.pop() != matching[char]:
					return False
		return stack==[]

print(is_valid_config("[({})]") )  # → True
print(is_valid_config("[(])") )    # → False
is_valid_config("{[]}")   # → True
is_valid_config("((((")     # → False
is_valid_config("")         # → True
#Hint if needed: Think about what data structure naturally handles "last opened must be first closed."