import sys
from configparser import ConfigParser

import argparse


def cli():
    """
    Permet de prendre les entrés de l'utilisateur sur le terminal.
    :return: un dictionnaire avec les entrés utilisateur
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-ls', '-ls-tree', help='The path of the directory or file whose size you want to calculate ', type=str)
    parser.add_argument('-hr', '--human-readle', help='a more readable output of the size (adapt to the size instead of always showing bytes)', type=str)
    args = parser.parse_args()

    dict = {
        "path": "",
        "readable": False,
    }
    if args.ls:
        dict["path"] = args.ls
    if args.human_readle == "true":
        dict["readable"] = True

    return dict


def read(file):
    """
    Permet de lire le ficher de config et de sortir les config requises
    :param file: file of config
    :return: all the config needed
    """
    commands = {}
    with open(file, 'r') as f:
        line = f.readline()
        for line in line:
            line = f.readline()
            line = line.split()
            if len(line) > 2:
                if line[0] == "input":
                    commands["input"] = line[2]
                elif line[0] == "output":
                    commands["output"] = line[2]
                elif line[0] == "content":
                    commands["filter"] = line[2]
                elif line[0] == "log_file":
                    commands["log_file"] = line[2]
    return commands


def conf(file):
    conf = {}
    config = ConfigParser()
    config.read(file)

    input_dir = config.get('general', 'input')
    conf["input"] = input_dir
    output_dir = config.get('general', 'output')
    conf["output"] = output_dir
    filtersss = config.get('filter', 'content')
    conf["filter"] = filtersss
    log_file = config.get('general', 'log_file')
    conf["log_file"] = log_file
    return (conf)
