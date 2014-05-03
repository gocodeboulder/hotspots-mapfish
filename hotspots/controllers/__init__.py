"""
from pylons.events import Subscriber, newResponse

@Subscriber(NewResponse)
def add_access_list(event):
    event.response.headerlist.append("Access-Control-Allow-Origin", "*")

"""
