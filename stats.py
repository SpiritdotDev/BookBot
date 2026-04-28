# opens the file at the filepath given and returns the entire file as a string
def get_book_text(filepath):
     with open(filepath) as f:
         return f.read()

# opens the file at the filepath given and returns a the entire as a list of strings
def get_book_words(filepath):
    with open(filepath) as f:
        book_as_string = f.read()
        return book_as_string.split()

#takes text from the book as a string, returns number of times 
# each character(including symbols and spaces) appears
def get_book_chars(filepath):
    with open(filepath) as f:
        book_as_string = f.read()
        book_as_lowercase = book_as_string.lower()
        chars =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z","."," ","?",",",";",":","!","*","&","/","[","]","-","_","1","2","3","4",
                "5","6","7","8","9","(",")","0", "æ","â","ê","ë","ô"]
        book_as_list = book_as_lowercase.split()
        counts = {}
        for word in book_as_list:
            for char in word:
                if char in chars:
                    if char in counts:
                        counts[char] += 1
                    else:
                        counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

#makes a sorted list from a dictionary
def get_sorted_list(dict):
    result = []

#makes a list of dictionaries out of the dictionary passed to it
    for key in dict:
        new_dict = {
            "char": key,
            "num": dict[key]
        }
        result.append(new_dict)
    result.sort(reverse=True, key=sort_on)
    return result
    


