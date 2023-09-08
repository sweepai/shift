from abc import ABC, abstractmethod


class LauncherInterface(ABC):

    @abstractmethod
    def start(self, port: int) -> None:
        pass

    @abstractmethod
    def kill(self, port: int) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass
