from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import IntEnum


class Priority(IntEnum):
    """Task priority levels."""
    HIGH = 0
    MEDIUM = 1
    LOW = 2


@dataclass
class Task:
    name: str
    due_date: datetime
    priority: Priority
    completed: bool = False

    def __str__(self) -> str:
        status = "✅" if self.completed else "⏳"
        return f"{status} {self.name} (Due: {self.due_date.strftime('%Y-%m-%d %H:%M')})"


@dataclass
class TodoList:
    """A collection of tasks with various management operations."""
    items: List[Task] = field(default_factory=list)

    @staticmethod
    def _get_priority_text(priority: Priority) -> str:
        """Convert numeric priority to a descriptive text."""
        priority_map = {
            Priority.HIGH: "🔴 High",
            Priority.MEDIUM: "🟡 Medium",
            Priority.LOW: "🟢 Low"
        }
        return priority_map.get(priority, f"Priority {priority}")

    def add_task(self, name: str, due_date: datetime, priority: Priority) -> None:
        """Add a new task to the list."""
        if not name.strip():
            raise ValueError("Task name cannot be empty")
        
        task = Task(name.strip(), due_date, priority)
        self.items.append(task)
        print(f"✅ Added task: {name}")

    def remove_task(self, name: str) -> bool:
        """Remove a task by name. Returns True if task was found and removed."""
        original_count = len(self.items)
        self.items = [task for task in self.items if task.name != name.strip()]
        
        if len(self.items) < original_count:
            print(f"🗑️ Removed task: {name}")
            return True
        else:
            print(f"❌ Task not found: {name}")
            return False

    def complete_task(self, name: str) -> bool:
        """Mark a task as completed. Returns True if task was found."""
        for task in self.items:
            if task.name == name.strip():
                task.completed = True
                print(f"🎉 Completed task: {name}")
                return True
        
        print(f"❌ Task not found: {name}")
        return False

    def find_task(self, name: str) -> Optional[Task]:
        """Find a task by name."""
        for task in self.items:
            if task.name.lower() == name.strip().lower():
                return task
        return None

    def sort_tasks(self, by_priority: bool = True, by_due_date: bool = False) -> None:
        """Sort tasks by priority and/or due date."""
        if by_priority and by_due_date:
            self.items.sort(key=lambda task: (task.priority, task.due_date))
            print("📋 Sorted tasks by priority and due date")
        elif by_priority:
            self.items.sort(key=lambda task: task.priority)
            print("📋 Sorted tasks by priority")
        elif by_due_date:
            self.items.sort(key=lambda task: task.due_date)
            print("📋 Sorted tasks by due date")

    def get_pending_tasks(self) -> List[Task]:
        """Get all incomplete tasks."""
        return [task for task in self.items if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return [task for task in self.items if task.completed]

    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue incomplete tasks."""
        now = datetime.now()
        return [task for task in self.items 
                if not task.completed and task.due_date < now]

    def list_all_tasks(self, show_completed: bool = True) -> None:
        """Display all tasks in a formatted list."""
        tasks_to_show = self.items if show_completed else self.get_pending_tasks()
        
        if not tasks_to_show:
            message = "No tasks found." if show_completed else "No pending tasks found."
            print(f"📝 {message}")
            return

        print("\n" + "=" * 70)
        print(f"{'TASK LIST':^70}")
        print("=" * 70)

        for i, task in enumerate(tasks_to_show, 1):
            priority_text = self._get_priority_text(task.priority)
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M")
            status_icon = "✅" if task.completed else "⏳"
            
            # Highlight overdue tasks
            is_overdue = not task.completed and task.due_date < datetime.now()
            overdue_marker = " ⚠️ OVERDUE" if is_overdue else ""

            print(f"{i:2d}. {status_icon} {task.name}{overdue_marker}")
            print(f"    📅 Due: {due_date_str}")
            print(f"    🔥 Priority: {priority_text}")
            print("-" * 50)

        completed_count = len(self.get_completed_tasks())
        pending_count = len(self.get_pending_tasks())
        overdue_count = len(self.get_overdue_tasks())
        
        print(f"\n📊 Summary:")
        print(f"   Total: {len(self.items)} | Pending: {pending_count} | "
              f"Completed: {completed_count} | Overdue: {overdue_count}")

    def clear_completed_tasks(self) -> int:
        """Remove all completed tasks. Returns number of tasks removed."""
        initial_count = len(self.items)
        self.items = [task for task in self.items if not task.completed]
        removed_count = initial_count - len(self.items)
        
        if removed_count > 0:
            print(f"🧹 Removed {removed_count} completed task(s)")
        
        return removed_count


def main():
    """Demo function showing TodoList usage."""
    todo_list = TodoList()
    
    # Add some sample tasks
    from datetime import timedelta
    
    now = datetime.now()
    todo_list.add_task("Curatenie casa", now + timedelta(days=1), Priority.HIGH)
    todo_list.add_task("Curatenie motan", now + timedelta(days=2), Priority.MEDIUM)
    todo_list.add_task("Cumparaturi", now + timedelta(hours=2), Priority.HIGH)
    todo_list.add_task("Curat frigider", now - timedelta(days=1), Priority.LOW)  # Overdue
    
    # Complete one task
    todo_list.complete_task("Curatenie motan")
    
    # Sort and display
    todo_list.sort_tasks(by_priority=True, by_due_date=True)
    todo_list.list_all_tasks()


if __name__ == "__main__":
    main()
