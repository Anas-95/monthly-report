from datetime import timedelta, date, datetime

def query_time():
    day = date.today() - timedelta(days=1)
    Start_day = datetime.combine(day, datetime.min.time())
    delta1 = timedelta(hours=5, minutes=59)
    delta2 = timedelta(hours=6)

    times = []
    st = Start_day
    for i in range(0,4):
        ed = st + delta1
        tup = (st.strftime("%Y-%m-%d %H:%M"), ed.strftime("%Y-%m-%d %H:%M"))
        times.append(tup)
        st = st + delta2
    # print(times)
    # exit()
    return times

print(query_time())