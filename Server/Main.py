from Configurations.WebConfigurations import WebConfigurations
from Models.Server import Server
from Models.APIs.Hever import Hever
from Models.APIs.Isracard import Isracard

def main():
    # Server.start(WebConfigurations.SERVER_PORT)
    Isracard.test()

if '__main__' == __name__:
    main()
