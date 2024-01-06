# prefect-quickstart
A small repo to get started with a prefect deployment


This is a simple configuration for a prefect environment with
* 2 flows
* 3 deployments
* a custom worker pool
* scheduling

NOTE: Before running, you need to change the [directory value](https://github.com/Ben-Epstein/prefect-quickstart/blob/main/prefect.yaml#L18) of the `prefect.yaml` file pointing to your working directory. It needs to be _your_ working dir, and the full path to it. If you're currently in the root of this repo (where this readme is), you can run this
```shell
sed -i .bak "s|FULL_PATH_TO_DIR|$PWD|g" prefect.yaml
```
and it will replace it with the current working dir.

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
prefect worker start --pool "default-process-1"
```
