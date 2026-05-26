'''
>>> p.join(("apple", "banana", "carrot"))
'apple, banana, and carrot'
>>> p.join(("apple", "banana"))
'apple and banana'
>>> p.join(("apple", "banana", "carrot"), final_sep="")
'apple, banana and carrot'
>>> p.join(('apples', 'bananas', 'carrots'), conj='and even')
'apples, bananas, and even carrots'
>>> p.join(('apple', 'banana', 'carrot'), sep='/', sep_spaced=False, conj='', conj_spaced=False)
'apple/banana/carrot'
'''

import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
        print()
    else:
        names.append(name)
    
phrase = p.join(names)

print("Adieu, adieu, to", phrase)