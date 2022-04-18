import re
text = 'abcdfghijk'
parser = re.search('a[b-f]+f', text)
print (parser)
#<_sre.SRE_Match object; span=(0, 5), match='abcdf'>

print (parser.group())
#'abcdf'

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    match = re.search(string, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text_pos)
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))


silly_string="the cat ine the hat"
pattern="the"

matches=re.finditer(pattern,silly_string)
for match in matches:
    s="Found '{group}' at {begin}:{end}".format(group=match.group(),begin=match.start(),end=match.end())
    print(s)