import camelcase
c = camelcase.CamelCase()
s = 'this is a sentence that needs CamelCasing!'
print(c.hump(s))
# This is a Sentence That Needs CamelCasing!
