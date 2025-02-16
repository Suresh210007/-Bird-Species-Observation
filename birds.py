import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# File path
file_path = "D:/GUVI PROJ02/NCRN LAND Bird Monitoring Data 2007 - 2017_Public (1).xlsx"
# Function to load Excel sheets
def load_data(file_path):
    data = {}
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return data
    try:
        xls = pd.ExcelFile(file_path)
        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            if not df.empty:
                data[sheet] = df
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
    return data

# Load and clean data
data = load_data(file_path)

if not data:
    st.error("No sheets found in the Excel file or all sheets are empty.")
    st.stop()

def clean_data(df):
    df = df.dropna(how='all').drop_duplicates()
    if 'Year' in df.columns:
        df = df[df['Year'].notnull()]
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

# Clean each sheet
data_cleaned = {sheet: clean_data(df) for sheet, df in data.items() if not df.empty}

# Streamlit App
def app():
    st.set_page_config(page_title="Bird Species Observation", layout="wide")
    st.title("🦉 Bird Species Observation Dashboard")

    col_main, col_sidebar = st.columns([3, 1], gap="large")  # Right Sidebar

    # Right Sidebar
    with col_sidebar:
        st.header("📊 Data Selection")
        if not data_cleaned:
            st.error("No valid sheets with data found in the Excel file.")
            st.stop()

        sheet_name = st.selectbox("Select Dataset", list(data_cleaned.keys()))
        df_selected = data_cleaned.get(sheet_name, pd.DataFrame())

        if df_selected.empty:
            st.warning("No data available for the selected sheet.")
            st.stop()

        if st.checkbox("Show Raw Data"):
            st.subheader("Raw Data Preview")
            st.dataframe(df_selected)

        # Habitat Type Filter
        st.subheader("🌿 Habitat Filter")
        habitat_types = ['Forest', 'Grassland']
        selected_habitat = st.radio("Select Habitat Type", habitat_types)

        if 'Habitat_Type' in df_selected.columns:
            df_selected = df_selected[df_selected['Habitat_Type'] == selected_habitat]

        # Seasonal Filter
        st.subheader("📆 Seasonal Analysis")
        seasons = ['Winter', 'Spring', 'Summer', 'Fall']
        selected_season = st.radio("Select Season", seasons)

    # Main Content
    with col_main:
        # Species Observation Analysis
        st.subheader(f"📌 Top Bird Species Observed in {selected_habitat} ({selected_season})")
        if 'Common_Name' in df_selected.columns and not df_selected['Common_Name'].dropna().empty:
            species_count = df_selected['Common_Name'].value_counts().head(10)
            if not species_count.empty:
                col1, col2 = st.columns([2, 1])
                with col1:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.barplot(x=species_count.values, y=species_count.index, palette='dark', ax=ax)
                    ax.set_xlabel("Number of Observations")
                    ax.set_ylabel("Bird Species")
                    ax.set_title(f"Top 10 Most Observed Bird Species in {selected_habitat}")
                    st.pyplot(fig)
                with col2:
                    fig, ax = plt.subplots(figsize=(5, 5))
                    species_count.plot.pie(autopct='%1.1f%%', ax=ax, startangle=90, cmap="tab10")
                    ax.set_ylabel("")
                    ax.set_title("Bird Species Distribution")
                    st.pyplot(fig)
            else:
                st.warning("No bird species data available for visualization.")
        else:
            st.warning("Column 'Common_Name' not found or empty in dataset.")

        # Yearly Observations
        st.subheader(f"📅 Yearly Bird Observations in {selected_habitat}")
        if 'Year' in df_selected.columns and not df_selected['Year'].dropna().empty:
            yearly_counts = df_selected['Year'].value_counts().sort_index()
            if not yearly_counts.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', linewidth=2.5, color='crimson', ax=ax)
                ax.set_xlabel("Year")
                ax.set_ylabel("Number of Observations")
                ax.set_title(f"Yearly Bird Observations Trend in {selected_habitat}")
                st.pyplot(fig)
            else:
                st.warning("No yearly data available for visualization.")
        else:
            st.warning("Column 'Year' not found or empty in dataset.")

if __name__ == "__main__":
    app()