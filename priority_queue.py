class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # For max-heap behavior

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        max_task = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify(0)
        return max_task

    def increase_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self._sift_up(i)
                break

    def _heapify(self, i):
        n = len(self.heap)
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.heap[l].priority > self.heap[largest].priority:
            largest = l
        if r < n and self.heap[r].priority > self.heap[largest].priority:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify(largest)

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i].priority > self.heap[parent].priority:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2


# Simulation Test
if __name__ == "__main__":
    print("== Scheduler Simulation ==")
    pq = PriorityQueue()

    # Insert tasks
    pq.insert(Task(1, 10, 0, 5))
    pq.insert(Task(2, 15, 1, 3))
    pq.insert(Task(3, 5, 2, 7))
    print("Inserted Tasks: ", pq.heap)

    # Extract max
    print("Extracted Task: ", pq.extract_max())

    # Increase priority of Task 3
    pq.increase_key(3, 20)
    print("After increasing priority of Task 3: ", pq.heap)

    # Extract max again
    print("Extracted Task: ", pq.extract_max())

    # Remaining Tasks
    print("Remaining Tasks in Queue: ", pq.heap)
