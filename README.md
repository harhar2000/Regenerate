# Regenerate - EarthAI x ClimateImpact Hackathon

Welcome to the repository for **Regenerate**, this project was developed over 24hrs during the EarthAI x ClimateImpact summit Hackathon at The Royal Institution.

## About the Hackathon
The EarthAI x ClimateImpact summit at The Royal Institution brought together 80 hackers split into 16 teams. The event was judged by a panel of industry experts from Extantia, OpenAI, Amazon, GSK, Dyson, DitchCarbon and Carbonfuture, fostering innovation and inspiration.

## Project Overview
**Regenerate** introduces Vi (Version One), a platform aimed at revolutionising ecological regeneration. Vi integrates carbon and biodiversity credits into a unified model, enhancing biomass wellbeing and utilising real-time data APIs for direct user engagement with carbon metrics. The goal is to stimulate competition and collaboration through a system of credits, verified by AI, satellite technology, and peer reviews. This approach aims to drive ecological action and public awareness through transparent, real-time environmental data.

Given we had 24 hours to bring our idea to fruition, we decided to distill our overview to its simplest form for the pitch. Our 3-minute pitch included an explanation of Carbon Regeneration and Carbon Sequestration. A demonstration of an interactive map with clickable pinpoints geographically tied to various projects releasing carbon was shown. You can click these pinpoints and review carbon data relating to that project at that location.

### Implementation Details
- We utilised AI to extract emission data from various sources and APIs, consolidating them into a single, readable CSV file, ready to be formatted.
- For the backend, we gathered and formatted annual CO2 emissions data per capita for Brazil from 2017 to 2020. We used machine learning to predict future CO2 emissions and developed an interactive map interpreting Brazil's emission data.
- Each location on the map is marked with a popup providing detailed emissions statistics, comparing data and enabling users to see real-time environmental changes directly linked to their actions.

## Features
- **Real-time Environmental Impact**: Users can access a detailed map showing real-time environmental impacts of our credit-linked projects.
- **Direct Contribution**: Users can contribute directly by participating in projects and earning credits, verified by AI modelling, satellite technology, and peer-to-peer validations.
- **Incentivising Individual and Corporate Action**: Our approach incentivises individual action and propels companies towards positive competition, creating a transparent, accountable platform for global change.

<img src="images/photo1.png" alt="Interactive Globe with controls" width="300"/>
<img src="images/photo2.png" alt="Zoomed in on Brazil. See datapoints" width="300"/>
<img src="images/photo3.png" alt="Geographically linked carbon data" width="300"/>

## Achievements
**Regenerate** secured 2nd place for the most ambitious project at the EarthAI Hackathon!

## Code Overview
Below are the main components of the project:

### Index.html
- HTML file containing code for the user interface and interaction with the Mapbox API.

### api_call.py
- Python script for fetching CO2 emissions data from the World Bank API, processing the data, and predicting future emissions.

### data_transaction_log.csv
- CSV file containing transaction logs for various sectors, including emissions quantity and differences.

## Usage
To run the project locally, follow these steps:
1. Clone the repository to your local machine.
2. Open `index.html` in a web browser to interact with the interface.
3. Ensure Python is installed and execute `api_call.py` to fetch and process CO2 data.

This project was developed during the EarthAI x ClimateImpact summit Hackathon at The Royal Institution.
