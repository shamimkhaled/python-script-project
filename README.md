# Task 1: Classification of MNIST Dataset Using CNN

#### 1. In task 1 file code added with explanation

#### 2. Usage

- Go to google colab (https://colab.research.google.com/)

- Upload the Task1 .ipynb file on the google colab [Task1- Classification of MNIST Dataset Using CNN.ipynb]

- When open this project in google colab. Firstly, you need to do installing the all libraries in this project first cell using below command.

```bash
 !pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

- Then you can run this project in google colab.

# Task 3 and 4: Documentation and Google Sheets API Integration with Python

To create a Python script that uses the Google Sheets API to retrieve information from a Google Sheet you'll need to follow these steps:

#### 1. Set up your Google Sheets API credentials:

- Go to the Google Developers Console (https://console.developers.google.com/).
- Create a new project or select an existing one.
- Enable the Google Sheets API for your project.
- Create credentials for your project to access the API. Choose "Service Account" and provide the necessary information.
- In created service account, Choose "Key" to create key and download the JSON file containing your credentials, and save it securely.
- Share your Google Sheet with the service account email address mentioned in your JSON credentials file, giving it the appropriate permissions (e.g., edit, view).

#### 2. Clone the Git Repository:

After done the first step, then clone the project's Git repository using the following command:

```bash
https://github.com/shamimkhaled/python-script-project.git
```

#### 3. Set Up a Virtual Environment:

- Open the cloned project in Visual Studio Code (VS Code). In the VS Code terminal (either Command Prompt or Git Bash), create a virtual environment inside the project root folder:

```bash
  python -m venv env
```

- Activate the virtual environment:
  In Command Prompt terminal:

```bash
  .\env\Scripts\activate
```

or

In Git Bash terminal (replace the path with your virtual environment path):

```bash
source "C:\Users\shamim\Desktop\Python\env\Scripts\activate"
```

#### 4. Install the dependencies:

Install the required Python packages using pip:

```bash
  pip install gspread pandas gspread-dataframe
```

or

You can install all project dependencies by running the following command:

```bash
     pip install -r requirements.txt
```

#### 5. Navigate the [task_three_and_four] project directory:

```bash
    cd task_three_and_four
```

#### 6. Provide Credentials:

- Inside the [task_three_and_four] folder you see the python script. Replace 'YOUR_SECRET_KEY_PATH' in the Python script with the path to your downloaded JSON credentials file.

```bash
  gc = gspread.service_account(filename=r'YOUR_SECRET_KEY_PATH')
```

- Replace your spreadsheet key in the python script. You will find your spreadsheet key in your spreadsheet url like [https://docs.google.com/spreadsheets/d/1xnuS_DpLOBy0m9V6W8obs5pWWyKgUDB5uVKC3AB7QwI/edit#gid=0]. In this url spreadsheet key is "1xnuS_DpLOBy0m9V6W8obs5pWWyKgUDB5uVKC3AB7QwI"

```bash
    google_sheet_key = 'YOUR_SPREADSHEET_KEY'
```

#### 7. Usage

To use the script:

- Ensure the your virtual environment is activated and you are in the task_three_and_four project directory.

- Open the VS code terminal : Run the script using Python

```bash
  python google_sheet_api.py
```

### Important Details

- The script demonstrates basic interaction with a Google Sheet by retrieving, updating, and processing data.
- It assumes that the Google Sheet key and worksheet name are provided correctly.
- The script clears the worksheet and writes a DataFrame, so ensure you have a backup or are okay with the data being overwritten.
- Make sure your Google Sheet is shared appropriately, considering privacy and security implications.

# Task 2: Working on SQL Database Setup and Python Interaction

#### Usage

- Ensure the your previous created virtual environment activated. [Follow the Task 3 and 4 Documentation]

- Navigate the [Task2] project directory:

```bash
  cd Task2
```

- Open the VS code terminal and run the script using Python:

```bash
  python python_crud_sql.py
```

## Color Reference

| Color         | Hex                                                              |
| ------------- | ---------------------------------------------------------------- |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |

## Authors

- [@shamimkhaled](https://www.github.com/shamimkhaled)
