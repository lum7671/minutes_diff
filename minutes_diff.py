import sys
from datetime import datetime


if len(sys.argv) != 2:
    print(f"{sys.argv[0]} hours[:minutes]")
    sys.exit(0)

st = sys.argv[1].split(":")

now = datetime.today()
period = now.replace(hour=int(st[0]), minute=len(st) > 1 and int(st[1]) or 0)

minutes_diff = (period - now).total_seconds() / 60.0
print(int(minutes_diff))
