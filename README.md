# 📊 CSV Analysis Web Application

This is a Django-based web application that allows users to upload CSV files, analyze data, and generate interactive visualizations. It leverages **Plotly** for dynamic graphing and **Pandas** for data manipulation.

---

## 🚀 Features

✅ **CSV Upload**: Upload CSV files and display the first few rows.\
✅ **Data Analysis**: Generate summary statistics (mean, median, etc.) and display missing values.\
✅ **Interactive Visualizations**:

- 📈 **Scatter Plots**
- 📊 **Histograms**
- 📦 **Box Plots**
- 🥧 **Pie Charts**
- 📊 **Bar Charts**
- 🔥 **Heatmaps** ✅ **Dynamic Graph Generation**: Select specific columns to visualize data interactively.

---

## 📋 Prerequisites

Ensure you have the following installed before running the project:

- 🐍 Python **3.7+**
- 🏗️ Django
- 📊 Pandas
- 📉 Plotly

### 🔹 Install Python 3.x

📥 Download from the official Python website: [Python Downloads](https://www.python.org/downloads/)

### 🔹 Install Dependencies

1️⃣ **Clone the repository**:

```bash
git clone https://github.com/yourusername/csv-analysis-webapp.git
cd csv-analysis-webapp
```

2️⃣ **Create a virtual environment (recommended):**

```bash
python -m venv venv
```

3️⃣ **Activate the virtual environment:**

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

4️⃣ **Install required dependencies:**

```bash
pip install -r requirements.txt
```

💡 If `requirements.txt` is missing, generate it with:

```bash
pip freeze > requirements.txt
```

---

## ▶️ Running the Project

1️⃣ **Apply Migrations** (if necessary):

```bash
python manage.py migrate
```

2️⃣ **Start the Server**:

```bash
python manage.py runserver
```

🔗 Your application will be accessible at: [http://localhost:8000/](http://localhost:8000/)

---

## 🛠️ Usage

🔹 **Upload a CSV file** via the "Choose File" button.\
🔹 **View basic statistics**, summary, and missing values.\
🔹 **Generate graphs** dynamically using dropdown selections.

---

## 📂 File Structure

```
csv-analysis-webapp/
│
├── analysis/
│   ├── migrations/
│   ├── templates/
│   │   ├── analysis_results.html
│   │   ├── upload.html
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

---

## 🔄 Project Flow

1️⃣ **Upload CSV** 📂 → Read data into a Pandas DataFrame.\
2️⃣ **Data Cleaning & Processing** 🧹 → Handle missing values and data types.\
3️⃣ **Graph Generation** 📊 → Users select columns for interactive visualizations.\
4️⃣ **Dynamic Updates** 🔄 → AJAX-based updates for seamless experience.

---

## 🛑 Troubleshooting

🔹 **File Upload Issues?** Increase the allowed file size in `settings.py`:

```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB
```

🔹 **Graphs Not Displaying?** Ensure valid columns are selected (e.g., categorical for pie/bar charts).

---

## 🎯 Conclusion

This web application provides an interactive way to analyze and visualize CSV data using Django and Plotly. 🚀

Feel free to ⭐ **star** this project if you find it useful!

---

