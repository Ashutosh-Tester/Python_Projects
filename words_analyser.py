""" This is a class called Wordplay, which has a field that holds a list of words. The user
 of the class passes a list of words they want to use to the class. The class has the 
 following methods:
 • words_with_length(length)— returns a list of all the words of length length
 • starts_with(s)— returns a list of all the words that start with s
 • ends_with(s)— returns a list of all the words that end with s
 • palindromes()— returns a list of all the palindromes in the list
 • only(L)— returns a list of the words that contain only those letters in L
 • avoids(L)— returns a list of the words that contain none of the letters in L """



class Wordplay:
    def __init__(self, a_list):
        self._a_list = a_list

    def words_with_length(self, length):
        new_list = []
        for i in  self._a_list:
            if len(i) == length:
                new_list.append(i) 
        return new_list

    def starts_with(self, letter):
        new_list = []
        for i in self._a_list:
            if i[0] == letter:
                new_list.append(i)
        return new_list

    def ends_with(self, letter):
        new_list = []
        for i in self._a_list:
            if i[-1] == letter:
                new_list.append(i)
        return new_list

    def palindromes(self):
        new_list = []
        for i in self._a_list:
            if i == i[ : :-1]:
                new_list.append(i)
        return new_list

    def only(self, a_string):
        new_list = []
        for i in self._a_list:
            for j in a_string:
                if j in i:
                    new_list.append(i)
        return new_list

    def avoids(self, a_string):
        new_list = []
        for i in self._a_list:
            for j in a_string:
                if j not in i:
                    new_list.append(i)
        return new_list

    def __str__(self) -> str:
        return '{}'.format(self._a_list)
 

if __name__ =='__main__':
    data = ['emmanuel', 'chimajieyedhor', 'ogu', 'abba']

    words_analyser = Wordplay(data)
    print(words_analyser.words_with_length(3))
    print(words_analyser.starts_with('c'))
    print(words_analyser.ends_with('l'))
    print(words_analyser.palindromes())
    print(words_analyser.only('a'))
    print(words_analyser.avoids('a'))