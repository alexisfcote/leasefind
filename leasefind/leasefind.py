# -*- coding: utf-8 -*-

import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import re


class AutoListing(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_listing(self):
        raise NotImplementedError


class LeaseBuster(AutoListing):
    URL = 'https://leasebusters.com/fr/default.asp'

    def __init__(self):
        super().__init__()

    def get_listing(self):
        headers = {
            'authority': 'leasebusters.com',
            'cache-control': 'max-age=0',
            'origin': 'https://leasebusters.com',
            'upgrade-insecure-requests': '1',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'referer':
            'https://leasebusters.com/fr/Search-for-a-lease-take-over-vehicle.asp',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
        }

        data = {
            'Category': 'smallsportutes',
            'ID': '',
            'view': 'Faster',
            'Territory': 'Quebec',
            'Submit.x': '100',
            'Submit.y': '10',
            'leftside': 'false'
        }

        response = requests.post(
            'https://leasebusters.com/fr/lease-take-over-vehicle-gallery-results.asp',
            headers=headers,
            data=data)


        soup =  BeautifulSoup(response.content,
                             'html.parser',
                             from_encoding="ISO-8859-1")

        lines = []
        for td in soup.find_all('td'):
            text = td.text
            if len(text)< 200:
                lines.append(text.strip())

        for line in lines[:]:
            if re.match("\d{4}", line):
                break
            else:
                lines.remove(line)

        re.findall(r"(\d{4})\|(\D*)\|(\D*)\|(\d*)\|(\d*)\|", '|'.join(lines))
        return lines

if __name__ == "__main__":
    lb = LeaseBuster()
    lb.get_listing()