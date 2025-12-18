import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import json

# --------------------------------------------------
# Configurações iniciais
# --------------------------------------------------

# Diretório onde está o arquivo ETL
BASE_DIR = Path(__file__).resolve().parent
print(f"Executando ETL em: {BASE_DIR}")

# Carrega variáveis de ambiente
load_dotenv()

DATASET_PATH = os.environ.get("DATASET_PATH")

if not DATASET_PATH:
    raise EnvironmentError("Variável de ambiente DATASET_PATH não definida")

DATASET_FILE = Path(DATASET_PATH) / "olist_orders_dataset.csv"

if not DATASET_FILE.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {DATASET_FILE}")

# --------------------------------------------------
# Leitura do dataset
# --------------------------------------------------

df = pd.read_csv(
    DATASET_FILE,
    parse_dates=[
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)

# --------------------------------------------------
# Métricas iniciais
# --------------------------------------------------

total_orders = df["order_id"].nunique()
unique_customers = df["customer_id"].nunique()

orders_by_status = df["order_status"].value_counts().to_dict()

delivered_orders = orders_by_status.get("delivered", 0)
canceled_orders = orders_by_status.get("canceled", 0)

delivery_rate = round(delivered_orders / total_orders, 4) if total_orders > 0 else 0
cancellation_rate = round(canceled_orders / total_orders, 4) if total_orders > 0 else 0

# --------------------------------------------------
# Métricas de tempo (apenas pedidos entregues)
# --------------------------------------------------

delivered_df = df[df["order_status"] == "delivered"].copy()

# Tempo de aprovação (horas)
delivered_df["approval_time_hours"] = (
    delivered_df["order_approved_at"] - delivered_df["order_purchase_timestamp"]
).dt.total_seconds() / 3600

# Tempo até envio (dias)
delivered_df["shipping_time_days"] = (
    delivered_df["order_delivered_carrier_date"] - delivered_df["order_approved_at"]
).dt.days

# Tempo de entrega ao cliente (dias)
delivered_df["delivery_time_days"] = (
    delivered_df["order_delivered_customer_date"] - delivered_df["order_delivered_carrier_date"]
).dt.days

# Tempo total do pedido (dias)
delivered_df["total_order_time_days"] = (
    delivered_df["order_delivered_customer_date"] - delivered_df["order_purchase_timestamp"]
).dt.days

time_metrics = {
    "average_approval_time_hours": round(delivered_df["approval_time_hours"].mean(), 2),
    "average_shipping_time_days": round(delivered_df["shipping_time_days"].mean(), 2),
    "average_delivery_time_days": round(delivered_df["delivery_time_days"].mean(), 2),
    "average_total_order_time_days": round(delivered_df["total_order_time_days"].mean(), 2)
}

# --------------------------------------------------
# Performance de entrega
# --------------------------------------------------

delivered_df["delivery_delay_days"] = (
    delivered_df["order_delivered_customer_date"]
    - delivered_df["order_estimated_delivery_date"]
).dt.days

on_time_deliveries = int((delivered_df["delivery_delay_days"] <= 0).sum())
late_deliveries = int((delivered_df["delivery_delay_days"] > 0).sum())

on_time_rate = (
    round(on_time_deliveries / delivered_orders, 4)
    if delivered_orders > 0 else 0
)

avg_delay = delivered_df.loc[
    delivered_df["delivery_delay_days"] > 0,
    "delivery_delay_days"
].mean()

delivery_performance = {
    "on_time_deliveries": on_time_deliveries,
    "late_deliveries": late_deliveries,
    "on_time_rate": on_time_rate,
    "average_delay_days": round(avg_delay, 2) if pd.notna(avg_delay) else 0
}

# --------------------------------------------------
# Métricas ao longo do tempo
# --------------------------------------------------

df["order_date"] = df["order_purchase_timestamp"].dt.date

orders_per_day = df.groupby("order_date")["order_id"].count()

orders_over_time = {
    "orders_per_day_avg": round(orders_per_day.mean(), 2),
    "peak_day": str(orders_per_day.idxmax()),
    "peak_day_orders": int(orders_per_day.max())
}

# --------------------------------------------------
# Montagem do JSON final
# --------------------------------------------------

metrics_json = {
    "dataset": "olist_orders_dataset",
    "generated_at": datetime.utcnow().isoformat(),
    "metrics": {
        "orders": {
            "total_orders": total_orders,
            "unique_customers": unique_customers,
            "orders_by_status": orders_by_status,
            "delivery_rate": delivery_rate,
            "cancellation_rate": cancellation_rate
        },
        "time_metrics": time_metrics,
        "delivery_performance": delivery_performance,
        "orders_over_time": orders_over_time
    }
}

# --------------------------------------------------
# Escrita do arquivo
# --------------------------------------------------

output_dir = BASE_DIR / "processed"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "metrics.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(metrics_json, f, ensure_ascii=False, indent=2)

print(f"Arquivo gerado com sucesso: {output_file}")
