import secrets
import string
from orders.models import Coupon


def generate_coupon_code(length=10):
    
    #Generate a coupon code that is unique
    alphabet = string.ascii_uppercase + string.digits # A to Z and 0 to 9
    while True:
        #Generate a unique code
        code = ''.join(secrets.choice(alphabet) for _ in range(length)) #e.g. XYZ1B2E65F
        #Check exits in DB or not
        if not Coupon.objects.filter(code=code).exists():
            return code
