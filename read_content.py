#! usr/bin/python3
import re

currencies = { 'Roman': 
                { 
                    'I': 1, 
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                } 
            }

trade_info = 'ThoughtWorks.txt'
visited_merchants = {}

class RomanNumeralAlgothrim:
    def roman_numeral_algothrim (self):
        
        cant_be_opertor = ('V', 'L', 'D')
        subtract_rules = { 'C': {'D', 'M'}, 'I': {'V', 'X'}, 'X': {'L', 'C'} }
        can_be_repeated = ('I', 'X', 'C', 'M')
        
        if (self < self):
            return self
        
        return '1'

class ReadFile:
    def read_file (self, trade_info):
        planet_name = trade_info.split('.')
        visited_merchants.update({planet_name[0]: {}})
        
        with open(trade_info, 'r') as f:
            for line in f:
                if (line):
                    lines = line.split(' ')
        f.closed

def get_currency (self):
    if ( lines[1] == 'is' ):
        for numeral, cur in currencies['Roman'].items():
            if ( numeral == lines[2].rstrip() ):
                visited_merchants.update({planet_name[0]: {lines[0]: cur}})
    return visited_merchants
    
def get_questions (trade_info):
    if ( lines[-1].rstrip() == '?' and re.search('is', str(lines))):
        visited_merchants.update({planet_name[0]: { 'Questions': lines } })
    return visited_merchants

def add_new_trade_info (visited_merchants):
    for planet, currency in visited_merchants.items():
        if (visited_merchants):
            currencies.update({planet: currency})
    return currencies

def answer_questions (visited_merchants):
    return '1'