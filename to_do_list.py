import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 12),
                                    command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 14))
        self.listbox.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.edit_button = tk.Button(button_frame, text="Edit Task", font=("Arial", 12),
                                     command=self.edit_task)
        self.edit_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 12),
                                       command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12),
                                      command=self.clear_tasks)
        self.clear_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def edit_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            current_task = self.tasks[selected_index]
            new_task = simpledialog.askstring("Edit Task", "Modify task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index] = new_task.strip()
                self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
