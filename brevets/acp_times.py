"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math
#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#
Min = [(1000,13.333), (600,11.428), (400,15), (200,15), (0, 15)]
Max = [(1000,26), (600,28), (400,30), (200,32), (0,34)]
match = {1000:26, 600:28, 400:30, 200:32, 0:34}
VALID_DISTANCES = [1000,600,400,200]

def valid_input(control_dist_km, brevet_dist_km):
    """
    args: it is to know if the control_dist_km is valid
    """
    if control_dist_km > (brevet_dist_km * 1.1):
        return False
    elif control_dist_km < 0:
        return False
    elif brevet_dist_km not in VALID_DISTANCES:
        return False
    else:
        return True


def calculate_time(control_dist_km, brevet_dist_km, brevet_start_time, index):

    time = arrow.get(brevet_start_time, 'YYYY-MM-DD HH:mm')

    if valid_input(control_dist_km, brevet_dist_km) == "False":
        return

    current = control_dist_km
    if index == 0:
        i = 1
        total = 0

        test_o = []

        for element in Max:
            if element[0] > brevet_dist_km:
                continue
            else:
                test = []
                if current > element[0]:
                    test.append(int(element[0]))
                    i += 1

        for n in range(i):
                total += 200 / Max[-n][1]


        final = round(total + (current - test_o[0] / match[test_o[0]]))
        #math.modf(100.12) :  (0.12000000000000455, 100.0)

        hour = math.modf(final[1])
        minn = math.modf(final[0]*60)

        control_time = time.shift(hours =+ hour, minutes =+ minn).isoformat(sep = 'T')
        return control_time

    if index == 1:
            a = 1
            b = 0
            test_c = []
            for element in Min:
                    if element[0] > brevet_dist_km:
                        continue
                    else:
                        test = []
                        if  current > element[0]:
                            test_c.append(int(element[0]))
                            a += 1
            # under 600
            if current <= 600*1.1:
                    b += round((200*a) / 15)
                    hour = math.modf(b[1])
                    minn = math.modf(b[0] * 60)
                    dtime = time.shift(hours =+ hour, minutes =+ minn).isoformat(sep = 'T')
                    return dtime
            #under 1000
            elif current <= 1000*1.1:
                b += round((200*a) / 15 + ((current - 600) / 28))
                hour = math.modf(b[1])
                minn = math.modf(b[0] * 60)
                dtime = time.shift(hours=+ hour, minutes=+ minn).isoformat(sep='T')
                return dtime
            else:
                b += round((200*a) / 15 + (200/11.428) + (current - 600/28))
                # math.modf(100.12) :  (0.12000000000000455, 100.0)
                hour = math.modf(b[1])
                minn = math.modf(b[0] * 60)
                dtime = time.shift(hours=+ hour, minutes=+ minn).isoformat(sep='T')
                return dtime


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    print(calculate_time(control_dist_km, brevet_dist_km, brevet_start_time, 0))


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return calculate_time(control_dist_km, brevet_dist_km, brevet_start_time, 1)
