import argparse

from dirk.commands.decorators import subcommand
from dirk.config import Config


def exec(conf: Config, args: argparse.Namespace):
    for stage in conf.stages:
        print(stage.name)


@subcommand(exec=exec)
def add_subcommand(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    parser = subparsers.add_parser(name="stages")
    return parser
