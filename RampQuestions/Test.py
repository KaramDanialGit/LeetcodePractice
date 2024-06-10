#!/usr/bin/env python3

import codecs
import string
import sys
import time
import re

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP


ONE_WEEK_IN_SECONDS = 604_800


def generate_secret():
    totp = TOTP(
        key=codecs.encode(string.ascii_letters, encoding="utf-8"),
        length=8,
        algorithm=SHA1(),
        time_step=ONE_WEEK_IN_SECONDS,
        backend=default_backend(),
    )
    seed = int(time.time())
    token = codecs.decode(totp.generate(seed), encoding="utf-8")
    return f"{token}-{seed}"


# if __name__ == "__main__":
#     sys.stdout.write(
#         f"Please head to https://ramp.com/careers and use this secret when "
#         f"you apply: {generate_secret()}\n"
#     )

tmp = '"<i>class="rampchar"value="h"></i><iclass="rampchar"value="g"></i><sectionclass="rampchar"value="g"></section><iclass="rampchar"value="2"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="s"></i><iclass="rampchar"value="t"></i><sectionclass="rampchar"value="-"></section><iclass="rampchar"value="."></i><iclass="rampchar"value="d"></i><sectionclass="rampchar"value="a"></section><iclass="rampchar"value="e"></i><iclass="rampchar"value="t"></i><articleclass="rampchar"value="."></article><iclass="rampchar"value="s"></i><iclass="rampchar"value="t"></i><sectionclass="rampchar"value="h"></section><iclass="rampchar"value="-"></i><articleclass="rampchar"value="e"></article><iclass="rampchar"value="p"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="5"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="r"></i><iclass="rampchar"value="p"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="t"></i><sectionclass="rampchar"value="n"></section><articleclass="rampchar"value="2"></article><iclass="rampchar"value=":"></i><iclass="rampchar"value="/"></i><articleclass="rampchar"value="b"></article><iclass="rampchar"value="p"></i><iclass="rampchar"value="/"></i><iclass="rampchar"value="h"></i><iclass="rampchar"value="w"></i><sectionclass="rampchar"value="g"></section><iclass="rampchar"value="w"></i><iclass="rampchar"value="g"></i><articleclass="rampchar"value="3"></article><iclass="rampchar"value="e"></i><iclass="rampchar"value="g"></i><iclass="rampchar"value="g"></i><iclass="rampchar"value="h"></i><articleclass="rampchar"value="g"></article><iclass="rampchar"value="s"></i><iclass="rampchar"value="d"></i><articleclass="rampchar"value="t"></article><iclass="rampchar"value="5"></i><iclass="rampchar"value="t"></i><iclass="rampchar"value="n"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="1"></i><iclass="rampchar"value="/"></i><iclass="rampchar"value="t"></i><iclass="rampchar"value="2"></i><iclass="rampchar"value="o"></i><sectionclass="rampchar"value="5"></section><iclass="rampchar"value="/"></i><articleclass="rampchar"value="."></article><iclass="rampchar"value="2"></i><articleclass="rampchar"value="t"></article><sectionclass="rampchar"value="l"></section><iclass="rampchar"value="t"></i><iclass="rampchar"value="e"></i><sectionclass="rampchar"value="n"></section><iclass="rampchar"value="p"></i><iclass="rampchar"value="s"></i><sectionclass="rampchar"value="q"></section><iclass="rampchar"value="-"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="a"></i><iclass="rampchar"value="w"></i><articleclass="rampchar"value="r"></article><iclass="rampchar"value="u"></i><iclass="rampchar"value="i"></i><sectionclass="rampchar"value="i"></section><iclass="rampchar"value="v"></i><articleclass="rampchar"value="t"></article><iclass="rampchar"value="7"></i><articleclass="rampchar"value="j"></article><iclass="rampchar"value="l"></i><iclass="rampchar"value="w"></i><sectionclass="rampchar"value="a"></section><articleclass="rampchar"value="i"></article><iclass="rampchar"value="n"></i><iclass="rampchar"value="h"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="."></i><iclass="rampchar"value="2"></i><sectionclass="rampchar"value="h"></section><iclass="rampchar"value="s"></i><iclass="rampchar"value="v"></i><articleclass="rampchar"value="h"></article><articleclass="rampchar"value="s"></article><iclass="rampchar"value="t"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="h"></i><iclass="rampchar"value="i"></i><iclass="rampchar"value="/"></i><iclass="rampchar"value="5"></i><articleclass="rampchar"value="g"></article><iclass="rampchar"value="."></i><iclass="rampchar"value="7"></i><articleclass="rampchar"value="5"></article><iclass="rampchar"value="-"></i><iclass="rampchar"value="6"></i><articleclass="rampchar"value="q"></article><iclass="rampchar"value="/"></i><iclass="rampchar"value="g"></i><iclass="rampchar"value="l"></i><iclass="rampchar"value="n"></i><sectionclass="rampchar"value="u"></section><iclass="rampchar"value="h"></i><iclass="rampchar"value="q"></i><iclass="rampchar"value="o"></i><sectionclass="rampchar"value="6"></section><sectionclass="rampchar"value=":"></section><iclass="rampchar"value="7"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="/"></i><iclass="rampchar"value="v"></i><iclass="rampchar"value="n"></i><sectionclass="rampchar"value="t"></section><iclass="rampchar"value="-"></i><iclass="rampchar"value="2"></i><iclass="rampchar"value="t"></i><iclass="rampchar"value="a"></i><articleclass="rampchar"value="h"></article><iclass="rampchar"value="6"></i><articleclass="rampchar"value="g"></article><iclass="rampchar"value="d"></i><articleclass="rampchar"value="h"></article><sectionclass="rampchar"value="t"></section><iclass="rampchar"value="r"></i><iclass="rampchar"value="q"></i><iclass="rampchar"value="7"></i><sectionclass="rampchar"value="g"></section><sectionclass="rampchar"value="w"></section><iclass="rampchar"value="5"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="g"></i><iclass="rampchar"value="t"></i><iclass="rampchar"value="v"></i><sectionclass="rampchar"value="w"></section><sectionclass="rampchar"value="b"></section><iclass="rampchar"value="."></i><sectionclass="rampchar"value="3"></section><iclass="rampchar"value="t"></i><iclass="rampchar"value="h"></i><iclass="rampchar"value="0"></i><iclass="rampchar"value="2"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="3"></i><iclass="rampchar"value="i"></i><sectionclass="rampchar"value="3"></section><iclass="rampchar"value="q"></i><sectionclass="rampchar"value="1"></section><iclass="rampchar"value="0"></i><iclass="rampchar"value="2"></i><articleclass="rampchar"value="t"></article><iclass="rampchar"value="t"></i><iclass="rampchar"value="o"></i><iclass="rampchar"value="."></i><sectionclass="rampchar"value="-"></section><iclass="rampchar"value="t"></i><iclass="rampchar"value="5"></i><iclass="rampchar"value="7"></i><iclass="rampchar"value="t"></i><articleclass="rampchar"value="2"></article><sectionclass="rampchar"value="7"></section><iclass="rampchar"value="2"></i><sectionclass="rampchar"value="6"></section><iclass="rampchar"value="p"></i><sectionclass="rampchar"value="s"></section><iclass="rampchar"value="7"></i><iclass="rampchar"value="g"></i><sectionclass="rampchar"value="e"></section><iclass="rampchar"value="a"></i><articleclass="rampchar"value="q"></article><iclass="rampchar"value="6"></i><iclass="rampchar"value="d"></i><iclass="rampchar"value="-"></i><articleclass="rampchar"value="g"></article><iclass="rampchar"value="j"></i><sectionclass="rampchar"value="w"></section><iclass="rampchar"value="a"></i><iclass="rampchar"value="."></i><articleclass="rampchar"value="7"></article><iclass="rampchar"value="v"></i><iclass="rampchar"value="1"></i><sectionclass="rampchar"value="s"></section><iclass="rampchar"value="l"></i><articleclass="rampchar"value="v"></article><iclass="rampchar"value="3"></i><iclass="rampchar"value="b"></i><iclass="rampchar"value="t"></i><sectionclass="rampchar"value="o"></section><iclass="rampchar"value="t"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="g"></i><sectionclass="rampchar"value="w"></section><iclass="rampchar"value="/"></i><articleclass="rampchar"value="-"></article><iclass="rampchar"value="m"></i><articleclass="rampchar"value="t"></article><iclass="rampchar"value="3"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="v"></i><sectionclass="rampchar"value="5"></section><sectionclass="rampchar"value="w"></section><iclass="rampchar"value="n"></i><iclass="rampchar"value="-"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="b"></i><articleclass="rampchar"value="r"></article><iclass="rampchar"value="g"></i><iclass="rampchar"value="d"></i><sectionclass="rampchar"value="a"></section><iclass="rampchar"value="n"></i><articleclass="rampchar"value="/"></article><iclass="rampchar"value="q"></i><iclass="rampchar"value="n"></i><iclass="rampchar"value="h"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="n"></i><articleclass="rampchar"value="2"></article><sectionclass="rampchar"value="l"></section><iclass="rampchar"value="i"></i><iclass="rampchar"value="5"></i><iclass="rampchar"value="p"></i><iclass="rampchar"value="-"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="u"></i><iclass="rampchar"value="w"></i><sectionclass="rampchar"value="o"></section><iclass="rampchar"value="u"></i><iclass="rampchar"value="."></i><articleclass="rampchar"value="1"></article><iclass="rampchar"value="w"></i><iclass="rampchar"value="r"></i><sectionclass="rampchar"value="1"></section><iclass="rampchar"value="t"></i><iclass="rampchar"value="t"></i><articleclass="rampchar"value="2"></article><iclass="rampchar"value="l"></i><iclass="rampchar"value="."></i><articleclass="rampchar"value="l"></article><iclass="rampchar"value="5"></i><iclass="rampchar"value="5"></i><iclass="rampchar"value="."></i><iclass="rampchar"value="s"></i><articleclass="rampchar"value="."></article><iclass="rampchar"value="/"></i><sectionclass="rampchar"value="p"></section><iclass="rampchar"value="u"></i><iclass="rampchar"value="n"></i><articleclass="rampchar"value="l"></article><iclass="rampchar"value="w"></i><iclass="rampchar"value="6"></i><iclass="rampchar"value="v"></i><sectionclass="rampchar"value="t"></section><iclass="rampchar"value="s"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="-"></i><iclass="rampchar"value="e"></i><iclass="rampchar"value="."></i><articleclass="rampchar"value="g"></article><iclass="rampchar"value="a"></i><articleclass="rampchar"value="q"></article><articleclass="rampchar"value="w"></article><iclass="rampchar"value="a"></i><iclass="rampchar"value="s"></i><sectionclass="rampchar"value="s"></section><iclass="rampchar"value="s"></i><iclass="rampchar"value="2"></i><iclass="rampchar"value="t"></i><iclass="rampchar"value="-"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="."></i><sectionclass="rampchar"value="r"></section><iclass="rampchar"value="1"></i><iclass="rampchar"value="e"></i><iclass="rampchar"value="i"></i><iclass="rampchar"value="q"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="s"></i><sectionclass="rampchar"value="t"></section><iclass="rampchar"value="3"></i><sectionclass="rampchar"value="o"></section><iclass="rampchar"value="v"></i><iclass="rampchar"value="."></i><iclass="rampchar"value="l"></i><iclass="rampchar"value="v"></i><iclass="rampchar"value="s"></i><iclass="rampchar"value="p"></i><sectionclass="rampchar"value="l"></section><iclass="rampchar"value="t"></i><iclass="rampchar"value="t"></i><iclass="rampchar"value="o"></i><iclass="rampchar"value="n"></i><iclass="rampchar"value="-"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="t"></i><sectionclass="rampchar"value="r"></section><iclass="rampchar"value="."></i><iclass="rampchar"value="a"></i><iclass="rampchar"value="n"></i><articleclass="rampchar"value="3"></article><iclass="rampchar"value="q"></i><iclass="rampchar"value="h"></i><articleclass="rampchar"value="s"></article><iclass="rampchar"value="h"></i><sectionclass="rampchar"value="b"></section><iclass="rampchar"value="w"></i><articleclass="rampchar"value="t"></article><iclass="rampchar"value="w"></i><iclass="rampchar"value="u"></i><articleclass="rampchar"value="j"></article><iclass="rampchar"value="s"></i><articleclass="rampchar"value="t"></article><articleclass="rampchar"value="t"></article><iclass="rampchar"value="/"></i><iclass="rampchar"value="2"></i><iclass="rampchar"value="o"></i><sectionclass="rampchar"value="e"></section><iclass="rampchar"value="7"></i><sectionclass="rampchar"value="7"></section><iclass="rampchar"value="6"></i><iclass="rampchar"value="3"></i><iclass="rampchar"value="6"></i><articleclass="rampchar"value="3"></article><iclass="rampchar"value="6"></i><iclass="rampchar"value="6"></i><sectionclass="rampchar"value="3"></section><iclass="rampchar"value="7"></i><articleclass="rampchar"value="6"></article><iclass="rampchar"value="3"></i><articleclass="rampchar"value="3"></article><iclass="rampchar"value="6"></i><iclass="rampchar"value="6"></i><iclass="rampchar"value="8"></i><articleclass="rampchar"value="3"></article><iclass="rampchar"value="7"></i>"'

# Using regular expression to extract values of x
x_values = re.findall(r'value="([^"]+)"', tmp)

# Joining x values into a string
result_string = ''.join(x_values)

print(result_string)

import codecs
import string
import sys
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP


ONE_WEEK_IN_SECONDS = 604_800


def generate_secret():
    totp = TOTP(
        key=codecs.encode(string.ascii_letters, encoding="utf-8"),
        length=8,
        algorithm=SHA1(),
        time_step=ONE_WEEK_IN_SECONDS,
        backend=default_backend(),
    )
    seed = int(time.time())
    token = codecs.decode(totp.generate(seed), encoding="utf-8")
    return f"{token}-{seed}"


if __name__ == "__main__":
    sys.stdout.write(
        f"Please head to https://ramp.com/careers and use this secret when "
        f"you apply: {generate_secret()}\n"
    )