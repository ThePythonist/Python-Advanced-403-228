# import datetime

# now = str(datetime.datetime.now())
#
# print(now.split())
# print(now.split()[1])

# ---------------------------------------

# import time
#
# c = 0
# while c <= 20:
#     time.sleep(1)
#     c += 1
#     print(str(datetime.datetime.now()))

# ---------------------------------------

# import datetime

# Attributes

# year = datetime.datetime.now().year
# month = datetime.datetime.now().month
# minute = datetime.datetime.now().minute
# day = datetime.datetime.now().day
# hour = datetime.datetime.now().hour
# second = datetime.datetime.now().second
#
# print(f"{hour}:{minute}")

# ---------------- STRFTIME EXAMPLES ----------------

import datetime

now = datetime.datetime.now()
print(now.strftime("%d"))
