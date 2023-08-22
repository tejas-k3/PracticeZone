"""
Implement a prototype service to analysis logs of requests to n
indexed from 1 to n. The logs are given as 2D array log_data of
size m where log_data[i] = [server_id, time] denotes that a
request was served by server with server_id at that time.

Given log_data, an int X and Q queries, for each query[i], find
the number of serveers that did not receive a request in the
time interval [query[i] - x, query[i]].
"""

def getUnrequestedServersCount(n, logData, query, x):
    timeBased = {}
    servers = []
    for val in logData:
        if val[1] not in timeBased:
            timeBased[val[1]] = [val[0]]
        timeBased[val[1]].append(val[0])
    for q in query:
        server = set()
        minTime, maxTime = q - x, q
        for time in timeBased.keys():
            if time >= minTime and time <= maxTime:
                server = server | set(timeBased[time])
        servers.append(n - len(server))
    return servers