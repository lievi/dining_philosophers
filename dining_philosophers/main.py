import logging
from dining_philosophers.table import Table

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(message)s'
)


def main():
    dining_table = Table()
    dining_table.start_dining()


def init():
    if __name__ == "__main__":
        main()
