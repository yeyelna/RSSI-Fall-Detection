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
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
        .block-container {
            padding-top: 0.75rem;
            padding-left: 0.75rem;
            padding-right: 0.75rem;
            max-width: 100%;
        }
        header, footer {visibility: hidden;}
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
    :root {
        --bg: #f7f9fc;
        --card: #ffffff;
        --text: #132238;
        --muted: #667085;
        --line: #e6eaf0;
        --blue: #2563eb;
        --blue-soft: #eff6ff;
        --green: #16a34a;
        --green-soft: #ecfdf3;
        --red: #dc2626;
        --red-soft: #fff1f2;
        --purple: #7c3aed;
        --purple-soft: #f5f3ff;
        --shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        --radius: 18px;
    }
    * {
        box-sizing: border-box;
    }
    body {
        margin: 0;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: var(--bg);
        color: var(--text);
    }
    .dashboard {
        width: 100%;
        max-width: 1550px;
        margin: 0 auto;
        padding: 18px;
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
        padding: 22px 24px;
        margin-bottom: 18px;
    }
    .header-title {
        margin: 0;
        font-size: clamp(1.2rem, 2vw, 1.9rem);
        line-height: 1.15;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .header-subtitle {
        margin: 8px 0 0;
        font-size: 0.95rem;
        color: var(--muted);
    }
    .status-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(150px, 1fr));
        gap: 10px;
        width: min(620px, 100%);
    }
    .status-card {
        min-height: 72px;
        padding: 12px 14px;
        border-radius: 14px;
        border: 1px solid var(--line);
        background: #fbfdff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 5px;
    }
    .status-label {
        color: var(--muted);
        font-size: 0.74rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .status-value {
        font-size: 0.9rem;
        font-weight: 800;
        word-break: break-word;
    }
    .status-connected {
        background: var(--green-soft);
        border-color: #bbf7d0;
        color: var(--green);
    }
    .status-disconnected {
        background: var(--red-soft);
        border-color: #fecdd3;
        color: var(--red);
    }
    .section-title {
        margin: 0 0 16px;
        font-size: 1rem;
        font-weight: 800;
    }
    .first-row {
        display: grid;
        grid-template-columns: minmax(260px, 0.9fr) minmax(390px, 1.8fr) minmax(290px, 1fr);
        gap: 18px;
        margin-bottom: 18px;
        align-items: stretch;
    }
    .second-row {
        display: grid;
        grid-template-columns: minmax(350px, 1fr) minmax(350px, 1fr);
        gap: 18px;
        margin-bottom: 18px;
    }
    .panel {
        padding: 20px;
        min-width: 0;
    }
    label {
        display: block;
        margin-bottom: 8px;
        color: #344054;
        font-size: 0.86rem;
        font-weight: 700;
    }
    input[type="text"] {
        width: 100%;
        border: 1px solid #d0d5dd;
        border-radius: 12px;
        padding: 12px 13px;
        color: var(--text);
        background: white;
        font-size: 0.95rem;
        outline: none;
    }
    input[type="text"]:focus {
        border-color: var(--blue);
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }
    .button {
        width: 100%;
        margin-top: 12px;
        border: 0;
        border-radius: 12px;
        padding: 12px 15px;
        font-size: 0.92rem;
        font-weight: 800;
        cursor: pointer;
        transition: transform 0.15s ease, opacity 0.15s ease, background 0.15s ease;
    }
    .button:active {
        transform: scale(0.99);
    }
    .button-primary {
        background: var(--blue);
        color: white;
    }
    .button-secondary {
        background: var(--blue-soft);
        color: var(--blue);
        border: 1px solid #bfdbfe;
    }
    .button-danger-lite {
        width: auto;
        margin: 0;
        background: transparent;
        color: var(--red);
        padding: 8px 10px;
        border: 1px solid transparent;
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
        background: var(--line);
        margin: 22px 0;
    }
    .upload-box {
        position: relative;
        border: 1.5px dashed #cbd5e1;
        border-radius: 14px;
        background: #fbfdff;
        min-height: 118px;
        display: grid;
        place-items: center;
        text-align: center;
        padding: 18px;
        cursor: pointer;
        color: var(--muted);
        overflow: hidden;
    }
    .upload-box input {
        position: absolute;
        inset: 0;
        opacity: 0;
        cursor: pointer;
    }
    .upload-icon {
        font-size: 1.8rem;
        color: #94a3b8;
        line-height: 1;
        margin-bottom: 6px;
    }
    .upload-main {
        color: #334155;
        font-size: 0.92rem;
        font-weight: 800;
    }
    .upload-sub {
        color: var(--muted);
        font-size: 0.78rem;
        margin-top: 4px;
    }
    .helper-text {
        margin-top: 8px;
        color: var(--muted);
        font-size: 0.82rem;
        word-break: break-word;
    }
    .signal-card {
        min-height: 405px;
        display: flex;
        flex-direction: column;
    }
    .chart-wrap {
        flex: 1;
        min-height: 310px;
        background: #fff;
        border-radius: 14px;
        border: 1px solid #f1f5f9;
        padding: 10px;
        position: relative;
    }
    .placeholder {
        height: 100%;
        min-height: 280px;
        display: grid;
        place-items: center;
        color: var(--muted);
        text-align: center;
        border: 1px dashed #d8dee8;
        border-radius: 14px;
        background: #fcfdff;
        padding: 20px;
    }
    .result-card {
        min-height: 405px;
    }
    .current-file {
        margin-top: -6px;
        margin-bottom: 14px;
        color: #475467;
        font-size: 0.86rem;
    }
    .result-box {
        border-radius: 16px;
        padding: 18px;
        font-size: 1.08rem;
        font-weight: 900;
        letter-spacing: 0.02em;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 16px;
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
        color: #475467;
        background: #f8fafc;
        border-color: #d0d5dd;
        align-items: flex-start;
        flex-direction: column;
        gap: 6px;
        letter-spacing: 0;
    }
    .invalid-box strong {
        color: #334155;
    }
    .metric-list {
        display: grid;
        gap: 12px;
    }
    .metric-row {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        padding-bottom: 10px;
        border-bottom: 1px solid #f1f5f9;
        font-size: 0.9rem;
    }
    .metric-row:last-child {
        border-bottom: none;
    }
    .metric-label {
        color: var(--muted);
        font-weight: 700;
    }
    .metric-value {
        color: var(--text);
        font-weight: 900;
        text-align: right;
    }
    .alert-note {
        margin-top: 14px;
        border-radius: 14px;
        padding: 13px 14px;
        font-weight: 800;
        font-size: 0.88rem;
        border: 1px solid;
    }
    .alert-note small {
        display: block;
        margin-top: 3px;
        font-weight: 600;
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
        margin-top: 12px;
        border-radius: 12px;
        padding: 11px 12px;
        font-size: 0.86rem;
        font-weight: 700;
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
        gap: 11px;
        flex-wrap: wrap;
        padding: 18px 8px 8px;
    }
    .flow-step {
        min-width: 92px;
        max-width: 118px;
        text-align: center;
        display: grid;
        justify-items: center;
        gap: 7px;
    }
    .flow-icon {
        width: 42px;
        height: 42px;
        border-radius: 13px;
        display: grid;
        place-items: center;
        font-size: 1.35rem;
        background: var(--blue-soft);
        color: var(--blue);
        border: 1px solid #bfdbfe;
    }
    .flow-label {
        font-size: 0.76rem;
        color: #334155;
        font-weight: 800;
        line-height: 1.2;
    }
    .flow-arrow {
        color: #94a3b8;
        font-weight: 900;
    }
    .flow-vertical {
        display: none;
    }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;
    }
    .info-item {
        border: 1px solid #f1f5f9;
        background: #fcfdff;
        border-radius: 14px;
        padding: 13px 14px;
        min-width: 0;
    }
    .info-label {
        font-size: 0.75rem;
        color: var(--muted);
        font-weight: 800;
        margin-bottom: 6px;
    }
    .info-value {
        font-size: 0.92rem;
        font-weight: 900;
        word-break: break-word;
    }
    .info-value.secondary {
        color: #475467;
        font-weight: 800;
        font-size: 0.86rem;
    }
    .history-card {
        padding: 20px;
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
        padding: 9px 12px;
        font-size: 0.82rem;
    }
    .table-wrap {
        width: 100%;
        overflow-x: auto;
        border: 1px solid #eef2f7;
        border-radius: 14px;
    }
    table {
        width: 100%;
        min-width: 1080px;
        border-collapse: collapse;
        background: white;
    }
    th, td {
        padding: 13px 14px;
        border-bottom: 1px solid #eef2f7;
        text-align: left;
        vertical-align: middle;
        font-size: 0.82rem;
        white-space: nowrap;
    }
    th {
        color: #475467;
        background: #fbfdff;
        font-size: 0.74rem;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    tr:last-child td {
        border-bottom: 0;
    }
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        border-radius: 999px;
        padding: 5px 10px;
        font-size: 0.76rem;
        font-weight: 900;
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
        width: 12px;
        height: 12px;
        border: 2px solid rgba(37, 99, 235, 0.22);
        border-top-color: var(--blue);
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
        vertical-align: -2px;
        margin-right: 6px;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    @media (max-width: 1050px) {
        .header-card {
            align-items: flex-start;
            flex-direction: column;
        }
        .status-grid {
            width: 100%;
        }
        .first-row {
            grid-template-columns: 1fr;
        }
        .input-panel { order: 1; }
        .result-card { order: 2; }
        .signal-card { order: 3; }
        .second-row {
            grid-template-columns: 1fr;
        }
    }
    @media (max-width: 768px) {
        .dashboard {
            padding: 10px;
        }
        .header-card, .panel, .history-card {
            padding: 16px;
        }
        .status-grid {
            grid-template-columns: 1fr;
        }
        .first-row,
        .second-row {
            gap: 12px;
            margin-bottom: 12px;
        }
        .button,
        .history-actions .button {
            width: 100%;
        }
        .history-header {
            align-items: stretch;
            flex-direction: column;
        }
        .history-actions {
            width: 100%;
            flex-direction: column;
        }
        .flow-horizontal {
            display: none;
        }
        .flow-vertical {
            display: grid;
            gap: 9px;
        }
        .vertical-step {
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 10px 12px;
            border: 1px solid #eef2f7;
            border-radius: 13px;
            background: #fcfdff;
        }
        .step-number {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--blue-soft);
            color: var(--blue);
            display: grid;
            place-items: center;
            font-weight: 900;
            flex: 0 0 auto;
        }
        .info-grid {
            grid-template-columns: 1fr;
        }
        .chart-wrap {
            min-height: 260px;
        }
        .placeholder {
            min-height: 230px;
        }
        th, td {
            padding: 11px 12px;
        }
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
            <div id="backendStatusCard" class="status-card">
                <span class="status-label">Backend status</span>
                <span id="backendStatus" class="status-value"><span class="tiny-loader"></span>Checking...</span>
            </div>
            <div class="status-card">
                <span class="status-label">Model status</span>
                <span id="modelStatus" class="status-value">Model: MTFF</span>
            </div>
            <div class="status-card">
                <span class="status-label">Last classification time</span>
                <span id="lastClassification" class="status-value">Loading...</span>
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
                        <div class="upload-icon">⇧</div>
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
                    <div class="flow-step"><div class="flow-icon">▣</div><div class="flow-label">MATLAB .mat File</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">≋</div><div class="flow-label">RSSI Signal</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">⌁</div><div class="flow-label">FFT + STFT + CWT</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">◇</div><div class="flow-label">MTFF</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">▤</div><div class="flow-label">LightGBM Model</div></div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step"><div class="flow-icon">↗</div><div class="flow-label">Fall / Non-Fall</div></div>
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
                <h2 class="section-title">Technical Model Information</h2>
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

    try {
        await safeFetch(`${API_BASE_URL}/health`);
        card.classList.remove("status-disconnected");
        card.classList.add("status-connected");
        status.textContent = "Backend Connected";
    } catch {
        card.classList.remove("status-connected");
        card.classList.add("status-disconnected");
        status.textContent = "Backend Disconnected";
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
        ? formatMalaysiaTimestamp(getRecordTimestamp(latest))
        : "No record yet";
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
