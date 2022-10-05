def reverse_string(s):
  word_arr = s.split(" ")
  word_arr.reverse()
  return " ".join(word_arr)


#demo
sample = "My name is xyz"
print(reverse_string(sample))
