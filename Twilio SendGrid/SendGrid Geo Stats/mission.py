import sendgrid
import json

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(API_KEY)


def best_country(str_date: str):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })
    return max(json.loads(response.body)[0]['stats'],
               key=lambda a: a['metrics']['unique_clicks'])["name"]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print('Check your results')
