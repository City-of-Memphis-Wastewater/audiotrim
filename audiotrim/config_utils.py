import toml
def load_defaults(config_file):
    return toml.load(config_file)['audio']