from IPython.display import display, HTML

def display_model_results(title, r2, rmse, feature_importances):
    html = f"""
    <div style="
        border: 1px solid #ccc;
        border-left: 6px solid #3498db;
        background-color: #ecf9ff;
        padding: 15px 20px;
        margin-top: 20px;
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
        color: #2c3e50;
    ">
        <h3 style="text-align:center"><strong>{title}</strong></h3>
        <p><strong>R² Score:</strong> {r2:.4f}</p>
        <p><strong>RMSE:</strong> {rmse:.2f}</p>
        <p><strong>Top Feature Importances:</strong></p>
        <ul>
    """
    for feature, importance in feature_importances.items():
        html += f"<li><strong>{feature}</strong>: {importance:.3f}</li>"
    html += "</ul></div>"
    display(HTML(html))