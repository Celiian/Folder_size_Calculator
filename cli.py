import sys
from fonctions import functions
from configparser import ConfigParser
import gif

import argparse


def cli():
    """
    Permet de prendre les entrés de l'utilisateur sur le terminal.
    :return: un dictionnaire avec les entrés utilisateur
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--filters', help='filter that you want to apply', type=str)
    parser.add_argument('-i', '--input-dir', help='path to the input directory where the originals images are stocked',
                        type=str)
    args = parser.parse_args()

    dict = {
        "filter": "",
        "input": "",

    }

    if args.config_file:
        dict = conf(args.config_file)
    if args.filters:
        dict["filter"] = args.filters
    if args.input_dir:
        dict["input"] = args.input_dir
    if args.output_dir:
        dict["output"] = args.output_dir
    if args.list_filters:
        functions.list_filters()
        exit(0)
    if args.log_file:
        dict["lof_file"] = args.log_file

    if args.vid_input:
        dict["vid_input"] = args.vid_input
        if args.vid_output:
            dict["vid_output"] = args.vid_output
        gif.vid_img(dict["vid_input"], dict["vid_output"])

    if args.gif_input:
        dict["gif_input"] = args.gif_input
        if args.gif_name:
            dict["gif_name"] = args.gif_name
        gif.gif(dict["gif_input"], dict["gif_name"])

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
