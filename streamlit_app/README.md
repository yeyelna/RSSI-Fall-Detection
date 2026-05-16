# Wi-Fi RSSI Fall Detection Dashboard

A responsive one-page Streamlit Cloud dashboard for a Wi-Fi RSSI-based fall detection system.  
The dashboard connects to a FastAPI backend and classifies `.mat` test files as either **Fall** or **Non-Fall** using an MTFF model.

## Dashboard Purpose

This dashboard is designed for an FYP presentation and demonstration of a Wi-Fi RSSI fall detection system.  
It allows users to:

- Classify a prepared `.mat` test file by entering its filename
- Upload a `.mat` file for classification
- View the RSSI signal preview
- View the latest classification result
- Monitor backend and model status
- View recent detection events
- Delete individual history records
- Clear manual test history
- Clear all detection history

## Important UI Terminology

The dashboard uses the term **classification** in the user interface instead of **prediction**, except where the FastAPI endpoint name requires `/predict`.

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```

## API Base URL

The dashboard connects to the FastAPI backend using the editable API base URL inside `app.py`:

```javascript
const API_BASE_URL = "https://wi-fi-rssi-fall-detection-system.onrender.com";
```

Do not add `/docs` to the API base URL.

## Required FastAPI Endpoints

The dashboard expects the backend to support the following endpoints:

```text
GET     /health
GET     /model-info
GET     /history?limit=20
POST    /predict/by-filename
POST    /predict/batch
DELETE  /history/{record_id}
DELETE  /history/manual
DELETE  /history/all?confirm=true
```

## Main Features

### 1. Header Section

The header includes:

- Dashboard title
- Dashboard subtitle
- Backend status
- Model status
- Last classification time

The backend status is checked using:

```text
GET /health
```

The model status is checked using:

```text
GET /model-info
```

The latest classification time is taken from:

```text
GET /history?limit=20
```

The dashboard displays timestamps in readable Malaysia time format.

### 2. Input Panel

The input panel supports two classification methods:

#### Classify by Filename

The user can enter a `.mat` filename such as:

```text
data31.mat
```

Then click:

```text
Classify by Filename
```

This calls:

```text
POST /predict/by-filename
```

Request body:

```json
{
  "filename": "data31.mat"
}
```

#### Upload and Classify

The user can upload a `.mat` file and click:

```text
Upload and Classify
```

This calls:

```text
POST /predict/batch
```

The uploaded file is sent using `FormData` with the exact key name:

```javascript
formData.append("file", selectedFile);
```

### 3. RSSI Signal Preview

The dashboard displays a clean RSSI line chart with:

- White background
- Light grid lines
- Blue line
- X-axis: Sample Index
- Y-axis: RSSI Value (dBm)

If the API does not return actual RSSI signal values, the dashboard uses a sample-style preview graph after classification.

### 4. Classification Result

The classification result card shows:

- Current file being tested
- Fall or Non-Fall status
- Fall confidence
- Decision threshold
- Risk level
- Processing time
- Alert status

For Fall activity, the dashboard shows:

```text
FALL DETECTED
```

For Non-Fall activity, the dashboard shows:

```text
NON-FALL / NORMAL
```

Unsupported files are handled with a user-friendly message:

```text
File not supported for fast classification. Please choose a test file from the prepared dataset.
```

The dashboard does not show raw backend or internal API error messages.

### 5. System Processing Flow

The system processing flow is displayed as:

```text
MATLAB .mat File
→ RSSI Signal
→ FFT + STFT + CWT
→ MTFF
→ LightGBM Model
→ Fall / Non-Fall
```

On mobile screens, this becomes a vertical step-by-step list.

### 6. Technical Model Information

The dashboard displays:

```text
Model: MTFF
Internal model: Balanced_COMB
Classifier: LightGBM
Feature Method: Multi-Transform Feature Fusion
Feature Order: FFT + STFT + CWT
Input Features: 384
Selected Features: 208
Decision Threshold: 0.79
Classification Type: Binary Classification
```

In the main display, the user-facing model name is **MTFF**.

### 7. Recent Detection Events

The dashboard shows a full-width history table with:

- Timestamp
- File Name
- Classified Activity
- Fall Confidence
- Risk Level
- Input Mode
- Processing Time
- Status
- Action

The table supports:

- Delete one history row
- Clear Manual Tests
- Clear All History

Input modes supported:

```text
MANUAL TEST
MANUAL UPLOAD
LIVE MONITORING
```

## Running Locally

Install Streamlit:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

## Deploying to Streamlit Cloud

1. Upload these files to your GitHub repository:

```text
app.py
requirements.txt
README.md
```

2. Go to Streamlit Cloud.

3. Select your GitHub repository.

4. Set the main file path as:

```text
app.py
```

5. Deploy the app.

## Notes for Backend Connection

Make sure your FastAPI backend is already deployed and running.

The current backend URL used in the dashboard is:

```text
https://wi-fi-rssi-fall-detection-system.onrender.com
```

If your backend URL changes, update this line in `app.py`:

```javascript
const API_BASE_URL = "https://wi-fi-rssi-fall-detection-system.onrender.com";
```

## Requirements

The dashboard only needs Streamlit:

```text
streamlit>=1.36.0
```

The chart and API calls are handled inside the embedded HTML/JavaScript code in `app.py`.

## Final Output

This dashboard is intended to look and function like a working cloud-connected fall detection classification system, not a static report. It is suitable for demonstrating the Wi-Fi RSSI fall detection system during an FYP presentation.
