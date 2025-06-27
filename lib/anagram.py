# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self,anagram_list):
        individual_letter_list = [letter for letter in self.word]
        final_result = []

        while len(anagram_list) > 0:
            last_element = anagram_list.pop(0)
            individual_letter_list2 = [letter for letter in last_element]
            if sorted(individual_letter_list2) == sorted(individual_letter_list):
                final_result.append(last_element)
            
        return final_result

enlist = Anagram("enlist")
print(enlist.match(["listen", "silent", "hippopotamus"]))


