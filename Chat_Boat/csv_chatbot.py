import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI



# Function to display data columns and summary statistics
def display_data_statistics(df):
    # Get summary statistics for numeric columns
    numeric_stats = df.describe()

    # Get column names
    column_names = df.columns.tolist()

    # Create a single-column layout
    left_column, right_column = st.columns(2)

    # Display data columns and summary statistics in Streamlit
    right_column.write("Data columns:")
    right_column.write(column_names)

    left_column.write("Summary Statistics:")
    left_column.write(numeric_stats)
    return None

def read_df():
    file = st.file_uploader("Upload the CSV file", type = "CSV")
    if file is not None:
        # Load data
        dataframe = pd.read_csv(file)
    return dataframe, file

def sidebar():
    st.sidebar.image(r"Data\analytics-1799646_1280.png")
    # Create sidebar navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Data Statistics"])
    return page


def main():
    st.title("Streamlit Application")
    page = sidebar()
    
    file = st.file_uploader("Upload the CSV file", type = "CSV")
    print(file)
    
    if file is not None:
        df = pd.read_csv(file)

    # Display different pages based on user selection
    if page == "Home":
        st.write("Chat with CSV!")

        # call the chain objects
        query = st.selectbox("Select Question You Want to Ask:",
                             options=["Number of rows in given dataframe?",
                                      "Are there any missing values in given data?",
                                      "Other"])

        if query == "Other":
            query = st.text_input("Ask a question about CSV: ")

        API_key = st.text_input('OpenAI API Key', type='password', disabled = not query)


        if API_key and file is not None and query:
            llm = OpenAI(temperature = 0.1, api_key = API_key)
            agent = create_csv_agent(
                OpenAI( temperature = 0, api_key = API_key),
                df,
                verbose=True,
            )

            reponse = agent.run(query)

            st.write(f"Your question was: {query}")
            st.write(f"Answer: {reponse}")

    elif page == "Data Statistics":
        st.write(df)
        st.write("Data Statistics Page")
        display_data_statistics(df)
    return None

# Run the Streamlit application
if __name__ == "__main__":
    main()
