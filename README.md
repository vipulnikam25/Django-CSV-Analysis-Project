# CSV Analysis Web Application

This project is a web application built using Django that allows users to upload CSV files, perform basic data analysis, and generate visualizations such as scatter plots, histograms, box plots, pie charts, bar charts, and heatmaps. The application uses **Plotly** for interactive graphing and **Pandas** for data manipulation.

## Features

- **CSV Upload**: Upload CSV files and display the first few rows.
- **Data Analysis**: Generate summary statistics (mean, median, etc.) and display missing values.
- **Visualizations**:
  - Scatter plots
  - Histograms
  - Box plots
  - Pie charts
  - Bar charts
  - Heatmaps

- **Dynamic Graph Generation**: Choose specific columns to generate desired graphs.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7+  
- Django  
- Pandas  
- Plotly  

### Install Python 3.x

If you don’t have Python installed, you can download it from the official Python website:
[Python Downloads](https://www.python.org/downloads/)

### Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/yourusername/csv-analysis-webapp.git
cd csv-analysis-webapp
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Create `requirements.txt`

If the `requirements.txt` is not available in your project, you can create it by running the following command in the virtual environment:

```bash
pip freeze > requirements.txt
```

**Example `requirements.txt`**:
```
Django==4.1.1
pandas==1.5.3
plotly==5.10.0
```

## Running the Project

1. **Set up the database (optional)**:
   
   If your project requires any migrations (e.g., models for user authentication), run the following:

```bash
python manage.py migrate
```

2. **Start the server**:

```bash
python manage.py runserver
```

Your web application will be live at [http://localhost:8000/](http://localhost:8000/).

## Usage

- **Upload a CSV file**: Click on the "Choose File" button to upload a CSV file.
- **Data Analysis**: After uploading, the first few rows, summary statistics, and missing values of the dataset will be displayed.
- **Graph Generation**: You can choose which columns to visualize (scatter plot, bar chart, pie chart, etc.) from dropdown menus.
  
## File Structure

```
csv-analysis-webapp/
│
├── analysis/
│   ├── migrations/
│   ├── templates/
│   │   └── analysis_results.html
│   │   └── upload.html
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Project Flow

1. **Upload CSV**: The user uploads a CSV file, and the data is read into a pandas DataFrame.
2. **Data Cleaning and Processing**: The CSV data is processed to handle dates, missing values, and numeric conversions.
3. **Graph Generation**: Based on user input, the selected columns are used to generate interactive visualizations with Plotly.
4. **Dynamic Updates**: Users can dynamically update the graphs via AJAX requests without reloading the page.

## Troubleshooting

- If you encounter issues with the file upload (e.g., the file is too large), ensure that your server configuration allows for larger uploads. You can adjust the file size limit in `settings.py`:
  
```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760 / 10MB
```

- If graphs are not generating, make sure the columns selected are valid (e.g., categorical columns for pie and bar charts).

## Conclusion

This web application allows you to perform quick data analysis and visualization on CSV files in an interactive manner. It is built using Django for the backend and Plotly for dynamic and interactive visualizations.

--- 