from IPython.display import display, HTML

def display_model_results(title, r2, rmse, feature_importances):
    html = f"""
    <div style="
        border: 1px solid #d0e6f7;
        border-left: 6px solid #3498db;
        background-color: #f4faff;
        padding: 20px 25px;
        margin-top: 25px;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
        color: #2c3e50;
  
    ">
        <h2 style="text-align:center; color: #2980b9; margin-bottom: 20px;">{title}</h2>
        <p style="margin: 5px 0;"><strong>R² Score:</strong> <span style="color:#16a085;">{r2:.4f}</span></p>
        <p style="margin: 5px 0;"><strong>RMSE:</strong> <span style="color:#e67e22;">{rmse:.2f}</span></p>
        <p style="margin: 10px 0 5px;"><strong>Top Feature Importances:</strong></p>
        <ul style="margin-left: 20px; line-height: 1.6;">
    """
    for feature, importance in feature_importances.items():
        html += f"<li><strong>{feature}</strong>: <span style='color:#34495e;'>{importance:.3f}</span></li>"
    html += "</ul></div>"
    display(HTML(html))