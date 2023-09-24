# prefect-quickstart
A small repo to get started with a prefect deployment


This is a simple configuration for a prefect environment with
* 2 flows
* 3 deployments
* a custom worker pool
* scheduling


To run this, first set your API key and authenticate, then run
```
prefect deploy --all
```

Then, in some remote environment, set your api key, authenticate, and run
```
prefect agent start --pool "default-process-1"
```
