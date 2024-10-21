### Simple python api with Flask xD
- Create new `.env` file for basic auth of exporter (/metrics). Example is from `.env.example`
- For grafana dashboard and exporter config: go to folder /dashboard in this repo!
- Moslty this will works if you don't use ingress or api gateway since they all have feature to monitor request xD.
- Recommend to use if you have prometheus and application only, not k8s or other thing xD
- Testing request with wrk, for simulator request 4xx/5xx
`wrk -t12 -c400 -d30s "http://10.0.0.1:31000/bad_request"`
```
Running 30s test @ http://10.0.0.1:31000/bad_request
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   129.24ms  121.05ms   1.88s    68.93%
    Req/Sec    94.08     52.03   333.00     64.33%
  28280 requests in 30.03s, 5.61MB read
  Socket errors: connect 132, read 0, write 0, timeout 9
  Non-2xx or 3xx responses: 28280
Requests/sec:    941.77
Transfer/sec:    191.30KB
```

`wrk -t2 -c400 -d120s "http://10.0.0.1:31000/server_error"`
```
Running 2m test @ http://10.0.0.1:31000/server_error
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   135.07ms  121.09ms   1.98s    56.61%
    Req/Sec   544.70    131.23     0.88k    66.54%
  28459 requests in 2.00m, 5.94MB read
  Socket errors: connect 130, read 0, write 0, timeout 3
  Non-2xx or 3xx responses: 28459
Requests/sec:    237.00
Transfer/sec:     50.69KB
```