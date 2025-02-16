# Bird Species Observation Dashboard

## 📌 Overview
The **Bird Species Observation Dashboard** is a **Streamlit web application** that allows users to explore and analyze bird observation data collected between **2007 - 2017**. The app loads an **Excel dataset**, cleans the data, and provides **interactive visualizations** based on habitat type, season, and species.

## 🚀 Features
- **Load & Clean Data**: Reads multiple sheets from an Excel file, removes empty rows/duplicates, and formats date columns.
- **Data Selection**: Users can choose different datasets (sheets) from the Excel file.
- **Filters**:
  - Filter observations by **Habitat Type** (Forest, Grassland).
  - Filter observations by **Season** (Winter, Spring, Summer, Fall).
- **Visualizations**:
  - **Top 10 Bird Species** observed (Bar Chart & Pie Chart).
  - **Yearly Bird Observations Trend** (Line Chart).
- **View Raw Data**: Users can toggle to see the raw dataset.

## 🏗️ Installation & Setup

### 1️⃣ Prerequisites
Make sure you have the following installed:
- **Python 3.x**
- **pip (Python package manager)**
- **Streamlit**

### 2️⃣ Install Required Packages
```bash
pip install pandas streamlit matplotlib seaborn
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 📂 File Structure
```
📂 BirdObservationApp
 ├── app.py                  # Main Streamlit app
 ├── NCRN LAND Bird Monitoring Data.xlsx # Data file (place in same folder)
 ├── README.md               # Documentation
```

## 📝 How to Use
1. **Run the app** using the Streamlit command.
2. **Select a dataset** from the sidebar.
3. **Filter data** by habitat and season.
4. **View top species** and **yearly trends** using visualizations.
5. **Toggle raw data** for detailed insights.

## 📊 Example Visualizations
### Top 10 Bird Species Observed (Bar Chart & Pie Chart)


### Yearly Bird Observations Trend (Line Chart)

## 🛠️ Future Enhancements
- 🌍 **Geospatial Mapping** of bird species locations
- 📌 **More Filters** (e.g., Bird Family, Rarity Level)
- 📈 **Additional Graphs** (Heatmaps, Time-Series Analysis)

## 🤝 Contributing
If you'd like to improve this project, feel free to fork, modify, and submit a pull request!

## 📜 License
This project is **open-source** and available under the **MIT License**.

