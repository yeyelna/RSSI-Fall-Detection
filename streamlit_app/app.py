import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Wi-Fi RSSI Fall Detection System",
    page_icon="📶",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root {
        --bg: #f6f8fb;
        --card: #ffffff;
        --text: #172033;
        --muted: #667085;
        --line: #e7eaf0;
        --line-soft: #f1f4f8;
        --blue: #2563eb;
        --blue-soft: #eef5ff;
        --green: #17803d;
        --green-soft: #edf8f1;
        --red: #c62836;
        --red-soft: #fff2f3;
        --purple: #6941c6;
        --purple-soft: #f4f0ff;
        --shadow: 0 6px 18px rgba(16, 24, 40, 0.055);
        --radius: 14px;
    }
    * { box-sizing: border-box; }
    body {
        margin: 0;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
        background: var(--bg);
        color: var(--text);
        font-weight: 400;
        letter-spacing: -0.006em;
    }
    .dashboard {
        width: 100%;
        max-width: 1480px;
        margin: 0 auto;
        padding: 16px;
    }
    .card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
    }
    .header-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 18px;
        padding: 18px 20px;
        margin-bottom: 16px;
    }
    .header-title {
        margin: 0;
        font-size: clamp(1.16rem, 1.8vw, 1.58rem);
        line-height: 1.2;
        font-weight: 680;
        letter-spacing: -0.025em;
    }
    .header-subtitle {
        margin: 7px 0 0;
        font-size: 0.9rem;
        color: var(--muted);
        font-weight: 400;
    }
    .status-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(132px, 1fr));
        gap: 10px;
        width: min(590px, 100%);
    }
    .status-card {
        min-height: 62px;
        padding: 10px 12px;
        border-radius: 12px;
        border: 1px solid var(--line);
        background: #fcfdff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 4px;
    }
    .status-label {
        color: var(--muted);
        font-size: 0.68rem;
        font-weight: 560;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .status-value {
        font-size: 0.84rem;
        font-weight: 620;
        word-break: break-word;
        color: var(--text);
    }
    .status-connected {
        background: var(--green-soft);
        border-color: #ccebd5;
    }
    .status-connected .status-value { color: var(--green); }
    .status-disconnected {
        background: var(--red-soft);
        border-color: #f4c4ca;
    }
    .status-disconnected .status-value { color: var(--red); }
    .section-title {
        margin: 0 0 14px;
        font-size: 0.98rem;
        font-weight: 500;
        letter-spacing: -0.015em;
        color: #111827;
    }
    .first-row {
        display: grid;
        grid-template-columns: minmax(250px, 0.88fr) minmax(390px, 1.78fr) minmax(290px, 1fr);
        gap: 16px;
        margin-bottom: 16px;
        align-items: stretch;
    }
    .second-row {
        display: grid;
        grid-template-columns: minmax(350px, 1fr) minmax(350px, 1fr);
        gap: 16px;
        margin-bottom: 16px;
    }
    .panel {
        padding: 18px;
        min-width: 0;
    }
    label {
        display: block;
        margin-bottom: 7px;
        color: #3b4658;
        font-size: 0.82rem;
        font-weight: 560;
    }
    input[type="text"] {
        width: 100%;
        border: 1px solid #d7dce5;
        border-radius: 10px;
        padding: 10px 12px;
        color: var(--text);
        background: white;
        font-size: 0.92rem;
        outline: none;
        font-weight: 400;
    }
    input[type="text"]:focus {
        border-color: #8fb3ff;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.10);
    }
    .button {
        width: 100%;
        margin-top: 11px;
        border-radius: 10px;
        padding: 10px 13px;
        font-size: 0.88rem;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.12s ease, opacity 0.12s ease, background 0.12s ease, border-color 0.12s ease;
    }
    .button:active { transform: scale(0.99); }
    .button-primary {
        border: 1px solid var(--blue);
        background: var(--blue);
        color: white;
    }
    .button-primary:hover { background: #1d4ed8; }
    .button-secondary {
        border: 1px solid #bcd2ff;
        background: #f8fbff;
        color: var(--blue);
    }
    .button-secondary:hover { background: var(--blue-soft); }
    .button-danger-lite {
        width: auto;
        margin: 0;
        background: transparent;
        color: var(--red);
        padding: 7px 9px;
        border: 1px solid transparent;
        font-weight: 560;
    }
    .button-danger-lite:hover {
        border-color: #f3c2c8;
        background: var(--red-soft);
    }
    .button:disabled {
        opacity: 0.55;
        cursor: not-allowed;
    }
    .divider {
        height: 1px;
        background: var(--line-soft);
        margin: 20px 0;
    }
    .upload-box {
        position: relative;
        border: 1px dashed #c9d1df;
        border-radius: 12px;
        background: #fcfdff;
        min-height: 108px;
        display: grid;
        place-items: center;
        text-align: center;
        padding: 16px;
        cursor: pointer;
        color: var(--muted);
        overflow: hidden;
    }
    .upload-box:hover { border-color: #8fb3ff; background: #f8fbff; }
    .upload-box input {
        position: absolute;
        inset: 0;
        opacity: 0;
        cursor: pointer;
    }
    .upload-icon {
        display: none;
    }
    .upload-main {
        color: #344054;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .upload-sub {
        color: var(--muted);
        font-size: 0.76rem;
        margin-top: 4px;
    }
    .helper-text {
        margin-top: 8px;
        color: var(--muted);
        font-size: 0.8rem;
        word-break: break-word;
        font-weight: 400;
    }
    .signal-card {
        min-height: 390px;
        display: flex;
        flex-direction: column;
    }
    .chart-wrap {
        flex: 1;
        min-height: 300px;
        background: #fff;
        border-radius: 12px;
        border: 1px solid var(--line-soft);
        padding: 10px;
        position: relative;
    }
    .placeholder {
        height: 100%;
        min-height: 270px;
        display: grid;
        place-items: center;
        color: var(--muted);
        text-align: center;
        border: 1px dashed #d8dee8;
        border-radius: 12px;
        background: #fcfdff;
        padding: 20px;
        font-weight: 400;
    }
    .result-card { min-height: 390px; }
    .current-file {
        margin-top: -5px;
        margin-bottom: 13px;
        color: #576171;
        font-size: 0.82rem;
        font-weight: 400;
    }
    .result-box {
        border-radius: 12px;
        padding: 14px 15px;
        font-size: 0.98rem;
        font-weight: 500;
        letter-spacing: 0;
        display: flex;
        align-items: center;
        gap: 9px;
        margin-bottom: 14px;
        border: 1px solid;
    }
    .fall-box {
        color: var(--red);
        background: var(--red-soft);
        border-color: #f0b9c0;
    }
    .normal-box {
        color: var(--green);
        background: var(--green-soft);
        border-color: #bfdfc9;
    }
    .invalid-box {
        color: #596579;
        background: #f8fafc;
        border-color: #d7dce5;
        align-items: flex-start;
        flex-direction: column;
        gap: 5px;
        letter-spacing: 0;
        font-weight: 500;
    }
    .invalid-box strong {
        color: #2f3a4a;
        font-weight: 620;
    }
    .metric-list { display: grid; gap: 9px; }
    .metric-row {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        padding-bottom: 9px;
        border-bottom: 1px solid var(--line-soft);
        font-size: 0.86rem;
    }
    .metric-row:last-child { border-bottom: none; }
    .metric-label {
        color: var(--muted);
        font-weight: 500;
    }
    .metric-value {
        color: var(--text);
        font-weight: 620;
        text-align: right;
    }
    .alert-note {
        margin-top: 13px;
        border-radius: 12px;
        padding: 11px 12px;
        font-weight: 600;
        font-size: 0.84rem;
        border: 1px solid;
    }
    .alert-note small {
        display: block;
        margin-top: 3px;
        font-weight: 400;
    }
    .alert-note.red {
        color: var(--red);
        background: var(--red-soft);
        border-color: #f4c4ca;
    }
    .alert-note.green {
        color: var(--green);
        background: var(--green-soft);
        border-color: #ccebd5;
    }
    .message {
        margin-top: 11px;
        border-radius: 10px;
        padding: 10px 11px;
        font-size: 0.82rem;
        font-weight: 500;
    }
    .message.error {
        background: var(--red-soft);
        color: var(--red);
        border: 1px solid #f4c4ca;
    }
    .message.info {
        background: var(--blue-soft);
        color: var(--blue);
        border: 1px solid #cfe0ff;
    }
    .flow-horizontal {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        flex-wrap: wrap;
        padding: 12px 4px 6px;
    }
    .flow-step {
        min-width: 86px;
        max-width: 112px;
        text-align: center;
        display: grid;
        justify-items: center;
        gap: 7px;
    }
    .flow-icon {
        width: 34px;
        height: 34px;
        border-radius: 10px;
        display: grid;
        place-items: center;
        font-size: 0.72rem;
        background: #f8fbff;
        color: var(--blue);
        border: 1px solid #d6e4ff;
        font-weight: 500;
        letter-spacing: 0.02em;
    }
    .flow-label {
        font-size: 0.73rem;
        color: #344054;
        font-weight: 520;
        line-height: 1.22;
    }
    .flow-arrow {
        color: #b0b7c3;
        font-weight: 400;
        font-size: 0.85rem;
    }
    .flow-vertical { display: none; }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 11px;
    }
    .info-item {
        border: 1px solid var(--line-soft);
        background: #fcfdff;
        border-radius: 12px;
        padding: 11px 12px;
        min-width: 0;
    }
    .info-label {
        font-size: 0.72rem;
        color: var(--muted);
        font-weight: 560;
        margin-bottom: 5px;
    }
    .info-value {
        font-size: 0.86rem;
        font-weight: 620;
        word-break: break-word;
    }
    .info-value.secondary {
        color: #4b5565;
        font-weight: 520;
        font-size: 0.84rem;
    }
    .history-card {
        padding: 18px;
        margin-bottom: 22px;
    }
    .history-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 14px;
        margin-bottom: 13px;
    }
    .history-actions {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        flex-wrap: wrap;
    }
    .history-actions .button {
        width: auto;
        margin: 0;
        padding: 8px 10px;
        font-size: 0.8rem;
    }
    .table-wrap {
        width: 100%;
        overflow-x: auto;
        border: 1px solid var(--line-soft);
        border-radius: 12px;
    }
    table {
        width: 100%;
        min-width: 920px;
        border-collapse: collapse;
        background: white;
    }
    th, td {
        padding: 11px 12px;
        border-bottom: 1px solid var(--line-soft);
        text-align: left;
        vertical-align: middle;
        font-size: 0.78rem;
        white-space: nowrap;
        font-weight: 400;
    }
    th {
        color: #5f6b7a;
        background: #fbfcfe;
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 0.035em;
        font-weight: 600;
    }
    tr:last-child td { border-bottom: 0; }
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        border-radius: 999px;
        padding: 4px 8px;
        font-size: 0.72rem;
        font-weight: 560;
        border: 1px solid transparent;
    }
    .badge-fall, .badge-alert {
        color: var(--red);
        background: var(--red-soft);
        border-color: #f4c4ca;
    }
    .badge-normal, .badge-low {
        color: var(--green);
        background: var(--green-soft);
        border-color: #ccebd5;
    }
    .badge-high {
        color: var(--red);
        background: var(--red-soft);
        border-color: #f4c4ca;
    }
    .badge-manual, .badge-live {
        color: var(--purple);
        background: var(--purple-soft);
        border-color: #d7c9fb;
    }
    .loading {
        position: relative;
        opacity: 0.78;
        pointer-events: none;
    }
    .tiny-loader {
        display: inline-block;
        width: 12px;
        height: 12px;
        border: 2px solid rgba(37, 99, 235, 0.20);
        border-top-color: var(--blue);
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
        vertical-align: -2px;
        margin-right: 6px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    @media (max-width: 1050px) {
        .header-card {
            align-items: flex-start;
            flex-direction: column;
        }
        .status-grid { width: 100%; }
        .first-row { grid-template-columns: 1fr; }
        .input-panel { order: 1; }
        .result-card { order: 2; }
        .signal-card { order: 3; }
        .second-row { grid-template-columns: 1fr; }
    }
    @media (max-width: 768px) {
        .dashboard { padding: 10px; }
        .header-card, .panel, .history-card { padding: 15px; }
        .status-grid { grid-template-columns: 1fr; }
        .first-row, .second-row {
            gap: 12px;
            margin-bottom: 12px;
        }
        .button, .history-actions .button { width: 100%; }
        .history-header {
            align-items: stretch;
            flex-direction: column;
        }
        .history-actions {
            width: 100%;
            flex-direction: column;
        }
        .flow-horizontal { display: none; }
        .flow-vertical {
            display: grid;
            gap: 8px;
        }
        .vertical-step {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 9px 11px;
            border: 1px solid var(--line-soft);
            border-radius: 11px;
            background: #fcfdff;
            font-weight: 520;
        }
        .step-number {
            width: 26px;
            height: 26px;
            border-radius: 8px;
            background: #f8fbff;
            color: var(--blue);
            border: 1px solid #d6e4ff;
            display: grid;
            place-items: center;
            font-weight: 620;
            flex: 0 0 auto;
            font-size: 0.78rem;
        }
        .info-grid { grid-template-columns: 1fr; }
        .chart-wrap { min-height: 260px; }
        .placeholder { min-height: 230px; }
        table { min-width: 850px; }
        th, td { padding: 10px 10px; }
    }
</style>
    """,
    unsafe_allow_html=True,
)

DASHBOARD_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Wi-Fi RSSI Fall Detection System</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
    @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;650;700&display=swap");

    :root {
        --bg: #f8fafc;
        --card: #ffffff;
        --text: #111827;
        --muted: #6b7280;
        --soft-muted: #94a3b8;
        --line: #e5e7eb;
        --line-soft: #f1f5f9;
        --blue: #2563eb;
        --blue-soft: #eff6ff;
        --green: #16a34a;
        --green-soft: #f0fdf4;
        --red: #dc2626;
        --red-soft: #fff1f2;
        --purple: #7c3aed;
        --purple-soft: #f5f3ff;
        --slate-soft: #f8fafc;
        --shadow: 0 3px 12px rgba(15, 23, 42, 0.045);
        --radius: 12px;
    }
    * { box-sizing: border-box; }
    body {
        margin: 0;
        font-family: "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: var(--bg);
        color: var(--text);
        font-size: 13px;
        font-weight: 400;
        letter-spacing: -0.006em;
        text-rendering: geometricPrecision;
    }
    .dashboard {
        width: 100%;
        max-width: 1540px;
        margin: 0 auto;
        padding: 16px;
    }
    .card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
    }
    .header-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 18px;
        padding: 18px 20px;
        margin-bottom: 16px;
    }
    .header-title {
        margin: 0;
        font-size: clamp(1.08rem, 1.45vw, 1.36rem);
        line-height: 1.2;
        font-weight: 500;
        letter-spacing: -0.025em;
    }
    .header-subtitle {
        margin: 7px 0 0;
        font-size: 0.82rem;
        line-height: 1.45;
        color: var(--muted);
        font-weight: 400;
    }
    .status-grid {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 9px;
        flex-wrap: wrap;
        max-width: 620px;
    }
    .status-card {
        min-height: 34px;
        padding: 7px 10px;
        border-radius: 9px;
        border: 1px solid var(--line);
        background: #fbfdff;
        display: inline-flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        gap: 7px;
        white-space: nowrap;
    }
    .status-icon {
        width: 16px;
        height: 16px;
        border-radius: 999px;
        display: inline-grid;
        place-items: center;
        flex: 0 0 auto;
        font-size: 0.67rem;
        line-height: 1;
        font-weight: 500;
    }
    .status-label { display: none; }
    .status-value {
        font-size: 0.76rem;
        line-height: 1;
        font-weight: 500;
        letter-spacing: -0.01em;
        word-break: normal;
    }
    .status-connected {
        background: var(--green-soft);
        border-color: #bbf7d0;
        color: #047857;
    }
    .status-connected .status-icon {
        background: #dcfce7;
        color: #047857;
        border: 1px solid #86efac;
    }
    .status-disconnected {
        background: var(--red-soft);
        border-color: #fecdd3;
        color: var(--red);
    }
    .status-disconnected .status-icon {
        background: #ffe4e6;
        color: var(--red);
        border: 1px solid #fda4af;
    }
    .status-model {
        background: var(--blue-soft);
        border-color: #bfdbfe;
        color: #1d4ed8;
    }
    .status-model .status-icon {
        background: #dbeafe;
        color: #1d4ed8;
        border: 1px solid #93c5fd;
        border-radius: 5px;
    }
    .status-time {
        background: var(--slate-soft);
        border-color: #e2e8f0;
        color: #475569;
    }
    .status-time .status-icon {
        background: #f1f5f9;
        color: #475569;
        border: 1px solid #cbd5e1;
    }
    .section-title {
        margin: 0 0 14px;
        font-size: 0.9rem;
        line-height: 1.2;
        font-weight: 500;
        letter-spacing: -0.015em;
    }
    .first-row {
        display: grid;
        grid-template-columns: minmax(250px, 0.9fr) minmax(390px, 1.8fr) minmax(290px, 1fr);
        gap: 16px;
        margin-bottom: 16px;
        align-items: stretch;
    }
    .second-row {
        display: grid;
        grid-template-columns: minmax(350px, 1fr) minmax(350px, 1fr);
        gap: 16px;
        margin-bottom: 16px;
    }
    .panel {
        padding: 18px;
        min-width: 0;
    }
    label {
        display: block;
        margin-bottom: 7px;
        color: #334155;
        font-size: 0.74rem;
        font-weight: 500;
    }
    input[type="text"] {
        width: 100%;
        border: 1px solid #d8dee8;
        border-radius: 9px;
        padding: 10px 11px;
        color: var(--text);
        background: white;
        font-size: 0.82rem;
        font-weight: 400;
        outline: none;
    }
    input[type="text"]:focus {
        border-color: #93c5fd;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.09);
    }
    .button {
        width: 100%;
        margin-top: 11px;
        border: 0;
        border-radius: 9px;
        padding: 10px 12px;
        font-size: 0.78rem;
        font-weight: 500;
        cursor: pointer;
        transition: transform 0.15s ease, opacity 0.15s ease, background 0.15s ease, border 0.15s ease;
    }
    .button:active { transform: scale(0.99); }
    .button-primary { background: var(--blue); color: white; }
    .button-primary:hover { background: #1d4ed8; }
    .button-secondary {
        background: #ffffff;
        color: var(--blue);
        border: 1px solid #bfdbfe;
    }
    .button-secondary:hover { background: var(--blue-soft); }
    .button-danger-lite {
        width: auto;
        margin: 0;
        background: transparent;
        color: var(--red);
        padding: 7px 9px;
        border: 1px solid transparent;
        font-weight: 500;
    }
    .button-danger-lite:hover {
        border-color: #fecdd3;
        background: var(--red-soft);
    }
    .button:disabled {
        opacity: 0.55;
        cursor: not-allowed;
    }
    .divider {
        height: 1px;
        background: var(--line-soft);
        margin: 20px 0;
    }
    .upload-box {
        position: relative;
        border: 1.5px dashed #d5dbe5;
        border-radius: 11px;
        background: #fcfdff;
        min-height: 112px;
        display: grid;
        place-items: center;
        text-align: center;
        padding: 16px;
        cursor: pointer;
        color: var(--muted);
        overflow: hidden;
    }
    .upload-box:hover {
        border-color: #bfdbfe;
        background: #f8fbff;
    }
    .upload-box input {
        position: absolute;
        inset: 0;
        opacity: 0;
        cursor: pointer;
    }
    .upload-icon {
        font-size: 1.35rem;
        color: var(--soft-muted);
        line-height: 1;
        margin-bottom: 6px;
        font-weight: 400;
    }
    .upload-main {
        color: #334155;
        font-size: 0.8rem;
        font-weight: 500;
    }
    .upload-sub {
        color: var(--muted);
        font-size: 0.7rem;
        margin-top: 4px;
    }
    .helper-text {
        margin-top: 8px;
        color: var(--muted);
        font-size: 0.74rem;
        word-break: break-word;
    }
    .signal-card {
        min-height: 388px;
        display: flex;
        flex-direction: column;
    }
    .chart-wrap {
        flex: 1;
        min-height: 300px;
        background: #fff;
        border-radius: 11px;
        border: 1px solid #f1f5f9;
        padding: 10px;
        position: relative;
    }
    .placeholder {
        height: 100%;
        min-height: 270px;
        display: grid;
        place-items: center;
        color: var(--muted);
        text-align: center;
        border: 1px dashed #d8dee8;
        border-radius: 11px;
        background: #fcfdff;
        padding: 20px;
        font-size: 0.82rem;
        font-weight: 400;
    }
    .result-card { min-height: 388px; }
    .current-file {
        margin-top: -5px;
        margin-bottom: 13px;
        color: #64748b;
        font-size: 0.74rem;
        font-weight: 400;
    }
    .result-box {
        border-radius: 11px;
        padding: 15px;
        font-size: 0.94rem;
        font-weight: 500;
        letter-spacing: 0.01em;
        display: flex;
        align-items: center;
        gap: 9px;
        margin-bottom: 14px;
        border: 1px solid;
    }
    .fall-box {
        color: var(--red);
        background: var(--red-soft);
        border-color: #fda4af;
    }
    .normal-box {
        color: var(--green);
        background: var(--green-soft);
        border-color: #86efac;
    }
    .invalid-box {
        color: #475569;
        background: #f8fafc;
        border-color: #d8dee8;
        align-items: flex-start;
        flex-direction: column;
        gap: 5px;
        letter-spacing: 0;
    }
    .invalid-box strong {
        color: #334155;
        font-weight: 600;
    }
    .metric-list { display: grid; gap: 9px; }
    .metric-row {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid #f1f5f9;
        font-size: 0.8rem;
    }
    .metric-row:last-child { border-bottom: none; }
    .metric-label {
        color: var(--muted);
        font-weight: 500;
    }
    .metric-value {
        color: var(--text);
        font-weight: 600;
        text-align: right;
    }
    .alert-note {
        margin-top: 13px;
        border-radius: 11px;
        padding: 11px 12px;
        font-weight: 600;
        font-size: 0.78rem;
        border: 1px solid;
    }
    .alert-note small {
        display: block;
        margin-top: 3px;
        font-weight: 400;
    }
    .alert-note.red {
        color: var(--red);
        background: var(--red-soft);
        border-color: #fecdd3;
    }
    .alert-note.green {
        color: var(--green);
        background: var(--green-soft);
        border-color: #bbf7d0;
    }
    .message {
        margin-top: 11px;
        border-radius: 10px;
        padding: 10px 11px;
        font-size: 0.76rem;
        font-weight: 500;
    }
    .message.error {
        background: var(--red-soft);
        color: var(--red);
        border: 1px solid #fecdd3;
    }
    .message.info {
        background: var(--blue-soft);
        color: var(--blue);
        border: 1px solid #bfdbfe;
    }
    .flow-horizontal {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
        padding: 20px 6px 6px;
    }
    .flow-step {
        min-width: 82px;
        max-width: 108px;
        text-align: center;
        display: grid;
        justify-items: center;
        gap: 7px;
    }
    .flow-icon {
        width: 28px;
        height: 28px;
        display: grid;
        place-items: center;
        font-size: 1.05rem;
        font-weight: 600;
        background: transparent;
        border: 0;
    }
    .flow-step:nth-child(1) .flow-icon { color: #2563eb; }
    .flow-step:nth-child(3) .flow-icon { color: #06b6d4; }
    .flow-step:nth-child(5) .flow-icon { color: #a855f7; }
    .flow-step:nth-child(7) .flow-icon { color: #0ea5e9; }
    .flow-step:nth-child(9) .flow-icon { color: #7c3aed; }
    .flow-step:nth-child(11) .flow-icon { color: #dc2626; }
    .flow-label {
        font-size: 0.68rem;
        color: #475569;
        font-weight: 500;
        line-height: 1.2;
    }
    .flow-arrow {
        color: #cbd5e1;
        font-size: 0.82rem;
        font-weight: 500;
    }
    .flow-vertical { display: none; }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 12px;
    }
    .info-item {
        border: 1px solid #f1f5f9;
        background: #ffffff;
        border-radius: 11px;
        padding: 12px 13px;
        min-width: 0;
    }
    .info-label {
        font-size: 0.68rem;
        color: var(--muted);
        font-weight: 500;
        margin-bottom: 6px;
    }
    .info-value {
        font-size: 0.82rem;
        line-height: 1.3;
        font-weight: 600;
        word-break: break-word;
    }
    .info-value.secondary {
        color: #475569;
        font-weight: 500;
        font-size: 0.8rem;
    }
    .history-card {
        padding: 18px;
        margin-bottom: 22px;
    }
    .history-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 14px;
        margin-bottom: 14px;
    }
    .history-actions {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        flex-wrap: wrap;
    }
    .history-actions .button {
        width: auto;
        margin: 0;
        padding: 7px 9px;
        font-size: 0.74rem;
    }
    .table-wrap {
        width: 100%;
        overflow-x: auto;
        border: 1px solid #eef2f7;
        border-radius: 11px;
    }
    table {
        width: 100%;
        min-width: 1060px;
        border-collapse: collapse;
        background: white;
    }
    th, td {
        padding: 11px 12px;
        border-bottom: 1px solid #eef2f7;
        text-align: left;
        vertical-align: middle;
        font-size: 0.74rem;
        white-space: nowrap;
        font-weight: 400;
    }
    th {
        color: #64748b;
        background: #fbfdff;
        font-size: 0.66rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    tr:last-child td { border-bottom: 0; }
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        border-radius: 999px;
        padding: 4px 8px;
        font-size: 0.68rem;
        font-weight: 500;
        border: 1px solid transparent;
    }
    .badge-fall, .badge-alert {
        color: var(--red);
        background: var(--red-soft);
        border-color: #fecdd3;
    }
    .badge-normal, .badge-low {
        color: var(--green);
        background: var(--green-soft);
        border-color: #bbf7d0;
    }
    .badge-high {
        color: var(--red);
        background: var(--red-soft);
        border-color: #fecdd3;
    }
    .badge-manual, .badge-live {
        color: var(--purple);
        background: var(--purple-soft);
        border-color: #ddd6fe;
    }
    .loading {
        position: relative;
        opacity: 0.78;
        pointer-events: none;
    }
    .tiny-loader {
        display: inline-block;
        width: 11px;
        height: 11px;
        border: 2px solid rgba(37, 99, 235, 0.22);
        border-top-color: var(--blue);
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
        vertical-align: -2px;
        margin-right: 6px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    @media (max-width: 1050px) {
        .header-card {
            align-items: flex-start;
            flex-direction: column;
        }
        .status-grid {
            width: 100%;
            max-width: 100%;
            justify-content: flex-start;
        }
        .first-row { grid-template-columns: 1fr; }
        .input-panel { order: 1; }
        .result-card { order: 2; }
        .signal-card { order: 3; }
        .second-row { grid-template-columns: 1fr; }
    }
    @media (max-width: 768px) {
        .dashboard { padding: 10px; }
        .header-card, .panel, .history-card { padding: 15px; }
        .status-grid {
            display: grid;
            grid-template-columns: 1fr;
        }
        .status-card {
            justify-content: flex-start;
            width: 100%;
        }
        .first-row, .second-row {
            gap: 12px;
            margin-bottom: 12px;
        }
        .button, .history-actions .button { width: 100%; }
        .history-header {
            align-items: stretch;
            flex-direction: column;
        }
        .history-actions {
            width: 100%;
            flex-direction: column;
        }
        .flow-horizontal { display: none; }
        .flow-vertical {
            display: grid;
            gap: 8px;
        }
        .vertical-step {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 9px 11px;
            border: 1px solid #eef2f7;
            border-radius: 10px;
            background: #fcfdff;
            font-size: 0.8rem;
        }
        .step-number {
            width: 25px;
            height: 25px;
            border-radius: 8px;
            background: var(--blue-soft);
            color: var(--blue);
            display: grid;
            place-items: center;
            font-weight: 600;
            flex: 0 0 auto;
            font-size: 0.74rem;
        }
        .info-grid { grid-template-columns: 1fr; }
        .chart-wrap { min-height: 260px; }
        .placeholder { min-height: 230px; }
        table { min-width: 880px; }
        th, td { padding: 10px 10px; }
    }

    /* Figma-like lighter typography pass */
    body {
        font-family: "Inter", "Segoe UI", Arial, sans-serif;
        font-size: 13px;
        font-weight: 400;
        color: #0f172a;
    }

    .header-title {
        font-size: clamp(1.05rem, 1.35vw, 1.28rem);
        font-weight: 500;
    }

    .header-subtitle,
    .current-file,
    .helper-text {
        font-weight: 400;
    }

    .section-title {
        font-size: 0.92rem;
        font-weight: 500;
        letter-spacing: -0.01em;
    }

    label,
    .metric-label,
    .info-label {
        font-weight: 400;
        color: #52637a;
    }

    .status-value,
    .metric-value,
    .info-value {
        font-weight: 500;
        color: #0f172a;
    }

    .info-value.secondary {
        font-weight: 400;
        color: #7b8da8;
    }

    .info-item {
        background: #f8fafc;
        border-color: #eef2f7;
        box-shadow: none;
    }

    .result-box {
        font-weight: 500;
    }

    .alert-note {
        font-weight: 500;
    }

    .alert-note small {
        font-weight: 400;
    }

    th {
        font-weight: 500;
    }

    .badge {
        font-weight: 500;
    }

    .button {
        font-weight: 500;
    }

</style>
</head>
<body>
<div class="dashboard">
    <header class="header-card card">
        <div>
            <h1 class="header-title">Wi-Fi RSSI Fall Detection System</h1>
            <p class="header-subtitle">A Wi-Fi RSSI-based system for classifying human activity as Fall or Non-Fall</p>
        </div>
        <div class="status-grid">
            <div id="backendStatusCard" class="status-card status-connected">
                <span id="backendIcon" class="status-icon">✓</span>
                <span id="backendStatus" class="status-value">Checking...</span>
            </div>
            <div class="status-card status-model">
                <span class="status-icon">▣</span>
                <span id="modelStatus" class="status-value">Model: MTFF</span>
            </div>
            <div class="status-card status-time">
                <span class="status-icon">◷</span>
                <span id="lastClassification" class="status-value">Last: Loading...</span>
            </div>
        </div>
    </header>

    <main>
        <section class="first-row">
            <article class="card panel input-panel" id="inputPanel">
                <h2 class="section-title">Input Panel</h2>

                <label for="filenameInput">Enter Filename</label>
                <input id="filenameInput" type="text" value="data31.mat" placeholder="data31.mat" />
                <button id="classifyBtn" class="button button-primary" onclick="classifyByFilename()">Classify by Filename</button>
                <div id="filenameMessage"></div>

                <div class="divider"></div>

                <label for="fileUpload">Upload .mat File</label>
                <div class="upload-box">
                    <input id="fileUpload" type="file" accept=".mat" onchange="handleFileSelect()" />
                    <div>
                        <div class="upload-icon"></div>
                        <div class="upload-main">Click to browse</div>
                        <div class="upload-sub">Accepted: .mat</div>
                    </div>
                </div>
                <div id="selectedFileName" class="helper-text">No file selected</div>
                <button id="uploadBtn" class="button button-secondary" onclick="uploadAndClassify()">Upload and Classify</button>
                <div id="uploadMessage"></div>
            </article>

            <article class="card panel signal-card">
                <h2 class="section-title">RSSI Signal Preview</h2>
                <div id="chartContainer" class="chart-wrap">
                    <div id="signalPlaceholder" class="placeholder">Signal preview available after file upload</div>
                    <canvas id="rssiChart" style="display:none;"></canvas>
                </div>
            </article>

            <article class="card panel result-card">
                <h2 class="section-title">Classification Result</h2>
                <div id="currentFile" class="current-file">Current file: None</div>
                <div id="resultContent">
                    <div class="result-box invalid-box">
                        <strong>No valid classification result</strong>
                        <span>Please choose a test file.</span>
                    </div>
                </div>
            </article>
        </section>

        <section class="second-row">
            <article class="card panel">
                <h2 class="section-title">System Processing Flow</h2>
                <div class="flow-horizontal" aria-label="System processing flow">
                    <div class="flow-step"><div class="flow-icon">01</div><div class="flow-label">MATLAB .mat File</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">02</div><div class="flow-label">RSSI Signal</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">03</div><div class="flow-label">FFT + STFT + CWT</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">04</div><div class="flow-label">MTFF</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">05</div><div class="flow-label">LightGBM Model</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">06</div><div class="flow-label">Fall / Non-Fall</div></div>
                </div>
                <div class="flow-vertical">
                    <div class="vertical-step"><span class="step-number">1</span><strong>MATLAB .mat File</strong></div>
                    <div class="vertical-step"><span class="step-number">2</span><strong>RSSI Signal</strong></div>
                    <div class="vertical-step"><span class="step-number">3</span><strong>FFT + STFT + CWT</strong></div>
                    <div class="vertical-step"><span class="step-number">4</span><strong>MTFF</strong></div>
                    <div class="vertical-step"><span class="step-number">5</span><strong>LightGBM Model</strong></div>
                    <div class="vertical-step"><span class="step-number">6</span><strong>Fall / Non-Fall</strong></div>
                </div>
            </article>

            <article class="card panel">
                <h2 class="section-title">Technical Model Info</h2>
                <div id="modelInfoGrid" class="info-grid">
                    <div class="info-item"><div class="info-label">Model</div><div class="info-value">MTFF</div></div>
                    <div class="info-item"><div class="info-label">Internal model</div><div class="info-value secondary">Balanced_COMB</div></div>
                    <div class="info-item"><div class="info-label">Classifier</div><div class="info-value">LightGBM</div></div>
                    <div class="info-item"><div class="info-label">Feature Method</div><div class="info-value">Multi-Transform Feature Fusion</div></div>
                    <div class="info-item"><div class="info-label">Feature Order</div><div class="info-value">FFT + STFT + CWT</div></div>
                    <div class="info-item"><div class="info-label">Input Features</div><div class="info-value">384</div></div>
                    <div class="info-item"><div class="info-label">Selected Features</div><div class="info-value">208</div></div>
                    <div class="info-item"><div class="info-label">Decision Threshold</div><div class="info-value">0.79</div></div>
                    <div class="info-item"><div class="info-label">Classification Type</div><div class="info-value">Binary Classification</div></div>
                </div>
            </article>
        </section>

        <section class="history-card card">
            <div class="history-header">
                <h2 class="section-title" style="margin:0;">Recent Detection Events</h2>
                <div class="history-actions">
                    <button id="clearManualBtn" class="button button-danger-lite" onclick="clearManualTests()">Clear Manual Tests</button>
                    <button id="clearAllBtn" class="button button-danger-lite" onclick="clearAllHistory()">Clear All History</button>
                </div>
            </div>
            <div id="historyMessage"></div>
            <div id="historyContainer" class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>File Name</th>
                            <th>Classified Activity</th>
                            <th>Fall Confidence</th>
                            <th>Risk Level</th>
                            <th>Input Mode</th>
                            <th>Processing Time</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="historyBody">
                        <tr><td colspan="9">Loading history...</td></tr>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
</div>

<script>
const API_BASE_URL = "https://wi-fi-rssi-fall-detection-system.onrender.com";

let state = {
    modelInfo: null,
    history: [],
    currentResult: null,
    currentFile: null,
    selectedFile: null,
    chart: null,
    loading: false
};

function friendlyErrorMessage() {
    return "File not supported for fast classification. Please choose a test file from the prepared dataset.";
}

function setMessage(targetId, message, type = "info") {
    const el = document.getElementById(targetId);
    if (!el) return;
    if (!message) {
        el.innerHTML = "";
        return;
    }
    el.innerHTML = `<div class="message ${type}">${message}</div>`;
}

function setLoading(buttonId, isLoading, loadingText = "Loading...") {
    const btn = document.getElementById(buttonId);
    if (!btn) return;
    if (isLoading) {
        btn.dataset.originalText = btn.textContent;
        btn.innerHTML = `<span class="tiny-loader"></span>${loadingText}`;
        btn.disabled = true;
    } else {
        btn.textContent = btn.dataset.originalText || btn.textContent;
        btn.disabled = false;
    }
}

async function safeFetch(url, options = {}) {
    const response = await fetch(url, options);
    if (!response.ok) {
        throw new Error("Request failed");
    }
    const text = await response.text();
    if (!text) return {};
    try {
        return JSON.parse(text);
    } catch {
        return {};
    }
}

function normalizeActivity(value) {
    if (value === undefined || value === null) return "";
    const text = String(value).trim();
    const lower = text.toLowerCase().replace(/_/g, "-");
    if (lower.includes("non-fall") || lower.includes("nonfall") || lower.includes("normal")) return "Non-Fall";
    if (lower.includes("fall")) return "Fall";
    return text;
}

function isFallActivity(activity) {
    return normalizeActivity(activity) === "Fall";
}

function formatPercent(value) {
    if (value === undefined || value === null || value === "") return "—";
    if (typeof value === "string" && value.includes("%")) return value.trim();
    const numeric = Number(value);
    if (Number.isNaN(numeric)) return String(value);
    const percent = numeric <= 1 ? numeric * 100 : numeric;
    return `${percent.toFixed(1)}%`;
}

function getFallConfidence(data) {
    if (!data) return null;
    return (
        data.fall_confidence_percent ??
        data.fall_confidence ??
        data.fall_probability ??
        data.probability ??
        data.confidence ??
        data.score ??
        null
    );
}

function formatSeconds(value) {
    if (value === undefined || value === null || value === "") return "—";
    if (typeof value === "string" && value.endsWith("s")) return value;
    const numeric = Number(value);
    if (Number.isNaN(numeric)) return String(value);
    if (numeric < 1) return `${numeric.toFixed(3)}s`;
    return `${numeric.toFixed(2)}s`;
}

function cleanThreshold(value) {
    const fallback = getModelField(["decision_threshold", "threshold"], 0.79);
    const raw = value ?? fallback;
    const numeric = Number(raw);
    if (Number.isNaN(numeric)) return String(raw);
    return numeric.toFixed(2);
}

function formatMalaysiaTimestamp(value) {
    if (!value) return "—";
    const raw = String(value).trim();

    if (!raw.includes("T") && !raw.includes("+") && !raw.endsWith("Z")) {
        const compact = raw.replace(/\.\d+$/, "");
        return compact.length >= 19 ? compact.slice(0, 19) : compact;
    }

    const date = new Date(raw);
    if (!Number.isNaN(date.getTime())) {
        const parts = new Intl.DateTimeFormat("en-CA", {
            timeZone: "Asia/Kuala_Lumpur",
            year: "numeric",
            month: "2-digit",
            day: "2-digit",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: false
        }).formatToParts(date);

        const get = (type) => parts.find(p => p.type === type)?.value || "";
        return `${get("year")}-${get("month")}-${get("day")} ${get("hour")}:${get("minute")}:${get("second")}`;
    }

    return raw.replace("T", " ").replace(/\+08:00$/, "").replace(/Z$/, "").slice(0, 19);
}

function getRecordTimestamp(record) {
    return record?.timestamp_display || record?.timestamp || "";
}

function getLatestHistoryRecord(records) {
    if (!Array.isArray(records) || records.length === 0) return null;
    let latest = records[0];
    let latestTime = Date.parse(records[0].timestamp || records[0].timestamp_display || "");
    for (const record of records) {
        const parsed = Date.parse(record.timestamp || record.timestamp_display || "");
        if (!Number.isNaN(parsed) && (Number.isNaN(latestTime) || parsed > latestTime)) {
            latest = record;
            latestTime = parsed;
        }
    }
    return latest;
}

function getModelField(keys, fallback) {
    const info = state.modelInfo || {};
    for (const key of keys) {
        if (info[key] !== undefined && info[key] !== null && info[key] !== "") return info[key];
    }
    return fallback;
}

function sanitizeFeatureOrder(value) {
    if (!value) return "FFT + STFT + CWT";
    return String(value)
        .replace(/FFT_128/gi, "FFT")
        .replace(/STFT_128/gi, "STFT")
        .replace(/CWT_128/gi, "CWT")
        .replace(/\s*\+\s*/g, " + ");
}

function renderModelInfo() {
    const threshold = cleanThreshold(getModelField(["decision_threshold", "threshold"], 0.79));
    const internalModel = getModelField(["internal_model", "model_name", "feature_set"], "Balanced_COMB");

    document.getElementById("modelStatus").textContent = "Model: MTFF";

    const items = [
        ["Model", "MTFF", ""],
        ["Internal model", internalModel, "secondary"],
        ["Classifier", getModelField(["classifier", "model_type"], "LightGBM"), ""],
        ["Feature Method", getModelField(["feature_method"], "Multi-Transform Feature Fusion"), ""],
        ["Feature Order", sanitizeFeatureOrder(getModelField(["feature_order"], "FFT + STFT + CWT")), ""],
        ["Input Features", getModelField(["input_features", "n_features", "total_features"], 384), ""],
        ["Selected Features", getModelField(["selected_features", "n_selected_features"], 208), ""],
        ["Decision Threshold", threshold, ""],
        ["Classification Type", "Binary Classification", ""],
    ];

    document.getElementById("modelInfoGrid").innerHTML = items.map(([label, value, secondaryClass]) => `
        <div class="info-item">
            <div class="info-label">${label}</div>
            <div class="info-value ${secondaryClass}">${value}</div>
        </div>
    `).join("");
}

function extractPredictionData(data) {
    const payload = data?.result || data?.data || data?.classification || data || {};
    const activity = normalizeActivity(
        payload.prediction_text ??
        payload.classified_activity ??
        payload.activity ??
        payload.classification ??
        payload.label ??
        payload.result ??
        payload.prediction
    );

    if (!activity || (activity !== "Fall" && activity !== "Non-Fall")) {
        return null;
    }

    const confidence = getFallConfidence(payload);
    const risk = payload.risk_level || (activity === "Fall" ? "High" : "Low");
    const processingTime = (
        payload.processing_time_sec ??
        payload.processing_time ??
        payload.inference_time_sec ??
        payload.elapsed_time_sec ??
        null
    );

    return {
        raw: payload,
        activity,
        confidence,
        threshold: payload.decision_threshold ?? payload.threshold ?? null,
        risk,
        processingTime,
        status: payload.status || (activity === "Fall" ? "Alert" : "Normal"),
        alertText: activity === "Fall"
            ? "Alert Triggered — Immediate attention required"
            : "Normal Activity — No alert triggered"
    };
}

function clearClassification(fileName = null) {
    state.currentResult = null;
    state.currentFile = fileName;
    renderResult();
}

function renderResult() {
    const currentFile = state.currentFile || "None";
    document.getElementById("currentFile").textContent = `Current file: ${currentFile}`;

    const container = document.getElementById("resultContent");
    const result = state.currentResult;

    if (!result) {
        container.innerHTML = `
            <div class="result-box invalid-box">
                <strong>No valid classification result</strong>
                <span>Please choose another test file.</span>
            </div>
        `;
        return;
    }

    const fall = result.activity === "Fall";
    const boxClass = fall ? "fall-box" : "normal-box";
    const title = fall ? "FALL DETECTED" : "NON-FALL / NORMAL";
    const alertClass = fall ? "red" : "green";

    container.innerHTML = `
        <div class="result-box ${boxClass}">
            <span>${fall ? "⊗" : "⊙"}</span>
            <span>${title}</span>
        </div>
        <div class="metric-list">
            <div class="metric-row">
                <span class="metric-label">Fall Confidence</span>
                <span class="metric-value">${formatPercent(result.confidence)}</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Decision Threshold</span>
                <span class="metric-value">${cleanThreshold(result.threshold)}</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Risk Level</span>
                <span class="metric-value">${result.risk}</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Processing Time</span>
                <span class="metric-value">${formatSeconds(result.processingTime)}</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Alert Status</span>
                <span class="metric-value">${fall ? "Alert Triggered" : "Normal Activity"}</span>
            </div>
        </div>
        <div class="alert-note ${alertClass}">
            ${fall ? "⊗" : "⊙"} ${result.alertText.split(" — ")[0]}
            <small>${result.alertText.split(" — ")[1] || "No alert triggered"}</small>
        </div>
    `;
}

function buildSampleSignal(activity = "Fall") {
    const values = [];
    for (let i = 0; i < 110; i++) {
        const base = -38 + Math.sin(i / 5) * 3.5 + Math.sin(i / 13) * 1.4;
        const eventDip = activity === "Fall" ? -35 * Math.exp(-Math.pow((i - 56) / 12, 2)) : -6 * Math.exp(-Math.pow((i - 56) / 18, 2));
        values.push(Number((base + eventDip).toFixed(2)));
    }
    return values;
}

function extractSignal(data) {
    const payload = data?.result || data?.data || data?.classification || data || {};
    const candidates = [
        payload.signal,
        payload.rssi_signal,
        payload.rssi_values,
        payload.rssi_preview,
        payload.preview_signal,
        payload.raw_rssi,
        payload.plot_data?.rssi,
        payload.chart?.rssi,
        data?.signal,
        data?.rssi_signal
    ];

    for (const candidate of candidates) {
        if (Array.isArray(candidate) && candidate.length > 0) {
            if (typeof candidate[0] === "number") return candidate.map(Number).filter(Number.isFinite);
            if (typeof candidate[0] === "object") {
                const mapped = candidate.map(item => Number(item.value ?? item.rssi ?? item.y)).filter(Number.isFinite);
                if (mapped.length > 0) return mapped;
            }
        }
    }
    return null;
}

function renderChart(values) {
    const canvas = document.getElementById("rssiChart");
    const placeholder = document.getElementById("signalPlaceholder");

    if (!values || values.length === 0) {
        canvas.style.display = "none";
        placeholder.style.display = "grid";
        if (state.chart) {
            state.chart.destroy();
            state.chart = null;
        }
        return;
    }

    placeholder.style.display = "none";
    canvas.style.display = "block";

    const labels = values.map((_, index) => index + 1);
    const ctx = canvas.getContext("2d");

    if (state.chart) {
        state.chart.destroy();
    }

    state.chart = new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [{
                label: "RSSI Value (dBm)",
                data: values,
                borderColor: "#2563eb",
                borderWidth: 2,
                tension: 0.35,
                pointRadius: 0,
                fill: false
            }]
        },
        options: {
            responsive: true,
            font: {
                family: '"Inter", "Segoe UI", Arial, sans-serif',
                size: 11,
                weight: "400"
            },
            maintainAspectRatio: false,
            interaction: { intersect: false, mode: "index" },
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (context) => `RSSI Value: ${context.parsed.y} dBm`
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: "Sample Index",
                        color: "#475467",
                        font: { weight: "bold" }
                    },
                    grid: { color: "#eef2f7" },
                    ticks: { color: "#667085", maxTicksLimit: 10 }
                },
                y: {
                    title: {
                        display: true,
                        text: "RSSI Value (dBm)",
                        color: "#475467",
                        font: { weight: "bold" }
                    },
                    grid: { color: "#eef2f7" },
                    ticks: { color: "#667085" }
                }
            }
        }
    });
}

async function loadHealth() {
    const card = document.getElementById("backendStatusCard");
    const status = document.getElementById("backendStatus");
    const icon = document.getElementById("backendIcon");

    try {
        await safeFetch(`${API_BASE_URL}/health`);
        card.classList.remove("status-disconnected");
        card.classList.add("status-connected");
        status.textContent = "Backend Connected";
        if (icon) icon.textContent = "✓";
    } catch {
        card.classList.remove("status-connected");
        card.classList.add("status-disconnected");
        status.textContent = "Backend Disconnected";
        if (icon) icon.textContent = "!";
    }
}

async function loadModelInfo() {
    try {
        state.modelInfo = await safeFetch(`${API_BASE_URL}/model-info`);
    } catch {
        state.modelInfo = {};
    }
    renderModelInfo();
}

async function loadHistory() {
    try {
        const response = await fetch(`${API_BASE_URL}/history?limit=20`);
        if (!response.ok) throw new Error("History failed");
        const data = await response.json();
        const records = Array.isArray(data) ? data : data.items || data.records || data.history || [];
        state.history = Array.isArray(records) ? records : [];
        renderHistory();
        updateLastClassificationTime();
        setMessage("historyMessage", "");
    } catch {
        state.history = [];
        renderHistory();
        updateLastClassificationTime();
        setMessage("historyMessage", "Unable to load detection history at the moment.", "error");
    }
}

function updateLastClassificationTime() {
    const latest = getLatestHistoryRecord(state.history);
    document.getElementById("lastClassification").textContent = latest
        ? `Last: ${formatMalaysiaTimestamp(getRecordTimestamp(latest))}`
        : "Last: No record yet";
}

function getRecordActivity(record) {
    return normalizeActivity(record.prediction_text || record.classified_activity || record.activity || record.classification || record.result);
}

function getRecordFileName(record) {
    return record.file_name || record.filename || "—";
}

function getRecordConfidence(record) {
    if (record.fall_confidence_percent !== undefined && record.fall_confidence_percent !== null) {
        return formatPercent(record.fall_confidence_percent);
    }
    return formatPercent(record.probability ?? record.fall_probability ?? record.confidence);
}

function getInputMode(record) {
    const mode = record.input_mode || "MANUAL TEST";
    const upper = String(mode).replace(/_/g, " ").toUpperCase();
    if (upper.includes("UPLOAD")) return "MANUAL UPLOAD";
    if (upper.includes("LIVE")) return "LIVE MONITORING";
    return "MANUAL TEST";
}

function getStatus(record, activity) {
    return record.status || (activity === "Fall" ? "Alert" : "Normal");
}

function escapeHtml(value) {
    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}

function renderHistory() {
    const body = document.getElementById("historyBody");
    const records = state.history;

    if (!Array.isArray(records) || records.length === 0) {
        body.innerHTML = `<tr><td colspan="9">No detection history available</td></tr>`;
        return;
    }

    body.innerHTML = records.map(record => {
        const id = record.id;
        const activity = getRecordActivity(record);
        const fall = activity === "Fall";
        const risk = record.risk_level || (fall ? "High" : "Low");
        const mode = getInputMode(record);
        const status = getStatus(record, activity);
        const statusClass = String(status).toLowerCase().includes("alert") ? "badge-alert" : "badge-normal";
        const activityClass = fall ? "badge-fall" : "badge-normal";
        const riskClass = String(risk).toLowerCase().includes("high") ? "badge-high" : "badge-low";

        return `
            <tr>
                <td>${formatMalaysiaTimestamp(getRecordTimestamp(record))}</td>
                <td>${escapeHtml(getRecordFileName(record))}</td>
                <td><span class="badge ${activityClass}">${escapeHtml(activity || "—")}</span></td>
                <td>${getRecordConfidence(record)}</td>
                <td><span class="badge ${riskClass}">${escapeHtml(risk || "—")}</span></td>
                <td><span class="badge badge-manual">${escapeHtml(mode)}</span></td>
                <td>${formatSeconds(record.processing_time_sec ?? record.processing_time)}</td>
                <td><span class="badge ${statusClass}">${escapeHtml(status)}</span></td>
                <td>
                    <button class="button button-danger-lite" title="Delete record" onclick="deleteRecord('${escapeHtml(id)}')">🗑</button>
                </td>
            </tr>
        `;
    }).join("");
}

async function classifyByFilename() {
    const filename = document.getElementById("filenameInput").value.trim();
    setMessage("filenameMessage", "");

    if (!filename) {
        clearClassification(null);
        setMessage("filenameMessage", "Please enter a .mat filename.", "error");
        return;
    }

    clearClassification(filename);
    setLoading("classifyBtn", true, "Classifying...");

    try {
        const data = await safeFetch(`${API_BASE_URL}/predict/by-filename`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ filename })
        });

        const result = extractPredictionData(data);
        if (!result) throw new Error("Unsupported");

        state.currentFile = filename;
        state.currentResult = result;
        renderResult();

        const signal = extractSignal(data) || buildSampleSignal(result.activity);
        renderChart(signal);

        await loadHistory();
    } catch {
        clearClassification(filename);
        renderChart(null);
        setMessage("filenameMessage", friendlyErrorMessage(), "error");
    } finally {
        setLoading("classifyBtn", false);
    }
}

function handleFileSelect() {
    const input = document.getElementById("fileUpload");
    state.selectedFile = input.files && input.files.length > 0 ? input.files[0] : null;
    document.getElementById("selectedFileName").textContent = state.selectedFile ? state.selectedFile.name : "No file selected";
    setMessage("uploadMessage", "");
}

async function uploadAndClassify() {
    setMessage("uploadMessage", "");

    if (!state.selectedFile) {
        clearClassification(null);
        setMessage("uploadMessage", "Please upload a .mat file first.", "error");
        return;
    }

    clearClassification(state.selectedFile.name);
    setLoading("uploadBtn", true, "Classifying...");

    const formData = new FormData();
    formData.append("file", state.selectedFile);

    try {
        const response = await fetch(`${API_BASE_URL}/predict/batch`, {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error("Upload failed");
        const data = await response.json();

        const result = extractPredictionData(data);
        if (!result) throw new Error("Unsupported");

        state.currentFile = state.selectedFile.name;
        state.currentResult = result;
        renderResult();

        const signal = extractSignal(data) || buildSampleSignal(result.activity);
        renderChart(signal);

        await loadHistory();
    } catch {
        clearClassification(state.selectedFile ? state.selectedFile.name : null);
        renderChart(null);
        setMessage("uploadMessage", friendlyErrorMessage(), "error");
    } finally {
        setLoading("uploadBtn", false);
    }
}

async function deleteRecord(recordId) {
    if (!recordId || recordId === "undefined" || recordId === "null") {
        setMessage("historyMessage", "This history row cannot be deleted because it has no record ID.", "error");
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/history/${recordId}`, {
            method: "DELETE"
        });
        if (!response.ok) throw new Error("Delete failed");
        await loadHistory();
    } catch {
        setMessage("historyMessage", "Unable to delete this record. Please try again.", "error");
    }
}

async function clearManualTests() {
    const btn = document.getElementById("clearManualBtn");
    btn.disabled = true;
    try {
        const response = await fetch(`${API_BASE_URL}/history/manual`, {
            method: "DELETE"
        });
        if (!response.ok) throw new Error("Clear failed");
        await loadHistory();
    } catch {
        setMessage("historyMessage", "Unable to clear manual test records. Please try again.", "error");
    } finally {
        btn.disabled = false;
    }
}

async function clearAllHistory() {
    const confirmed = window.confirm("Clear all detection history? This will remove all manual and live monitoring records.");
    if (!confirmed) return;

    const btn = document.getElementById("clearAllBtn");
    btn.disabled = true;
    try {
        const response = await fetch(`${API_BASE_URL}/history/all?confirm=true`, {
            method: "DELETE"
        });
        if (!response.ok) throw new Error("Clear all failed");
        await loadHistory();
    } catch {
        setMessage("historyMessage", "Unable to clear all history. Please try again.", "error");
    } finally {
        btn.disabled = false;
    }
}

async function bootDashboard() {
    renderResult();
    renderChart(null);
    await Promise.all([loadHealth(), loadModelInfo(), loadHistory()]);
}

document.addEventListener("DOMContentLoaded", bootDashboard);
</script>
</body>
</html>
"""

components.html(DASHBOARD_HTML, height=1320, scrolling=True)
