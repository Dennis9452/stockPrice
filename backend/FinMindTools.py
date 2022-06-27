from pathlib import Path

from flask import Flask, render_template, request
from loguru import logger
from pyecharts.charts import Page

import FinMind
from FinMind import plotting
from FinMind.data import DataLoader
class FinMind():
    def __init__(self):
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMi0wNi0wNCAxNzoxMzozMSIsInVzZXJfaWQiOiJEZW5uaXNUc2FpIiwiaXAiOiIyMjMuMTM3LjgyLjIxOSJ9.s6J7ChAYKZN3XcyBfzDwX0-JSkEdA8R6T_EJDi7yUU0"
        self.api_client = HttpClient(api_token=self.token)

    def kline(data_loader: DataLoader, stock_id: str, start_date: str, end_date: str):
        stock_data = data_loader.taiwan_stock_daily(stock_id, start_date, end_date)
        stock_data = data_loader.feature.add_kline_institutional_investors(
            stock_data
        )
        stock_data = data_loader.feature.add_kline_margin_purchase_short_sale(
            stock_data
        )
        # 繪製k線圖
        kline_plot = plotting.kline(stock_data)
        return kline_plot

    def bar(data_loader: DataLoader, stock_id: str, start_date: str, end_date: str):
        df = data_loader.taiwan_stock_month_revenue(
            stock_id=stock_id, start_date=start_date, end_date=end_date
        )
        df["labels"] = (
            df[["revenue_year", "revenue_month"]]
            .astype(str)
            .apply(lambda date: f"{date[0]}-{date[1]}M", axis=1)
        )
        df["series"] = df["revenue"].map(lambda value: round(value * 1e-8, 2))
        bar_plot = plotting.bar(
            labels=df["labels"],
            series=df["series"],
            title="月營收",
            yaxis_color="orange",
            y_axis_name="億",
        )
        return bar_plot

    def line(data_loader: DataLoader, stock_id: str, start_date: str, end_date: str):
        df = data_loader.taiwan_stock_shareholding(
            stock_id=stock_id, start_date=start_date, end_date=end_date
        )
        df["series"] = df["ForeignInvestmentSharesRatio"].map(
            lambda value: round(value * 1e-2, 2)
        )
        df["labels"] = df["date"]
        line_plot = plotting.line(
            labels=df["labels"],
            series=df["series"],
            title="外資持股比例",
            yaxis_color="blue",
            y_axis_name="",
        )
        return line_plot
