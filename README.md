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
pip install .
```

### To uninstall
```bash
pip uninstall taskcli
```

## ✨ Features
- View all tasks and by status
- Add a new task
- Remove a task
- Update a task description
- Mark tasks as to do, in progress or done

## 🚀 Usage
```bash
$ taskcli list [-h] [{done,in-progress,todo}]

$ taskcli add [-h] description

$ taskcli delete [-h] id

$ taskcli update [-h] id description

$ taskcli mark [-h] {done,in-progress,todo} id
```

## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

> Made for the [project](https://roadmap.sh/projects/task-tracker)
