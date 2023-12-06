import tkinter as tk
from tkinter import mainloop, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST APP ")

        self.tasks = []

        self.create_widgets()
        # تحديد لون الخلفية للنافذة
        self.root.configure(bg="#E0FFFF")

    def create_widgets(self):
        # إدخال لإضافة المهام
        self.entry_task = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.entry_task.grid(row=0, column=0, padx=10, pady=10)

        # زر لإضافة المهام
        self.add_button = tk.Button(self.root, text="Add Task", width=15, command=self.add_task,bg="#659EC7",fg="white", font=("Arial", 12))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox لعرض المهام
        self.listbox_tasks = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10, font=("Arial", 12))
        self.listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # زر لحذف المهمة المحددة
        self.delete_button = tk.Button(self.root, text="Delet Task", width=15, command=self.delete_task,bg="#659EC7",fg="white", font=("Arial", 12))
        self.delete_button.grid(row=3, column=1, padx=10, pady=3)

        # زر لتحديد المهمة كمكتملة أو غير مكتملة
        self.toggle_button = tk.Button(self.root, text="Toggle Complete", width=15, command=self.toggle_completion,bg="#659EC7",fg="white", font=("Arial", 12))
        self.toggle_button.grid(row=2, column=1, padx=10, pady=3)
        # Button to delete all tasks
        self.delete_all_button = tk.Button(self.root, text="Delete All", width=15, command=self.delete_all_tasks,bg="#659EC7",fg="white", font=("Arial", 12))
        self.delete_all_button.grid(row=4, column=1, padx=5, pady=3)

        # Button to exit the application
        self.exit_button = tk.Button(self.root, text="Exit", width=15, command=self.root.destroy,bg="#659EC7",fg="white", font=("Arial", 12))
        self.exit_button.grid(row=6, column=1, padx=5, pady=3)
        


    def add_task(self):
        task = self.entry_task.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("WArning", " Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox_tasks.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def toggle_completion(self):
        try:
            selected_task_index = self.listbox_tasks.curselection()[0]
            self.tasks[selected_task_index]["completed"] = not self.tasks[selected_task_index]["completed"]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Pleasa select a task to toggle completion satus.")

    def delete_all_tasks(self):
      confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?")
      if confirmed:
          self.tasks = []
          self.update_listbox()
  
    def update_listbox(self):
        self.listbox_tasks.delete(0, tk.END)
        for index, task_data in enumerate(self.tasks, start=1):
            task_text = f"[{'✔' if task_data['completed'] else '✘'}] {task_data['task']}"
            self.listbox_tasks.insert(tk.END, task_text)

            # تخصيص ألوان خلفية المهمة
            if task_data["completed"]:
                self.listbox_tasks.itemconfig(index - 1, {'bg': '#C2F0C2'})  # خلفية مهمة مكتملة
            else:
                self.listbox_tasks.itemconfig(index - 1, {'bg': '#FFB6B6'})  # خلفية مهمة غير مكتملة

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
  

if __name__ == "__main__":
    main()


