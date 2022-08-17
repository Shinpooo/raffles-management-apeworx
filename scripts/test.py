from ape import accounts, Contract, networks
import click 

# @click.command()
def main():
    print(networks.provider)
    contract = Contract("0x663F0D9C19D912d201DC9aD97F9264e42c35c181")
    print("Hello world!")