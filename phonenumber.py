import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata

phone_number = phonenumbers.parse("+917507710009")

print(geocoder.description_for_number(phone_number, 'en'))
print(carrier.name_for_valid_number(phone_number, 'en'))
print(phonemetadata.NumberFormat(phone_number, 'en'))