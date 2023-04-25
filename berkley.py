from datetime import datetime, timedelta

def berkley(server_time, client1_time, client2_time):

    fmt = "%M:%S"
    server_dt = datetime.strptime(server_time, fmt)
    client1_dt = datetime.strptime(client1_time, fmt)
    client2_dt = datetime.strptime(client2_time, fmt)

    st1 = client1_dt - server_dt
    st2 = client2_dt - server_dt
    print(f"Difference in client1 and server: {st1.total_seconds()}")
    print(f"Difference in client2 and server: {st2.total_seconds()}")

    aveg = (st1+st2)/2

    adj_server = server_dt + aveg
    adj_c1 = client1_dt - st1 + aveg
    adj_c2 = client2_dt - st2 + aveg

    print(f"Adjusted time of server: {adj_server.strftime(fmt)}")
    print(f"Adjusted time of client 1: {adj_c1.strftime(fmt)}")
    print(f"Adjusted time of client 2: {adj_c2.strftime(fmt)}")



berkley("03:00" , "02:30", "03:30")