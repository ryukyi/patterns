from abc import ABC, abstractmethod

# Strategy Interface
class Strategy(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

# Concrete Strategies
class ConcreteStrategyA(Strategy):
    def execute(self) -> str:
        return "Strategy A execution"

class ConcreteStrategyB(Strategy):
    def execute(self) -> str:
        return "Strategy B execution"

class DefaultStrategy(Strategy):
    def execute(self) -> str:
        return "Default execution"

# Context Class
class Context:
    def __init__(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = DefaultStrategy()

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        result = self.strategy.execute()
        print(result)

if __name__ == "__main__":
    # default
    context = Context()
    context.execute_strategy()

    # A
    context.set_strategy(ConcreteStrategyA())
    context.execute_strategy()

    # B
    context.set_strategy(ConcreteStrategyB())
    context.execute_strategy()
