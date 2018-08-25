from Configurations.WebConfigurations import WebConfigurations
from Models.Server import Server
from Models.APIs.Hever import Hever


def main():
    # Server.start(WebConfigurations.SERVER_PORT)
    Hever.test()

if '__main__' == __name__:
    main()
