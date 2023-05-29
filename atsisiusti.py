import os
import pdfcrowd
from flask import make_response


def atsisiusti():
    username = 'winipux'
    api_key = os.getenv("api_key")

    client = pdfcrowd.HtmlToPdfClient(username, api_key)
    client.convertUrlToFile('http://localhost:5000', 'page.pdf')

    response = make_response(open('page.pdf', 'rb').read())
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition',
                         'attachment', filename='zygimantasCV.pdf')
    return response
