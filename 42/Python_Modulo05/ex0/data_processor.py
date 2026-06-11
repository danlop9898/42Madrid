from typing import Any
from abc import ABC, abstractmethod

'''
DataProcessor (abstracta)
│
├── validate()  ABSTRACT
├── ingest()    ABSTRACT
└── output()    NORMAL
     ↑
     ↑ heredado
     ↑
├── NumericProcessor
├── TextProcessor
└── LogProcessor
'''


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
        cont = 0
        leng = len(data)
        if (self.validate(data) is True):
            if (
                isinstance(data, int) is True or
                isinstance(data, float) is True
            ):
                self.data.append(str(data))
            else:
                while (cont < leng):
                    self.data.append(str(data[cont]))
                    cont = cont + 1
        else:
            raise Exception("Improper numeric data")


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


def main() -> None:
    print("=== Code Nexus- Data Processor ===")
    print()
    print("Testing Numeric Processor...")

    np = NumericProcessor()

    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for i in range(3):
        idx, val = np.output()
        print(f"Numeric value {idx}: {val}")

    print()

    print("Testing Text Processor...")

    tp = TextProcessor()

    print(f"Trying to validate input '42': {tp.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    idx, val = tp.output()
    print(f"Text value {idx}: {val}")

    print()
    print("Testing Log Processor...")

    lp = LogProcessor()

    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]

    print(f"Processing data: {logs}")
    lp.ingest(logs)

    print("Extracting 2 values...")
    for i in range(2):
        idx, val = lp.output()
        clean = val.replace("{", "").replace("}", "").replace("'", "")
        parts = clean.split(", ")
        msg = parts[0].split(": ")[1]
        print(f"Log entry {i}: {msg}")


if __name__ == "__main__":
    main()
