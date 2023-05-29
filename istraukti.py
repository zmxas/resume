import requests
from bs4 import BeautifulSoup
import os


def cv():
    link = 'https://www.cvbankas.lt/login.php'

    with requests.Session() as s:
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        res = s.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        payload = {i['name']: i.get('value', '')
                   for i in soup.select('input[name]')}
        payload['uname'] = 'zygimantas@mozuraitis.lt'
        payload['pass'] = os.getenv('payload_pass')

        s.post(link, data=payload)

        r = s.get('https://www.cvbankas.lt/perziureti-mano-cv-863096716.html')
        soup = BeautifulSoup(r.text, 'html.parser')

        try:
            pareigos = soup.find('h3', class_='heading3').text.strip()
            imone_div = soup.find('div', class_='cv_subsection_inner')
            imone_spans = imone_div.find_all('span', class_='cv_organization')
            imone = ' '.join([span.text.strip() for span in imone_spans])
            trukme = soup.find(
                'div', class_='cv_subsection_label cv_subsection_label_durations').text.strip()

            return pareigos, imone, trukme
        except AttributeError:
            return None
