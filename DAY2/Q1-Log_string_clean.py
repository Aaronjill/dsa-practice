#Problem 1 — Warm-up 🔥
#Topic: String methods + clean functions
#Target: 5–8 min
#Your pipeline logs fruit labels but sometimes they come in messy — extra spaces, mixed case, random formatting.
#Write a function clean_label(label) that:
#Strips leading/trailing spaces
#Converts to lowercase
#Replaces any internal spaces with underscores

def clean_label(label):
	clean_strip= label.strip()
	clean_strip= clean_strip.replace(" ","_")
	clean_strip= clean_strip.lower()
	return clean_strip

print(clean_label("  Granny Smith  "))  # → "granny_smith"

print(clean_label("ROTTEN MANGO "))     # → "rotten_mango"
print(clean_label("apple") )           # → "apple"