from esports.models import Match
#from scheduler.config_stuff import config


def get_match_json():
    return {'data': 'hey there'}

def update_match():
    json = get_match_json()
    m = Match(data=json['data'])

    m.save()

    print('a match saved')
