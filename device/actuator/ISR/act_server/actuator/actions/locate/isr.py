import math
import random

from datetime import datetime, timezone


def randCoord(cLat=38.889484, cLong=-77.035278, radius=10000):
    """
    Generate a random lat/long within a radius of a central location
    :param cLat: central points latitude, in degrees
    :param cLong: central points longitude, in degrees
    :param radius: radius to generate points, in degrees
    :return: tuple - lat, long
    """
    rad = radius/111300

    rand_1 = float(random.uniform(0.0, 1.0))
    rand_2 = float(random.uniform(0.0, 1.0))

    w = rad * math.sqrt(rand_1)
    t = 2 * math.pi * rand_2

    deltaLat = w * math.cos(t)
    deltaLong = w * math.sin(t)

    return f'{deltaLat+cLat:.6f}', f'{deltaLong+cLong:.6f}'


def isr(self, cmd_id=0, target={}, *extra_args, **extra_kwargs):
    if len(target) != 1:
        return self._action_exception(cmd_id, 'query', except_msg='Invalid target type for action')

    lat, long = randCoord()

    results = dict(
        time_of_arrival=f'{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%S%z}',
        position=dict(
            latitude=lat,
            longitude=long
        )
    )

    if 'signal' in target:
        freq = target['signal'].get('frequency', None)
        band = target['signal'].get('band', None)
        lower_freq_band = target['signal'].get('lower_freq_band', None)
        upper_freq_band = target['signal'].get('upper_freq_band', None)

    elif 'generic' in target:
        uav_id = target['generic'].get('uav_id', None)
        actuator_id = target['generic'].get('actuator_id', None)

    else:
        return self._bad_request(cmd_id)

    return dict(
        id=cmd_id,
        status=200,
        status_text='Ok, The request has succeeded',
        results={
            'isr:Results': results
        }
    )