def spam():
    eggs = "spam local variable"
    print(eggs)

def bacon():
    eggs = "Bacon Local"
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)
