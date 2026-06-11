from typing import Any
from typing import Protocol, List, Tuple
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:

        values = []

        for item in data:
            values.append(str(item))

        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        values = []

        for item in data:
            values.append(str(item))

        print("{" + ", ".join(values) + "}")


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        datapop = self.data.pop(0)
        self.total_processed += 1
        return (0, str(datapop))


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
            total = processor.total_processed

            print(
                f"{name}: total {total} items processed,"
                "remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        for processor in self.processors:

            batch = []

            for _ in range(nb):
                if not processor.data:
                    break

                batch.append(processor.data.pop(0))  # 👈 IMPORTANTE

            if batch:
                plugin.process_output(batch)


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
        if not self.validate(data):
            raise Exception("Improper string data")

        if isinstance(data, str):
            self.data.append(data)
            self.total_processed += 1
        else:
            for x in data:
                self.data.append(x)
                self.total_processed += 1


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
            self.total_processed += 1
        else:
            for x in data:
                self.data.append(x)
                self.total_processed += 1

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
                    not isinstance(data[cont], int) and
                    not isinstance(data[cont], float)
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
            self.total_processed += 1
        else:
            for x in data:
                self.data.append(str(x))
                self.total_processed += 1


def main() -> None:
    print("=== Code Nexus- Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()

    ds = DataStream()

    print("== DataStream statistics ==")
    print("No processor found, no data")
    print()
    print("Registering Processors")
    print()

    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()

    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)

    # ---------------- FIRST BATCH ----------------
    stream1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING", "log_message":
                "Telnet access! Use ssh instead"
            },
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch of data on stream:", stream1)

    ds.process_stream(stream1)

    print()
    print("== DataStream statistics ==")
    print()
    ds.print_processors_stats()

    csv_plugin = CSVExportPlugin()

    print("Send 3 processed data from each processor to a CSV plugin:")

    ds.output_pipeline(3, csv_plugin)

    print()
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    stream2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE", "log_message":
                "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("Send another batch of data:", stream2)

    ds.process_stream(stream2)

    print()
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    json_plugin = JSONExportPlugin()

    print("Send 5 processed data from each processor to a JSON plugin:")

    ds.output_pipeline(5, json_plugin)

    print()
    print("== DataStream statistics ==")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
