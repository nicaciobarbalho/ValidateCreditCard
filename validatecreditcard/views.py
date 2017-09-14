
from pyramid.view import view_config

from validatecreditcard.controller.card import Card


@view_config(route_name='home', renderer='templates/validcard.jinja2')
def my_view(request):
    return {'project': 'ValidateCreditCard'}

@view_config(route_name='card_valid', renderer='templates/validcard.jinja2')
def card_valid_view(request):
    number = request.params["number"]
    card = Card()
    message = 'Invalid Card'
    result = card.valid(number)
    if result:
        message = 'Valid Card'
    return {'message':message}
