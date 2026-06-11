from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[Any] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        datapop = self.data.pop(0)
        listpop = (0, datapop)
        return (listpop)


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        cont = 0

        while cont < len(stream):
            item = stream[cont]
            found = False

            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    found = True
                    break

            if not found:
                print(
                    "DataStream error- Can't process element in stream:",
                    item
                )

            cont += 1

    def print_processors_stats(self) -> None:
        for processor in self.processors:
            name = processor.__class__.__name__
            count = len(processor.data)
            print(
                f"{name}: total {count} items processed, remaining {count}"
                "on processor"
            )


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        cont = 0
        if (isinstance(data, str) is True):
            return True
        elif (isinstance(data, list) is True):
            leng = len(data)
            while (cont < leng):
                if (isinstance(data[cont], str) is False):
                    return False
                cont = cont + 1
            return True
        return False

    def ingest(self, data: Any) -> None:
        cont = 0
        leng = len(data)
        if (self.validate(data) is True):
            if (isinstance(data, str) is True):
                self.data.append(str(data))
            else:
                while (cont < leng):
                    self.data.append(str(data[cont]))
                    cont = cont + 1
        else:
            raise Exception("Improper string data")


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for key, value in item.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, dict):
            self.data.append(data)
        else:
            for item in data:
                self.data.append(item)

    def output(self) -> tuple[int, str]:
        item = self.data.pop(0)
        return (0, f"{item['log_level']}: {item['log_message']}")


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        cont = 0
        if (isinstance(data, int) is True or isinstance(data, float) is True):
            return True
        elif (isinstance(data, list) is True):
            leng = len(data)
            while (cont < leng):
                if (
                    isinstance(data[cont], int) is False and
                    isinstance(data[cont], float) is False
                ):
                    return False
                cont = cont + 1
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, (int, float)):
            self.data.append(str(data))
        else:
            cont = 0
            leng = len(data)
            while cont < leng:
                self.data.append(str(data[cont]))
                cont += 1


def main() -> None:
    print("=== Code Nexus- Data Stream ===")
    print()
    print("Initialize Data Stream...")

    ds = DataStream()

    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("No processor found, no data")
    print()

    print("Registering Numeric Processor")
    print()
    np = NumericProcessor()
    ds.register_processor(np)

    print("Send first batch of data on stream:")

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print(stream)

    ds.process_stream(stream)

    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print()
    print("Registering other data processors")

    tp = TextProcessor()
    lp = LogProcessor()

    ds.register_processor(tp)
    ds.register_processor(lp)

    print("Send the same batch again")

    ds.process_stream(stream)

    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print()
    print(
        "Consume some elements from the data processors:"
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        np.output()

    for _ in range(2):
        tp.output()

    for _ in range(1):
        lp.output()

    print("== DataStream statistics ==")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
