def _removeVowels(text):
    vow = ['a','e','i','o','u']
    chars = []

    for i in text:
        if i not in vow:
            chars.append(i)

    return "".join(chars)
