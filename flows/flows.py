from prefect import flow, task, serve


@task()
def do_print(param: str) -> None:
    print("Doing the task")
    print(param)


@flow(log_prints=True)
def run_my_flow(param: str) -> None:
    print("flow 2")
    do_print(param)



@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")

"""
This is if you want to serve these locally and use the local server as your runner
if __name__ == "__main__":
    f1 = hello_world.to_deployment(name="my-first-deployment",
                      tags=["onboarding"],
                      parameters={"goodbye": True},
                      interval=60)

    f2 = run_my_flow.to_deployment(name="print_flow", tags=["param_check"])
    f3 = run_my_flow.to_deployment(name="nikitas_dep", parameters={"param":"nikita"})
    serve(f1, f2, f3, work_pool_name="default-agent-pool")
"""
