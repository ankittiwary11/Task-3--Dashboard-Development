# ============================================================
# Task 3: Dashboard Development
# Intern: Ankit Tiwary
# Company: CodTech IT Solutions Pvt. Ltd.
# Internship Domain: Data Analytics
# Tool Used: Dash (Plotly) + Pandas
# ============================================================

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ----------------------------------------------------------
# 1. LOAD & PREPARE DATA
# ----------------------------------------------------------
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Profit_Margin"] = (df["Profit"] / df["Sales"] * 100).round(2)

# ----------------------------------------------------------
# 2. APP INITIALISATION
# ----------------------------------------------------------
app = dash.Dash(__name__, title="Sales Analytics Dashboard")

# ----------------------------------------------------------
# 3. COLOUR PALETTE
# ----------------------------------------------------------
COLORS = {
    "bg": "#0f172a",
    "card": "#1e293b",
    "accent": "#38bdf8",
    "text": "#e2e8f0",
    "muted": "#94a3b8",
    "positive": "#4ade80",
    "warning": "#facc15",
}

CARD_STYLE = {
    "backgroundColor": COLORS["card"],
    "borderRadius": "12px",
    "padding": "20px",
    "boxShadow": "0 4px 20px rgba(0,0,0,0.3)",
}

# ----------------------------------------------------------
# 4. LAYOUT
# ----------------------------------------------------------
app.layout = html.Div(
    style={"backgroundColor": COLORS["bg"], "minHeight": "100vh", "fontFamily": "'Segoe UI', Arial, sans-serif", "color": COLORS["text"]},
    children=[

        # ── HEADER ──────────────────────────────────────────
        html.Div(
            style={"background": "linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%)",
                   "padding": "28px 40px", "borderBottom": f"2px solid {COLORS['accent']}"},
            children=[
                html.H1("📊 Sales Analytics Dashboard",
                        style={"margin": 0, "fontSize": "2rem", "color": COLORS["accent"], "fontWeight": "700"}),
                html.P("CodTech IT Solutions | Data Analytics Internship — Task 3",
                       style={"margin": "6px 0 0", "color": COLORS["muted"], "fontSize": "0.9rem"}),
            ]
        ),

        # ── FILTERS ROW ─────────────────────────────────────
        html.Div(
            style={"display": "flex", "flexWrap": "wrap", "gap": "20px",
                   "padding": "24px 40px 8px"},
            children=[
                html.Div([
                    html.Label("Region", style={"color": COLORS["muted"], "fontSize": "0.8rem", "marginBottom": "6px", "display": "block"}),
                    dcc.Dropdown(
                        id="filter-region",
                        options=[{"label": "All Regions", "value": "All"}] +
                                [{"label": r, "value": r} for r in sorted(df["Region"].unique())],
                        value="All",
                        clearable=False,
                        style={"width": "180px", "backgroundColor": COLORS["card"], "color": "#000"},
                    )
                ]),
                html.Div([
                    html.Label("Category", style={"color": COLORS["muted"], "fontSize": "0.8rem", "marginBottom": "6px", "display": "block"}),
                    dcc.Dropdown(
                        id="filter-category",
                        options=[{"label": "All Categories", "value": "All"}] +
                                [{"label": c, "value": c} for c in sorted(df["Category"].unique())],
                        value="All",
                        clearable=False,
                        style={"width": "210px", "backgroundColor": COLORS["card"], "color": "#000"},
                    )
                ]),
                html.Div([
                    html.Label("Customer Segment", style={"color": COLORS["muted"], "fontSize": "0.8rem", "marginBottom": "6px", "display": "block"}),
                    dcc.Dropdown(
                        id="filter-segment",
                        options=[{"label": "All Segments", "value": "All"}] +
                                [{"label": s, "value": s} for s in sorted(df["Customer_Segment"].unique())],
                        value="All",
                        clearable=False,
                        style={"width": "200px", "backgroundColor": COLORS["card"], "color": "#000"},
                    )
                ]),
            ]
        ),

        # ── KPI CARDS ───────────────────────────────────────
        html.Div(id="kpi-row",
                 style={"display": "flex", "flexWrap": "wrap", "gap": "20px",
                        "padding": "16px 40px"}),

        # ── ROW 1: Line + Bar ────────────────────────────────
        html.Div(
            style={"display": "flex", "flexWrap": "wrap", "gap": "20px", "padding": "0 40px 20px"},
            children=[
                html.Div(dcc.Graph(id="line-sales"), style={**CARD_STYLE, "flex": "2", "minWidth": "320px"}),
                html.Div(dcc.Graph(id="bar-region"), style={**CARD_STYLE, "flex": "1", "minWidth": "260px"}),
            ]
        ),

        # ── ROW 2: Pie + Scatter + Top Products ─────────────
        html.Div(
            style={"display": "flex", "flexWrap": "wrap", "gap": "20px", "padding": "0 40px 20px"},
            children=[
                html.Div(dcc.Graph(id="pie-category"), style={**CARD_STYLE, "flex": "1", "minWidth": "260px"}),
                html.Div(dcc.Graph(id="scatter-profit"), style={**CARD_STYLE, "flex": "2", "minWidth": "320px"}),
            ]
        ),

        # ── ROW 3: Heatmap ───────────────────────────────────
        html.Div(
            style={"padding": "0 40px 40px"},
            children=[
                html.Div(dcc.Graph(id="heatmap-segment"), style=CARD_STYLE),
            ]
        ),

        # ── FOOTER ──────────────────────────────────────────
        html.Div(
            "Developed by Ankit Tiwary | CodTech IT Solutions Internship | Data Analytics Task 3",
            style={"textAlign": "center", "padding": "16px", "color": COLORS["muted"],
                   "borderTop": f"1px solid {COLORS['card']}", "fontSize": "0.82rem"}
        )
    ]
)


# ----------------------------------------------------------
# 5. HELPER: FILTER DATA
# ----------------------------------------------------------
def filter_df(region, category, segment):
    filtered = df.copy()
    if region != "All":
        filtered = filtered[filtered["Region"] == region]
    if category != "All":
        filtered = filtered[filtered["Category"] == category]
    if segment != "All":
        filtered = filtered[filtered["Customer_Segment"] == segment]
    return filtered


# ----------------------------------------------------------
# 6. CALLBACKS
# ----------------------------------------------------------
@app.callback(
    Output("kpi-row", "children"),
    Output("line-sales", "figure"),
    Output("bar-region", "figure"),
    Output("pie-category", "figure"),
    Output("scatter-profit", "figure"),
    Output("heatmap-segment", "figure"),
    Input("filter-region", "value"),
    Input("filter-category", "value"),
    Input("filter-segment", "value"),
)
def update_dashboard(region, category, segment):
    d = filter_df(region, category, segment)

    PLOT_BG = COLORS["card"]
    PAPER_BG = COLORS["card"]
    TEXT_COL = COLORS["text"]
    FONT = dict(family="Segoe UI, Arial", size=12, color=TEXT_COL)

    # ── KPIs ─────────────────────────────────────────────
    total_sales = d["Sales"].sum()
    total_profit = d["Profit"].sum()
    total_orders = len(d)
    avg_margin = d["Profit_Margin"].mean() if len(d) > 0 else 0

    def kpi_card(title, value, icon, color):
        return html.Div(
            style={**CARD_STYLE, "flex": "1", "minWidth": "160px", "borderTop": f"3px solid {color}"},
            children=[
                html.Div(icon, style={"fontSize": "1.6rem", "marginBottom": "8px"}),
                html.Div(title, style={"color": COLORS["muted"], "fontSize": "0.78rem", "marginBottom": "4px"}),
                html.Div(value, style={"fontSize": "1.5rem", "fontWeight": "700", "color": color}),
            ]
        )

    kpi_children = [
        kpi_card("Total Sales", f"₹{total_sales:,.0f}", "💰", COLORS["accent"]),
        kpi_card("Total Profit", f"₹{total_profit:,.0f}", "📈", COLORS["positive"]),
        kpi_card("Total Orders", f"{total_orders}", "🛒", COLORS["warning"]),
        kpi_card("Avg Profit Margin", f"{avg_margin:.1f}%", "🎯", "#f472b6"),
    ]

    # ── LINE: Monthly Sales Trend ─────────────────────────
    monthly = d.groupby("Month")[["Sales", "Profit"]].sum().reset_index()
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=monthly["Month"], y=monthly["Sales"],
                                  mode="lines+markers", name="Sales",
                                  line=dict(color=COLORS["accent"], width=2.5),
                                  marker=dict(size=7)))
    fig_line.add_trace(go.Scatter(x=monthly["Month"], y=monthly["Profit"],
                                  mode="lines+markers", name="Profit",
                                  line=dict(color=COLORS["positive"], width=2.5, dash="dot"),
                                  marker=dict(size=7)))
    fig_line.update_layout(title="Monthly Sales & Profit Trend", plot_bgcolor=PLOT_BG,
                           paper_bgcolor=PAPER_BG, font=FONT, legend=dict(bgcolor="rgba(0,0,0,0)"),
                           xaxis=dict(tickangle=-45, gridcolor="#334155"),
                           yaxis=dict(gridcolor="#334155"), margin=dict(t=45, b=10))

    # ── BAR: Sales by Region ──────────────────────────────
    reg = d.groupby("Region")["Sales"].sum().reset_index().sort_values("Sales", ascending=True)
    fig_bar = px.bar(reg, x="Sales", y="Region", orientation="h",
                     color="Sales", color_continuous_scale=["#1e3a5f", COLORS["accent"]],
                     title="Sales by Region")
    fig_bar.update_layout(plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG, font=FONT,
                          coloraxis_showscale=False, margin=dict(t=45, b=10),
                          yaxis=dict(gridcolor="#334155"), xaxis=dict(gridcolor="#334155"))

    # ── PIE: Sales by Category ────────────────────────────
    cat = d.groupby("Category")["Sales"].sum().reset_index()
    fig_pie = px.pie(cat, names="Category", values="Sales", title="Sales by Category",
                     hole=0.45, color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_pie.update_layout(plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG, font=FONT,
                          margin=dict(t=45, b=10))

    # ── SCATTER: Sales vs Profit ──────────────────────────
    fig_scatter = px.scatter(d, x="Sales", y="Profit", color="Category", size="Quantity",
                             hover_data=["Product", "Region", "Customer_Segment"],
                             title="Sales vs Profit (bubble size = Quantity)",
                             color_discrete_sequence=px.colors.qualitative.Bold)
    fig_scatter.update_layout(plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG, font=FONT,
                              legend=dict(bgcolor="rgba(0,0,0,0)"),
                              xaxis=dict(gridcolor="#334155"), yaxis=dict(gridcolor="#334155"),
                              margin=dict(t=45, b=10))

    # ── HEATMAP: Category × Region ───────────────────────
    pivot = d.pivot_table(values="Sales", index="Category", columns="Region", aggfunc="sum", fill_value=0)
    fig_heat = go.Figure(go.Heatmap(
        z=pivot.values, x=pivot.columns.tolist(), y=pivot.index.tolist(),
        colorscale="Blues", text=pivot.values,
        texttemplate="₹%{text:,.0f}", hoverongaps=False))
    fig_heat.update_layout(title="Sales Heatmap: Category × Region",
                           plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG, font=FONT,
                           margin=dict(t=45, b=10))

    return kpi_children, fig_line, fig_bar, fig_pie, fig_scatter, fig_heat


# ----------------------------------------------------------
# 7. RUN SERVER
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
