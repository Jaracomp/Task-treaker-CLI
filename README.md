# Task treaker CLI

## 📖 Description
Task treaker CLI is a command line interface for task management. You can add, remove, update and view tasks. All tasks are stored in a JSON file.

## ⚡ Installation
You can install Task treaker CLI directly from GitHub:
```bash
pip install git+https://github.com/Jaracomp/Task-treaker-CLI.git
```
or
```bash
git clone https://github.com/Jaracomp/Task-treaker-CLI.git
cd Task-treaker-CLI
pip install . -e
```

### To uninstall
```bash
pip uninstall taskcli
```

## ✨ Features
- View all tasks
- Add a new task
- Remove a task
- Update a task
- View tasks by status
- Mark tasks as to do
- Mark tasks as in progress
- Mark tasks as done

## 🚀 Usage
```bash
$ taskcli add [-h] description

$ taskcli delete [-h] id

$ taskcli update [-h] id description

$ taskcli mark-todo [-h] id

$ taskcli mark-done [-h] id

$ taskcli mark-in-progress [-h] id

$ taskcli list [-h] [{done,in-progress,todo}]
```

## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.
