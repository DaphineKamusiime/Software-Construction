from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, employee):
        pass
