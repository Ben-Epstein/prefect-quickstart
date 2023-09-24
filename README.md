# prefect-quickstart
A small repo to get started with a prefect deployment


This is a simple configuration for a prefect environment with
* 2 flows
* 3 deployments
* a custom worker pool
* scheduling

NOTE: Before running, you need to change the value of the `prefect.yaml` file pointing to your working directory. It needs to be _your_ working dir, and the full path to it

To run this, first set your API key and authenticate, then create the work-pool
```
prefect work-pool create 'default-process-1' --type process
```

then
```
prefect deploy --all
```

Then, in some remote environment, set your api key, authenticate, and run
```
prefect agent start --pool "default-process-1"
```


## Notes about work-pools, workers, and agents

There are 2 "local running" work-pools: `process` and `prefect-agent`. As far as I can tell, if you are executing them on a machine, they behave the same. 

The `worker` and `agent` seem to also be the same in this regard, with the one exception that an `agent` can connect to both `process` and `prefect-agent` worker-pools, whereas a `worker` can only connect to `process` worker-pools.


```shell
# Example 1
prefect work-pool create default-process-1 --type process

# Either works
# prefect agent start --pool default-process-1
# prefect worker start --pool default-process-1
```


```shell
# Example 2
prefect work-pool create default-process-2 --type prefect-agent

# prefect agent start --pool default-process-2   # works
# prefect worker start --pool default-process-2  # fails
```
