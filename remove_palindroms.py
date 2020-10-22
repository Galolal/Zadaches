def remove_palindroms(spells):
    for i in spells:
        if i[::1].lower() == i[::-1].lower():
            spells.remove(i)
    return spells
