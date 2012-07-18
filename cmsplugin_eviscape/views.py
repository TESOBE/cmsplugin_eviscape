import urllib2
import json


def get_sent_evis(server, nod_id, limit, evis_type):
    """(Currently) returns a list of dictionaries with keys evis, ref and id.
    Returns an empty list in case it could not fetch the data from eviscape."""

    json_url = "http://%s/api/1.0/rest/?method=evis.sent&format=json&jsoncallback=?&nod_id=%s&per_page=%s" % (server, nod_id, limit)

    # quick and dirty
    try:
        socket_file_obj = urllib2.urlopen(json_url)
    # for the case we cannot get access to eviscape data
    except urllib2.URLError, e:
        print e
        print 'ERROR in get_sent_evis'
        return []

    data = socket_file_obj.read()
    # strip parentheses because jsoncallback=?, otherwise there would be a jsonEviscapeApi(...)
    data = data.strip('()')
    data = json.loads(data)

    sent_evis = [e for e in data['objects'] if e['evis']['typ_value'] == evis_type]
    print sent_evis
    return sent_evis
