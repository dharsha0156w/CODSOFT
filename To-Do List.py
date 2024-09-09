import pickle
import os

class TodoApp:
    def __init__(self):
        self.filename = 'todos.pkl'
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        else:
            return []

    def save_todos(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.todos, f)

    def add_task(self, task):
        self.todos.append(task)
        self.save_todos()
        print(f'Task added: {task}')

    def list_tasks(self):
        if not self.todos:
            print('No tasks found.')
        else:
            for index, task in enumerate(self.todos, start=1):
                print(f'{index}. {task}')

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.todos):
            removed_task = self.todos.pop(task_index - 1)
            self.save_todos()
            print(f'Task removed: {removed_task}')
        else:
            print('Invalid task number.')

# Main program
app = TodoApp()

while True:
    print('\nTo-Do List Application')
    print('1. Add Task')
    print('2. List Tasks')
    print('3. Remove Task')
    print('4. Exit')

    choice = input('Enter your choice: ').strip()

    if choice == '1':
        task = input('Enter the task: ').strip()
        app.add_task(task)
    elif choice == '2':
        app.list_tasks()
    elif choice == '3':
        app.list_tasks()
        try:
            task_index = int(input('Enter the task number to remove: ').strip())
            app.remove_task(task_index)
        except ValueError:
            print('Please enter a valid number.')
    elif choice == '4':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please select a valid option.')
