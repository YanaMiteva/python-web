from urllib import  parse

def decode(encoded_url):
    return parse.unquote(encoded_url)

print(decode('http://www.google.bg/search?q=C%23'))
print(decode('https://mysite.com/show?n%40m3=p3%24h0'))
print(decode('http://url-decoder.com/i%23de%25?id=23'))


tests = {
    ('http://www.google.bg/search?q=C%23', 'http://www.google.bg/search?q=C#'),
    ('https://mysite.com/show?n%40m3= p3%24h0', 'https://mysite.com/show?n@m3= p3$h0'),
    ('http://url-decoder.com/i%23de%25?id=23', 'http://url-decoder.com/i#de%?id=23')
}

for (test, expected) in tests:
    result = decode(test)
    print(result, result == expected)