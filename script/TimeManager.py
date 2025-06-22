from datetime import datetime, timedelta


NOTIFICATION_INTERVAL = timedelta(minutes=30)

NIGHT_START = 21
NIGHT_END = 10

last_notification_time = None


def get_time_of_day():
    hour = datetime.now().hour

    if 6 <= hour < 9:
        return 'dawn'
    elif 9 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 18:
        return 'day'
    elif 18 <= hour < 21:
        return 'twilight'
    elif 21 <= hour or hour < 3:
        return 'night'
    else:
        return 'predawn'


def is_night():
    now = datetime.now().hour
    return now >= NIGHT_START or now < NIGHT_END


def should_notify():
    global last_notification_time

    now = datetime.now()

    if is_night():
        return False

    notify = False

    if last_notification_time is None:
        notify = True
    elif now - last_notification_time >= NOTIFICATION_INTERVAL:
        notify = True

    if notify:
        last_notification_time = now

    return notify