from abc import ABC, abstractmethod

#Implement Report Generation Class:

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, employee):
        pass
