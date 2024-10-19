import jdatetime

# jdatetime.set_locale(jdatetime.FA_LOCALE)
# now = jdatetime.datetime.now()
# print(now.strftime("%A"))

# =====================================================================================

from persiantools.jdatetime import JalaliDateTime
import pytz

# shamsi = JalaliDateTime(1403, 7, 26, 0, 0, 0, 0, pytz.utc).strftime("%A")
# print(shamsi)

print(JalaliDateTime.now().strftime("%A"))
