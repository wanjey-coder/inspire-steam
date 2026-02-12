# Wanjey Gikenye
#11/2/2026
#string formatting

#get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The lenth is {string_length}")

sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")


print(f"the first subject is:",split[1])

# Make everything CAPS
mpesa_code = "ub2876r"

capitalized = mpesa_code.upper()

print("New mpesa code:", capitalized)

sentence_3 = "WE ARE CHAMPIONS"
lower_case = capitalized.lower()

print(f"lower case: {capitalized}")

#replacing characters in a string

balance = "100Kes"
amount_added = "50Kes"

new_balance = balance.replace("Kes", "")

print("cleaned balance: ", new_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("cleaned amount added:", cleaned_amount_added)

updated_balance = (int(cleaned_amount_added) + int(new_balance))
print(f"updated balance is: {updated_balance} Kes")

stuff = "CONFIRMED, you have received 40Kes from Phillip"

seperation = stuff.split(" ")
print("the amount received is :",seperation[4])