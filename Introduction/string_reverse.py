def reverse_string(s):
  word_arr = s.split(" ")
  word_arr.reverse()
  return " ".join(word_arr)


print("\n------------------------------\n")
NorString = input("\nEnter a string: ")
print("\nOriginal String: ", NorString)
print("\nReversed String: ", reverse_string(NorString))
print("\n------------------------------\n")

