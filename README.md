# 🔱 Bitcoin Trust Network Analysis

## Overview
This project analyzes the Bitcoin Alpha trust-weighted signed network using Gephi. The dataset represents a "who-trusts-whom" network of Bitcoin traders. By performing network analysis and visualizing the graph, we evaluate the trustworthiness of traders to detect fraud and identify reliable sellers.

## Features
- **Network Analysis**: Centrality metrics (degree, betweenness, closeness) calculated for all nodes.
- **Graph Visualization**: Uses Gephi to visualize network topology and distinguish trustworthy traders from fraudulent ones.
- **Color-coded Ratings**: Nodes and edges are color-coded to reflect trust levels (from -10 to +10).
- **IMDB Review Analysis**: Implements text processing and topic modeling on IMDB reviews as an additional analysis.

## 📁 Project Structure
```
bitcoin-trust-network-analysis/
├── code/                      # Code files for the project
│   └── IMDB_reviews.py        # Python script for IMDB review analysis
│
├── data/                      # Dataset files
│   └── BitcoinAlphafinal.gephi # Bitcoin Alpha dataset
│
├── reports/                   # Project documentation
│   └── Report.pdf           # Detailed project report
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview and instructions
```

## 🛠️ Setup Instructions

### Prerequisites
- **Python** (v3.8 or higher)
- **Gephi** for network visualization. Download it from [Gephi.org](https://gephi.org/).

### 1. Install Python Dependencies
Create a virtual environment and install required libraries:
```bash
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### 2. Run the IMDB Review Analysis
The `IMDB_reviews.py` script demonstrates text preprocessing and topic modeling using IMDB reviews:
```bash
python code/IMDB_reviews.py
```

### 3. Analyze the Bitcoin Network
- Open `BitcoinAlphafinal.gephi` in Gephi.
- Follow the steps in the `Report.pdf` to perform centrality analysis and graph visualization.

---

## 🖋️ Results
- **Network Analysis**: Identified fraudulent and trustworthy traders using node centrality and edge ratings.
- **Graph Visualization**: Highlighted communities and major traders using ForceAtlas2 layout.
- **IMDB Analysis**: Preprocessed text, generated word clouds, and performed topic modeling.

---

## 📜 Documentation
- **Report**: Detailed findings and analysis steps are in the `reports/Report_1.pdf`.

---

## 💡 Future Work
- Explore additional datasets to generalize the fraud detection methodology.
- Implement advanced graph analysis using Python libraries like `NetworkX`.

---

## 👩‍💻 Author
**Bita Nasserfarahmand**  
- [Email](mailto:bita.nf@gmail.com)

Feel free to reach out with questions or contributions!
