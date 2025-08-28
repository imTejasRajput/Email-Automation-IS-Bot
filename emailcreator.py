from templates import *
from models import create_response
def basic_email_creator(name,magazine_title,edition_title,price):
    return BASIC_TEMPLATE.format(name=name,magazine_title=magazine_title,edition_title=edition_title,price=price)

def ai_email_creator(name,magazine_title,edition_title,price,about,experience=None):
    personlised_response=create_response(about,experience)
    return AI_TEMPLATE.format(name=name,magazine_title=magazine_title,edition_title=edition_title,price=price,personlised_response=personlised_response)

def test_email_creator():
    return TEST_TEMPLATE


def basic_email_creator_2(name,magazine_title,edition_title):
    return BASIC_TEMPLATE_2
