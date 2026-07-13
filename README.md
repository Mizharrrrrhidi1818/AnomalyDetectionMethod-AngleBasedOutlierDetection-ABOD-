# 🍷 Wine Anomaly Detection with ABOD

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![UCI Dataset](https://img.shields.io/badge/dataset-UCI-orange.svg)](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)

Angle-Based Outlier Detection (ABOD) applied to the UCI Wine Quality dataset to identify chemically anomalous wine samples in an unsupervised manner.

## 🎯 Objective
Identify wine samples with unusual physicochemical properties (e.g., acidity, alcohol, sulphates) using ABOD, without relying on quality labels during training. Results are interpreted post-hoc using PCA visualization and statistical analysis.

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/wine-abod-anomaly-detection.git
cd wine-abod-anomaly-detection

# Install dependencies
pip install -r requirements.txt
