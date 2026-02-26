import keyword

print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("print"))   # False — print nu este keyword!
print(keyword.iskeyword("True"))    # True
print(keyword.kwlist)               # Afișează lista completă de keywords