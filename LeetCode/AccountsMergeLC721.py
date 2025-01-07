"""Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is
a name, and the rest of the elements are emails representing emails of the account.Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two
accounts have the same name, they may belong to different people as people could have the same name. A person can have
any number of accounts initially, but all of their accounts definitely have the same name.After merging the accounts,
return the accounts in the following format: the first element of each account is the name, and the rest of the elements
are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]

Output: [
    ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]

Explanation:The first and second John's are the same person as they have the common email "johnsmith@mail.com".The third
John and Mary are different people as none of their email addresses are used by other accounts.We could return these lists
in any order, for example the answer
[
    ['Mary', 'mary@mail.com'],
    ['John', 'johnnybravo@mail.com'],
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
]
would still be accepted."""
from typing import List
from collections import defaultdict

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    result = []
    adj_list = defaultdict(list)
    visited = set()

    def dfs(account, email):
        nonlocal visited
        visited.add(email)
        account.append(email)

        for e in adj_list[email]:
            if e not in visited:
                dfs(account, e)

    for account in accounts:
        emails = account[1:]

        for i in range(len(emails)):
            for j in range(i, len(emails)):
                if emails[i] not in adj_list[emails[j]]:
                    adj_list[emails[j]].append(emails[i])
                if emails[j] not in adj_list[emails[i]]:
                    adj_list[emails[i]].append(emails[j])

    for account in accounts:
        accountName = account[0]
        accountFirstEmail = account[1]

        if (accountFirstEmail not in visited):
            mergedAccount = []
            dfs(mergedAccount, accountFirstEmail)

            mergedAccount.sort()
            mergedAccount.insert(0, accountName)
            result.append(mergedAccount)

    return result