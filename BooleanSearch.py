#!/usr/bin/python3

import re, os

class BooleanSearch():

    def __init__(self, wordList = False, query = False):
        self.wordList = wordList
        self.query = query


    # Convert the query string into a list of individual elements
    def createQueryToEval(self):
        query = re.sub(r'\(', ' ( ', self.query)
        query = re.sub(r'\)', ' ) ', query)
        return query.split()


    # Create a boolean query for evaluation based on the provided word list and query string
    def creatBoolQuery(self):
        querySplited = self.createQueryToEval()
        print(querySplited)
        newQuery = ""
        exist = []

        for item in querySplited:
            if item not in ['et', 'ou'] and (item in self.wordList or item[3:] in self.wordList):
                exist.append(item[3:]) if item.startswith('non') else exist.append(item)

        for item in querySplited:
            if item in set(exist) or item[3:] in set(exist):
                if item.startswith('non'):
                    decision = " 0 "
                else:
                    decision = " 1 "
                newQuery += decision
            elif item == '(':
                newQuery += ' ( '
            elif item == ')':
                newQuery += ' ) '
            elif item == 'et':
                newQuery += ' and '
            elif item == 'ou':
                newQuery += ' or '
            else:
                newQuery += " 0 "
        print(newQuery)
        return newQuery