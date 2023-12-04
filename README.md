# Malaria Forecasting Deep Learning Model

# Creators of DL Model
- Julia Mc-Addy
- Juliann Mc-Addy

# Problem
Malaria is a hazardous infectious disease caused by the Plasmodium parasite which spreads through the bites of infected mosquitoes (NHS inform, 2023). According to the World Health Organization (WHO), there has been an estimated 247 million Malaria cases worldwide, and four African countries, including Nigeria, Democratic Republic of the Congo, United Republic of Tanzania and Niger accounted for half of all Malaria deaths (World Health Organization, n.d.). West Africa is one of the prominent areas worldwide facing constant challenges with malaria outbreaks. We believe that most countries in this region lack advanced tools that would enable them to predict the outbreaks of this disease, leading to an increased level of infections amongst citizens and inefficient medical resources.

# Solution
Through the use of this AI model, we aim to forecast the number of malaria cases from 2022 to 2032, which will lead to an increased level of preparedness to ensure a safe and healthy environment for all of West Africa.

# Dataset
The dataset was obtained from the World Health Organization. It contained the confirmed number of malaria cases from 2000 to 2021 for almost every country in the world. 
APA Citation: World Health Organization. (n.d.). Gho | by category | confirmed malaria cases - by country. World Health Organization. https://apps.who.int/gho/data/node.main.MALARIACONFCASES?lang=en 

# Operations
- Filtered to produce a dataset for 16 West African countries only- Benin, Burkina Faso, Cape Verde, Côte d’Ivoire, Gambia, Ghana, Guinea, Guinea-Bissau, Liberia, Mali, Mauritania, Niger, Nigeria, Senegal, Sierra Leone,Togo
- Renamed to appropriate column headings, such that the first column heading is titled 'Country' and the rest of the column headings are 2021, 2020, 2019,etc
- Data Preprocessing:
    - Conversion the columns into numeric
    - Imputation
    - Splitting  the dataset (containing details of West African countries) into 16 dataframes. Each dataframe must correspond to each West African country
- Exploratory Data Analysis:
    - Construction of scatterplots to visualize the number of malaria cases from 2000 to 2021 for each West African country
    - Interpretation of the scatterplots
- Alteration of the 16 dataframes by sorting the number of malaria cases in each year in ascending order
- Feature Engineering:
    - Scaled each dataframe using MinMaxScalar
    - Split each dataframe into training, testing and validation sets
- Training of Models, Evaluation and Optimisation:
    - Each dataframe was first trained without GridSearch and Cross Validation. The training and testing mean sqare errors were calculated and printed
    - Each dataframe was then trained using GridSearch and Cross Validation. The training and testing mean sqare errors were calculated and printed
    - The optimized model was built for each dataframe
- The optimized model was then used to predict the number of malaria cases for the years 2022 to 2032. A scatterplot was then generated to capture and visualise this
- Deployment:
    - Streamlit, a Python library, was used to create the web application
      
# How to the application was hosted on a local server:
- Installation of Streamlit
- Creation of Streamlit Application
- Run the Streamlit Application by running the following command- streamlit run deployment.py
- Access the Streamlit App by opening a web browser and navigating to the URL provided by the Streamlit command

# Video Link
- Video link- https://youtu.be/xOmSqd-uLQs
    
