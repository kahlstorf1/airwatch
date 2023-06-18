import requests

years = range(2000, 2024)

for year in years:
    url = f'https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_{year}.zip'
    response = requests.get(url, allow_redirects=True)

    with open(f'rawData/{year}_data.csv', 'wb') as file:
        file.write(response.content)
