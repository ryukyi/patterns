from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass 


class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Using quicksort")
        # implement quicksort
        return sorted(data)
    
class MergeSort(SortingStrategy):
    def sort(self, data):
        print("Using mergesort")
        # implement merge sort
        return sorted(data)
    

class Context:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)
    
if __name__ == "__main__":
    # Data
    data_small = list(range(1000, 0, -1))
    data_large = list(range(10000, 0, -1))

    context = Context(QuickSort() if len(data_small) < 5000 else MergeSort())
    print(context.sort_data(data_small))  # QuickSort for smaller data set

    context.set_strategy(QuickSort() if len(data_large) < 5000 else MergeSort())
    print(context.sort_data(data_large))  # MergeSort for larger data set