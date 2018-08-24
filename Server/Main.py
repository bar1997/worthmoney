from Configurations.WebConfigurations import WebConfigurations
from Models.Server import Server


def main():
    Server.start(WebConfigurations.SERVER_PORT)

if '__main__' == __name__:
    main()
