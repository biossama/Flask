import requests
url = 'http://127.0.0.1:5000/'

data = {
    'duedate': 'September 1, 2022',
    'from_addr': {
        'addr1': 'Pochet, France',
        'addr2': 'Clermont 63000',
        'company_name': 'Ab Tech'
    },
    'invoice_number': 200,
    'items': [{
            'charge': 500.0,
            'title': 'App Development'
        },
        {
            'charge': 85.0,
            'title': 'Hosting (6 months)'
        },
        {
            'charge':10.0,
            'title': 'Domain name (1 year)'
        }
    ],
    'to_addr': {
        'company_name': 'Tech-bio',
        'person_email': 'my_mail@example.com',
        'person_name': 'kindy jhon'
    }
}
html = requests.post(url, json=data)
with open('invoice.pdf', 'wb') as f:
    f.write(html.content)
