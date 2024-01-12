from request import get_tide, format_tide
from send_sms import send_sms
# from request import

# get tide
tide, begin, end = get_tide(interval=20)

msg = format_tide(tide, begin)

# send sms
send_sms('+18445420578', '+18777804236', msg)
