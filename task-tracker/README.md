# Task Tracker
This is a CLI task tracker build with Python. Based on the requirements from [roadmap.sh](https://roadmap.sh/projects/task-tracker)

## Requirements
- Create a command line application with persistent storage using local JSON.
- No external libraries or frameworks can be used
- Users should be able to do all CRUD operation on the tasks

## How to Run
Must have Python downloaded (version >= 3.9.2)

After downloading this project, navigate to the task-tracker directory. And run the following command:
`python src/main.py -h`

If the application was successfully downloaded, a list of available commands should appear.

## Technologies Used
- Python
    - argparse
    - json


## Code Decisions

### File Separation
I decided to separate the application into the following layers:
- UI
- Data
- Storage

By separating the code in this way, it would make it easier to swap the implementation of one layer with another. E.g. swap JSON storage with a SQL database.