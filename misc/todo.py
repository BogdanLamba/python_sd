from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    name: str
    due_date: datetime
    priority: int


def _get_priority_text(priority: int) -> str:
    """Convert numeric priority to a descriptive text."""
    priority_map = {
        0: "🔴 High",
        1: "🟡 Medium",
        2: "🟢 Low"
    }
    return priority_map.get(priority, f"Priority {priority}")


@dataclass
class Todos:
    items: List[Task] = field(default_factory=list)

    def add_task(self, name: str, due_date: datetime, priority: int) -> None:
        self.items.append(Task(name, due_date, priority))
        print(f"The following item was added: {name}")

    def remove_task(self, name: str) -> List[Task]:
        self.items = [task for task in self.items if task.name != name]
        print(f"The following item was removed: {name}")
        return self.items

    def sort_tasks(self) -> List[Task]:
        print(f"Sorting the tasks...")
        sorted(self.items, key=lambda task: task.priority)
        return self.items

    def list_all_tasks(self) -> None:
        """
        Display all tasks in a formatted, human-readable way.

        If no tasks exist, displays an appropriate message.
        Tasks are shown with their name, due date, and priority level.
        """
        if not self.items:
            print("No tasks found.")
            return

        print("\n" + "=" * 60)
        print(f"{'TASK LIST':^60}")
        print("=" * 60)

        for i, task in enumerate(self.items, 1):
            priority_text = _get_priority_text(task.priority)
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M")

            print(f"{i:2d}. {task.name}")
            print(f"    Due: {due_date_str}")
            print(f"    Priority: {priority_text}")
            print("-" * 40)

        print(f"\nTotal tasks: {len(self.items)}")


def main():
    todos = Todos()
    todos.add_task("Curatenie casa", datetime.now(), 0)
    todos.add_task("Curatenie motan", datetime.now(), 1)
    todos.add_task("Cumparaturi", datetime.now(), 0)
    todos.add_task("Curatenie casa", datetime.now(), 0)
    todos.add_task("Curat frigider", datetime.now(), 0)


if __name__ == "__main__":
    main()
