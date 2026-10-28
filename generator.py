import datetime
import time
import uuid

rnd_str = str(uuid.uuid4())

while True:
    now = datetime.datetime.now()
    result = f"{now.date()}T{now.strftime('%H:%M:%S')}.{now.microsecond // 1000:03d}Z: {rnd_str}"
    print(result)
    time.sleep(5)