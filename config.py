import os
import yaml

try:
    with open("local.yaml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
except FileNotFoundError:
    with open("config.yaml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
