from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
import plotly.express as px
import plotly.io as pio

uploaded_df = None  # Store the uploaded dataframe globally

def upload_csv(request):
    global uploaded_df

    if request.method == "POST" and "csv_file" in request.FILES:
        csv_file = request.FILES["csv_file"]
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file, encoding="ISO-8859-1")

            if df.empty:
                return render(request, "upload.html", {"error_message": "Uploaded CSV file is empty."})

            # Process date and numeric columns, but ensure that categorical columns remain unchanged
            for col in df.columns:
                if "date" in col.lower() or "time" in col.lower():
                    df[col] = pd.to_datetime(df[col], errors="coerce")
                elif df[col].dtype == "object":
                    df[col] = df[col].astype(str)  # Explicitly ensure they are treated as categorical
                else:
                    # For numeric columns, keep them as numeric
                    df[col] = pd.to_numeric(df[col], errors="coerce")

            uploaded_df = df

            # Extract categorical columns (columns with dtype 'object')
            categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

            # If no categorical columns, add a message
            if not categorical_columns:
                categorical_columns = ["No categorical columns found in the dataset"]

            # Extract numerical columns
            numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()

            # Generate default graphs
            graphs_context = generate_default_graphs(df)

            context = {
                "csv_data": df.head().to_html(classes="table table-striped"),
                "summary_stats": df.describe(include="all").to_html(classes="table table-bordered"),
                "missing_values": df.isnull().sum().to_dict(),
                **graphs_context,
                "numerical_columns": numerical_columns,
                "categorical_columns": categorical_columns,  # Pass categorical columns to template
            }
            return render(request, "analysis_results.html", context)
        
        except Exception as e:
            return render(request, "upload.html", {"error_message": f"Error processing file: {e}"})

    return render(request, "upload.html")





def update_graph(request):
    global uploaded_df

    if uploaded_df is None:
        return JsonResponse({"error": "No data uploaded yet."}, status=400)

    graph_type = request.POST.get("graph_type")

    # Handle specific graph types and generate corresponding graphs
    if graph_type == "scatter":
        scatter_x = request.POST.get("scatter_x")
        scatter_y = request.POST.get("scatter_y")
        scatter_fig = px.scatter(uploaded_df, x=scatter_x, y=scatter_y, title="Scatter Plot")
        return JsonResponse({"scatter_html": pio.to_html(scatter_fig, full_html=False)})

    elif graph_type == "histogram":
        histogram_x = request.POST.get("histogram_x")
        histogram_fig = px.histogram(uploaded_df, x=histogram_x, nbins=20, title="Histogram")
        return JsonResponse({"histogram_html": pio.to_html(histogram_fig, full_html=False)})

    elif graph_type == "box":
        box_y = request.POST.get("box_y")
        box_fig = px.box(uploaded_df, y=box_y, title="Box Plot")
        return JsonResponse({"box_html": pio.to_html(box_fig, full_html=False)})

    elif graph_type == "heatmap":
        heatmap_x = request.POST.get("heatmap_x")
        heatmap_y = request.POST.get("heatmap_y")
        heatmap_fig = px.imshow(uploaded_df[[heatmap_x, heatmap_y]].corr(), text_auto=True, title="Heatmap")
        return JsonResponse({"heatmap_html": pio.to_html(heatmap_fig, full_html=False)})

    # Handle specific graph types and generate corresponding graphs
    if graph_type == "pie":
        pie_column = request.POST.get("pie_column")
        if pie_column and uploaded_df[pie_column].dtype == 'object' and uploaded_df[pie_column].nunique() > 1:
            pie_fig = px.pie(uploaded_df, names=pie_column, title="Pie Chart")
            return JsonResponse({"pie_html": pio.to_html(pie_fig, full_html=False)})
        else:
            return JsonResponse({"error": f"The column '{pie_column}' is not suitable for a pie chart."}, status=400)

    elif graph_type == "bar":
        bar_column = request.POST.get("bar_column")
        if bar_column and uploaded_df[bar_column].dtype == 'object' and uploaded_df[bar_column].nunique() > 1:
            bar_fig = px.bar(uploaded_df[bar_column].value_counts(), x=uploaded_df[bar_column].value_counts().index,
                             y=uploaded_df[bar_column].value_counts(), title="Bar Graph")
            return JsonResponse({"bar_html": pio.to_html(bar_fig, full_html=False)})
        else:
            return JsonResponse({"error": f"The column '{bar_column}' is not suitable for a bar graph."}, status=400)

    return JsonResponse({"error": "Invalid graph type or parameters."}, status=400)




def generate_default_graphs(df):
    graphs_context = {}
    numerical_cols = df.select_dtypes(include=["number"]).columns
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    # Default Scatter Plot
    if len(numerical_cols) > 1:
        scatter_fig = px.scatter(df, x=numerical_cols[0], y=numerical_cols[1], title="Default Scatter Plot")
        graphs_context["scatter_html"] = pio.to_html(scatter_fig, full_html=False)

    # Default Histogram
    if len(numerical_cols) > 0:
        histogram_fig = px.histogram(df, x=numerical_cols[0], nbins=20, title="Default Histogram")
        graphs_context["histogram_html"] = pio.to_html(histogram_fig, full_html=False)

    # Default Box Plot
    if len(numerical_cols) > 0:
        box_fig = px.box(df, y=numerical_cols[0], title="Default Box Plot")
        graphs_context["box_html"] = pio.to_html(box_fig, full_html=False)

    # Default Heatmap
    if len(numerical_cols) > 1:
        heatmap_fig = px.density_heatmap(df, x=numerical_cols[0], y=numerical_cols[1], title="Default Heatmap")
        graphs_context["heatmap_html"] = pio.to_html(heatmap_fig, full_html=False)

    # Default Pie Chart
    if len(categorical_cols) > 0:
        pie_fig = px.pie(df, names=categorical_cols[0], title="Default Pie Chart")
        graphs_context["pie_html"] = pio.to_html(pie_fig, full_html=False)

    # Default Bar Graph
    if len(categorical_cols) > 0 and len(numerical_cols) > 0:
        bar_fig = px.bar(df, x=categorical_cols[0], y=numerical_cols[0], title="Default Bar Graph")
        graphs_context["bar_html"] = pio.to_html(bar_fig, full_html=False)

    return graphs_context


def generate_graphs(df, scatter_x=None, scatter_y=None, histogram_x=None, box_y=None, heatmap_x=None, heatmap_y=None, pie_column=None, bar_column=None):
    graphs_context = {}

    # Scatter Plot
    if scatter_x and scatter_y:
        scatter_fig = px.scatter(df, x=scatter_x, y=scatter_y, title="Scatter Plot")
        graphs_context["scatter_html"] = pio.to_html(scatter_fig, full_html=False)

    # Histogram
    if histogram_x:
        histogram_fig = px.histogram(df, x=histogram_x, nbins=20, title="Histogram")
        graphs_context["histogram_html"] = pio.to_html(histogram_fig, full_html=False)

    # Box Plot
    if box_y:
        box_fig = px.box(df, y=box_y, title="Box Plot")
        graphs_context["box_html"] = pio.to_html(box_fig, full_html=False)

    # Heatmap
    if heatmap_x and heatmap_y:
        heatmap_fig = px.imshow(df[[heatmap_x, heatmap_y]].corr(), text_auto=True, title="Heatmap")
        graphs_context["heatmap_html"] = pio.to_html(heatmap_fig, full_html=False)

    # Pie Chart
    if pie_column:
        if pie_column in df.columns and (df[pie_column].dtype == 'object' or df[pie_column].nunique() < 20):
            df_cleaned = df[pie_column].dropna()  # Remove NaN values
            pie_fig = px.pie(df_cleaned, names=pie_column, title="Pie Chart")
            graphs_context["pie_html"] = pio.to_html(pie_fig, full_html=False)
        else:
            graphs_context["error"] = f"The column '{pie_column}' is not suitable for a pie chart."

    # Bar Graph
    if bar_column:
        if bar_column in df.columns and (df[bar_column].dtype == 'object' or df[bar_column].nunique() < 20):
            df_cleaned = df[bar_column].dropna()  # Remove NaN values
            bar_fig = px.bar(df_cleaned.value_counts(), x=df_cleaned.value_counts().index,
                             y=df_cleaned.value_counts(), title="Bar Graph")
            graphs_context["bar_html"] = pio.to_html(bar_fig, full_html=False)
        else:
            graphs_context["error"] = f"The column '{bar_column}' is not suitable for a bar graph."

    return graphs_context
