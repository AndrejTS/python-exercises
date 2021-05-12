# -*- coding: utf-8 -*-
from datetime import datetime


header_rows = {
    'en_US': '{:11}|{:27}|{:14}'.format('Date', ' Description', ' Change'),
    'nl_NL': '{:11}|{:27}|{:14}'.format('Datum', ' Omschrijving', ' Verandering')
} 


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


create_entry = LedgerEntry


def format_entries(currency, locale, entries):
    table = ''
    entries.sort(key=lambda x: (x.date, x.description, x.change))
    table += header_rows[locale]
    for entry in entries:
        table += '\n'
        table += generate_entry_date(locale, entry)
        if len(entry.description) > 25:
            table += f'{entry.description[:22]}... | '
        else:
            table += f'{entry.description:<25} | '
        table += generate_entry_change(locale, currency, entry)
    return table


def generate_entry_date(locale, entry):
    if locale == 'en_US':
        return f'{entry.date.month:0>2}/{entry.date.day:0>2}/{entry.date.year} | '
    elif locale == 'nl_NL':
        return f'{entry.date.day:0>2}-{entry.date.month:0>2}-{entry.date.year} | '


def generate_entry_change(locale, currency, entry):
    change_currency = abs(int(entry.change / 100.0))
    change_cents = abs(entry.change) % 100
    currency_chunks = []
    while change_currency > 0:
        currency_chunks.insert(0, str(change_currency % 1000))
        change_currency = change_currency // 1000
    if locale == 'en_US':
        thousands_separator = ','
        cent_separator = '.'
        change_str = ''
        if entry.change < 0:
            change_str = '('
        if currency == 'USD':
            change_str += '$'
        elif currency == 'EUR':
            change_str += u'€'
    elif locale == 'nl_NL':
        thousands_separator = '.'
        cent_separator = ','
        if currency == 'USD':
            change_str = '$ '
        elif currency == 'EUR':
            change_str = u'€ '
        if entry.change < 0:
            change_str += '-'
    if len(currency_chunks) == 0:
        change_str += '0'
    else:
        change_str += thousands_separator.join(currency_chunks)
    change_str += cent_separator
    change_str += f'{change_cents:0>2}'
    if locale == 'en_US' and entry.change < 0:
        change_str += ')'
    else:
        change_str += ' '
    return f'{change_str:>13}'

