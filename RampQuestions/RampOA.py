import collections
# We want to query an API endpoint to receive data about currently available apartment listings from a rental website. Among the data fields is a column called num_bedrooms, which takes the value of 1 for a "1-bedroom" apartment and 0 for a "studio".
# Note: This rental agency only works with studios and 1-bedroom apartments, so there will never be 2+ bedroom listings. Each listing includes information about a "studio" or a "1-bedroom" apartment, so there will never be a listing with both a "studio" and "1-bedroom" offerings in one posting.
# The algorithm used occasionally mistags the num_bedrooms value. Specifically, sometimes a "studio" is tagged as having num_bedrooms = 1 or a "1-bedroom" is tagged as num_bedrooms = 0. Further investigation revealed it to be an issue with one of the data fields, description, and the way our algorithm parsed the field to extract a num_bedrooms value.
# For example: "description": "Beautiful 1-bedroom apartment with nearby yoga studio." was detected as a yoga studio instead of 1-bedroom and incorrectly had num_bedrooms = 0.
# Your task is to write a function that takes in the jsonData and corrects this problem. The GET request retrieves the data as a string which looks like this:
#
# jsonData = [
#    {
#       "id": "3",
#       "agent": "Ton Jett",
#       "unit": "#12",
#       "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
#       "num_bedrooms": 1
#    },
#    ...
# ]
# While correcting the problem, remember the following edge cases:
#
# If the word "studio" or "1-bedroom" is preceded immediately by any of the words: "yoga", "dance" or "art", don't consider it for num_bedrooms value.
# If the description does not contain the word "studio" or "1-bedroom", do not change the value for num_bedrooms.
# The rules above should be applied regardless of punctuation or letter casing within the description field.
# Your end goal is to return an array of integers representing num_bedrooms for each rental listing, example: [0, 1, 1, 1, 0, 0].

# Example:
jsonData = '''[
   {
      "id": "1",
      "agent": "Radulf Katlego",
      "unit": "#3",
      "description": "This luxurious studio apartment is in the heart of downtown.",
      "num_bedrooms": 1
   },
   {
      "id": "2",
      "agent": "Kelemen Konrad",
      "unit": "#36",
      "description": "We have a 1-bedroom available on the third floor.",
      "num_bedrooms": 1
   },
   {
      "id": "3",
      "agent": "Ton Jett",
      "unit": "#12",
      "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
      "num_bedrooms": 1
   },
   {
      "id": "4",
      "agent": "Fishel Salman",
      "unit": "#13",
      "description": "Beautiful studio with a nearby art studio.",
      "num_bedrooms": 1
   }
]'''
answer = [0, 1, 1, 0]

import json


def solution(jsonData):
    result = []

    myJson = json.loads(jsonData)
    bedRoomExcp = set(["yoga 1-bedroom", "dance 1-bedroom", "art 1-bedroom"])
    studioExcp = set(["yoga studio", "dance studio", "art studio"])

    for element in myJson:
        description = element["description"].lower()
        numBedrooms = element["num_bedrooms"]
        ignoreStudio = False
        ignoreBedRoom = False

        for exception in bedRoomExcp:
            if exception in description:
                ignoreBedRoom = True
        if exception in studioExcp:
            if exception in description:
                ignoreStudio = True

        if "studio" not in description or "1-bedroom" not in description:
            if not ignoreStudio and "studio" in description:
                result.append(0)
            elif not ignoreBedRoom and "1-bedroom" in description:
                result.append(1)
        else:
            result.append(numBedrooms)

    return result

assert solution(jsonData) == answer