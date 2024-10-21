### Readme
- Since i didn't find any good dashboard exists for this: https://github.com/pilosus/flask_prometheus_metrics , i have to create new dashboard xD
- What it looks like?
![alt text](image.png)
- How to config job in prometheus?. Label is needed for filter, the name you set is your `serviceName`. label `flask` is just for fixed label that we are know job for flask api with `flask_prometheus_metrics`
```
scrape_configs:
  - job_name: simple-python-flask
    static_configs:
      - targets:
        - '10.0.0.1:31000'
        labels:
          service: flask
          serviceName: simple-python-flask
    basic_auth:
      username: 'user'
      password: 'password'

  - job_name: new-api-flask
    static_configs:
      - targets:
        - '10.0.0.2:32000'
        labels:
          service: flask
          serviceName: new-api-flask
    basic_auth:
      username: 'user'
      password: 'password'
```