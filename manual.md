# ChatDev Flask Arxiv Papers Web App User Manual

Welcome to the user manual for the ChatDev Flask Arxiv Papers Web App! This manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it effectively.

## Table of Contents

1. [Installation](#installation)
2. [Main Functions](#main-functions)
3. [Usage](#usage)
4. [Testing](#testing)

## 1. Installation <a name="installation"></a>

To install the ChatDev Flask Arxiv Papers Web App, please follow the steps below:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/your_username/your_repository.git
   ```

2. Create a new conda environment:

   ```
   conda create --name flask-arxiv-app python=3.11
   ```

3. Activate the conda environment:

   ```
   conda activate flask-arxiv-app
   ```

4. Navigate to the project directory:

   ```
   cd your_repository
   ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run the Flask app:

   ```
   python main.py
   ```

Congratulations! You have successfully installed the ChatDev Flask Arxiv Papers Web App.

## 2. Main Functions <a name="main-functions"></a>

The ChatDev Flask Arxiv Papers Web App provides the following main functions:

- Displaying recent papers on Arxiv about AI agents.
- Storing paper information in a SQLite database.
- Scraping Arxiv using an API call each day to update the database.

## 3. Usage <a name="usage"></a>

To use the ChatDev Flask Arxiv Papers Web App, follow these steps:

1. Open a web browser and navigate to `http://localhost:5000` (or the appropriate URL if running on a remote server).

2. The main page will display a table with columns for paper name, date, and title.

3. The table will be populated with the most recent papers on Arxiv about AI agents.

4. To update the table with the latest papers, an API call is made each day to scrape Arxiv and store the new papers in the SQLite database.

## 4. Testing <a name="testing"></a>

The ChatDev Flask Arxiv Papers Web App includes unit and integration tests developed using pytest. To run the tests, follow these steps:

1. Activate the conda environment:

   ```
   conda activate flask-arxiv-app
   ```

2. Navigate to the project directory:

   ```
   cd your_repository
   ```

3. Run the pytest command:

   ```
   pytest
   ```

   The tests will be executed, and the results will be displayed in the terminal.

Congratulations! You have completed the user manual for the ChatDev Flask Arxiv Papers Web App. If you have any further questions or need assistance, please don't hesitate to contact our support team. Enjoy using the app!