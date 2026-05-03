import heapq
from typing import Optional, Tuple, List

class TriageSystem:
    _arrival_counter: int = 0

    def __init__(self) -> None:
        self._heap: List[Tuple[int, int, str, int]] = []

    @classmethod
    def NextArrivalOrder(cls) -> int:
        current = cls._arrival_counter
        cls._arrival_counter += 1
        return current

    def AddPatient(self, name: str, severity: int) -> None:
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a nonempty string")
        if not isinstance(severity, int) or not (1 <= severity <= 5):
            raise ValueError("severity must be an integer between 1 and 5")
        arrival = self.NextArrivalOrder()
        entry = (-severity, arrival, name, severity)
        heapq.heappush(self._heap, entry)

    def ProcessNext(self) -> Optional[Tuple[str, int]]:
        if not self._heap:
            return None
        _, _, name, severity = heapq.heappop(self._heap)
        return (name, severity)

    def PeekNext(self) -> Optional[Tuple[str, int]]:
        if not self._heap:
            return None
        _, _, name, severity = self._heap[0]
        return (name, severity)

    def IsEmpty(self) -> bool:
        return len(self._heap) == 0

    def Size(self) -> int:
        return len(self._heap)

    def Clear(self) -> None:
        self._heap.clear()
