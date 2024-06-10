import urllib.request
import re

fp = urllib.request.urlopen("https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge")
data = fp.read()
myString = data.decode("utf8")
fp.close()

result = ''

index = 0
tmpStr = ''
myCodes = []
myDivs = []
mySpans = []
myIs = []
values = []

while index < len(myString):
    tmpStr += myString[index]
    index += 1

    if 'code' in tmpStr:
        tmpStr = ''
        while index and "</code>" not in tmpStr:
            tmpStr += myString[index]
            index += 1
        myCodes.append(tmpStr)
        tmpStr = ''

for code in myCodes:
    index = 0
    tmpStr = ''

    while index < len(code):
        tmpStr += code[index]

        if 'div' in tmpStr:
            tmpStr = ''
            while index < len(code) and '</div>' not in tmpStr:
                tmpStr += code[index]
                index += 1
            myDivs.append(tmpStr)
            tmpStr = ''

        index += 1

for div in myDivs:
    index = 0
    tmpStr = ''

    while index < len(div):
        tmpStr += div[index]

        if 'span' in tmpStr:
            tmpStr = ''
            while index < len(div) and '</span>' not in tmpStr:
                tmpStr += div[index]
                index += 1
            mySpans.append(tmpStr)
            tmpStr = ''

        index += 1

for span in mySpans:
    index = 0
    tmpStr = ''

    while index < len(span):
        tmpStr += span[index]

        if 'i' in tmpStr:
            tmpStr = ''
            while index < len(span) and '</i>' not in tmpStr:
                tmpStr += span[index]
                index += 1
            myIs.append(tmpStr)
            tmpStr = ''

        index += 1

htmlData = ''.join(myIs)

pattern = r'<i class="ramp char" value="([^"]+)"></i>'

# Extracting all matches
values = re.findall(pattern, htmlData)

# Printing the extracted values
print(''.join(values))