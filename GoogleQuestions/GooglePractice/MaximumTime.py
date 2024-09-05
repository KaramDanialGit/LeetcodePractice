"""
You are given a string that represents time in the format hh:mm.
Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum
possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.
"""

def maxTime(timeString):
    hh = timeString[0:2]
    mm = timeString[3:5]

    if hh == "??":
        hh = str(23)
    elif "?" in hh:
        if hh[0] == "?":
            if int(hh[1]) >= 4:
                hh = hh[1:]
                hh = "1" + hh
            else:
                hh = hh[:1]
                hh = hh + "2"
        else:
            if int(hh[0]) == 2:
                hh = hh[:1]
                hh += "3"
            else:
                hh = hh[:1]
                hh += "9"

    if mm == "??":
        mm = str(59)
    elif "?" in mm:
        if mm[0] == "?":
            mm = mm[1:]
            mm = "5" + mm
        else:
            mm = mm[:1]
            mm = "9" + mm

    print(hh + ":" + mm)

maxTime("??:??")