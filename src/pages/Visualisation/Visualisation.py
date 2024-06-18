import pandas as pd
import polars as pl
import plotly.express as px
import plotly.graph_objs as go
import taipy.gui.builder as tgb
import os
from algorithms import preprocess, train_arima, train_xgboost, concat, forecast_xgboost, forecast

#strptime

data = pd.read_csv('data/modified_supermarkt_sales_plus_four_years.csv')
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data['Month_Year'] = data['Date'].dt.to_period('M').dt.to_timestamp()

def create_bar_figure(data, group_by):
    sales_over_time = data.groupby(group_by)['Total'].sum().reset_index()
    fig = px.bar(sales_over_time, x=group_by, y='Total', title=f'Sales Trends Over {group_by}', color='Total')
    return fig

def create_perc_fig(df, group_column):
    # Group, sum, and convert to percentage
    df = df.groupby(['Month_Year', group_column])['Total'].sum().unstack(fill_value=0)
    df = df.div(df.sum(axis=1), axis=0).reset_index().melt(id_vars='Month_Year', var_name=group_column, value_name='Percentage')
    df['Percentage'] = (df.loc[:, 'Percentage'].round(3) * 100)
    # Create and return the plot
    fig = px.bar(df, x='Month_Year', y='Percentage', color=group_column, title=f"Evolution of Sales by {group_column} over Time", labels={'Percentage': '% of Total'}, text_auto=True)
    return fig

fig_product_line = create_perc_fig(data, 'Product_line')
fig_city = create_perc_fig(data, 'City')
fig_gender = create_perc_fig(data, 'Gender')
fig_customer_type = create_perc_fig(data, 'Customer_type')


def on_change(state, var_name, var_value):
    if var_name in ['city', 'customer_type', 'gender']:
        data = state.data.loc[
            state.data["City"].isin(state.city)
            & state.data["Customer_type"].isin(state.customer_type)
            & state.data["Gender"].isin(state.gender), :
        ]

        state.fig_product_line = create_perc_fig(data, 'Product_line')
        state.fig_city = create_perc_fig(data, 'City')
        state.fig_gender = create_perc_fig(data, 'Gender')
        state.fig_customer_type = create_perc_fig(data, 'Customer_type')


def plot_total_sales_distribution(data):
    data['date'] = pd.to_datetime(data['Date'])
    data['year'] = data['date'].dt.year

    # Filter necessary columns for the plot
    filtered_data = data[['year', 'Total']]

    # Create the histogram plot
    fig = px.histogram(filtered_data, x='Total', color='year', barmode='overlay',
                       marginal='rug', histnorm='probability density',
                       labels={'Total': 'Total Sales', 'year': 'Year'})

    # Update layout for better visualization
    fig.update_layout(title='Distribution of Total Sales by Year',
                      xaxis_title='Total Sales',
                      yaxis_title='Frequency',
                      bargap=0.1)

    return fig

def plot_results_and_errors(initial_data, comparison_data, result):
    # Tracer les résultats avec Plotly Express
    fig = px.line(initial_data, x='Date', y='Total', title='Prévisions des ventes totales')
    fig.add_scatter(x=result['Date'], y=result['ARIMA'], mode='lines', name='Prévisions ARIMA', line=dict(color='red'))
    fig.add_scatter(x=result['Date'], y=result['Xgboost'], mode='lines', name='Prévisions XGBoost', line=dict(color='green'))

    # Comparer avec les données réelles
    comparison_data['Date'] = pd.to_datetime(comparison_data['Date'])
    comparison = pd.merge(result, comparison_data[['Date', 'Total']], on='Date', how='inner', suffixes=('', '_true'))

    # Calculer l'erreur de prédiction
    comparison['error_arima'] = comparison['Total'] - comparison['ARIMA']
    comparison['error_xgboost'] = comparison['Total'] - comparison['Xgboost']

    # Tracer les erreurs de prédiction avec Plotly Express
    fig_error = px.line(comparison, x='Date', y='error_arima', title='Erreur de prédiction au fil du temps')
    fig_error.add_scatter(x=comparison['Date'], y=comparison['error_xgboost'], mode='lines', name='Erreur XGBoost', line=dict(color='green'))
    
    return fig, fig_error

# Charger les données
initial_data = pd.read_csv('data/modified_supermarkt_sales_plus.csv')
comparison_data = pd.read_csv('data/modified_supermarkt_sales_plus_four_years.csv')

# Préprocesser les données
final_data, last_date = preprocess(initial_data, holiday=None, level=None)

# Entraîner les modèles
arima_model = train_arima(final_data)
xgboost_model = train_xgboost(final_data)

# Faire des prévisions
predictions_arima = forecast(arima_model, n_periods=3*365)
predictions_xgboost = forecast_xgboost(xgboost_model, last_date, n_periods= 3*365)

# Concaténer les résultats
result = concat(final_data, predictions_arima, predictions_xgboost)

# Tracer les résultats et les erreurs de prédiction
fig, fig_error = plot_results_and_errors(initial_data, comparison_data, result)


customer_type = ["Normal", "Member"]
gender = ["Male", "Female"]
city = ["Bangkok", "Chiang Mai", "Vientiane", "Luang Prabang"]
print(result.head())



with tgb.Page() as Visualisation:
    tgb.chart(figure="{create_bar_figure(data, 'Date')}")
    tgb.chart(figure="{plot_total_sales_distribution(data)}")
    tgb.chart(figure="{fig}")
    tgb.chart(figure="{fig_error}")