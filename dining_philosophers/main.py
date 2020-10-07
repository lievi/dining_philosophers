import logging
from dining_philosophers.table import Table

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(message)s'
)


def main():
    dinning_table = Table()
    dinning_table.start_dinning()


if __name__ == "__main__":
    main()
