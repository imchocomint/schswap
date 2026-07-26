import argparse
from get_opt import listsch, showlist
from reload_scx import reload_scx, showstatus
def list_schedulers():
    listsch()
    showlist()
def switch(scheduler):
    reload_scx(scheduler)
    showstatus()

if __name__ == "__main__":
    print('Please remove "scx_" from the scheduler name when switching.')
    parser = argparse.ArgumentParser(description="schswap")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the "list" command
    list_parser = subparsers.add_parser("list", help="List available schedulers")

    # Subparser for the "switch" command
    switch_parser = subparsers.add_parser("switch", help="Switch to the specified scheduler")
    switch_parser.add_argument("scheduler", type=str, help="The scheduler to switch to")

    args = parser.parse_args()

    if args.command == "list":
        list_schedulers()
    elif args.command == "switch":
        switch(args.scheduler)
    else:
        parser.print_help()