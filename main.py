def numWords(b) -> int:
    return len(b.split())

def charCount(b):
    strang = b.lower()
    ret = {}
    for i in strang:
        if i not in ret:
            ret[i] = 1
        else:
            ret[i] += 1
    return ret, sum(ret.values())

def reformat(chars):
    kees = list(chars.keys())
    alphas = []
    print("\n")
    for i in kees:
        if i.isalpha():
            val = chars[i]
            alphas.append({"letter":i,"num":val})
    print('\n')
    return alphas


def sort_on(dict):
    return dict["num"]

def main():
    boo = open("./books/frankenstein.txt", "r")
    boo = boo.read()
    print(boo)
    print(f"Number of words: {numWords(boo)}\n")
    chrs = charCount(boo)
    print(f"Number of each character, and total characters: {chrs}")
    final = reformat(chrs[0])    
    final.sort(reverse=True, key=sort_on)
    for thing in final:
        print(f'''The '{thing["letter"]}' was found {thing["num"]} times''')



main()