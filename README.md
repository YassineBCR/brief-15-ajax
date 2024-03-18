# AJAX Clustering is magic !

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Backend Documentation](#backend-documentation)
   1. [Key Features](#key-features-backend)
   2. [Data Validation](#data-validation)
   3. [Endpoints](#endpoints-backend)
   4. [Running the backend](#running-the-backend)
4. [Front Documentation](#front-documentation)
   1. [Key Features](#key-features)
   2. [Running the model's api](#running-the-model-api)

## Description

The AJAX is an application designed to announce the best clustering model to be used for a database. Here we use an existing databse about consumers.
Many models of clustering exists but we have chosen 3 relevant one :

- Kmeans
- Hierarchical
- DBscan
  We have also decided to use only one score result (which is not the most relevant for DBScan) => the silhouette score

## Installation

To install the requirements, follow these steps:

1. Clone the repository: `git clone git@github.com:luciepienne/b15_cluster_ajax.git`
2. Install the requirements using `pip install -r requirements.txt` in back repository

## Backend Documentation

This backend is implemented using FastAPI and integrates the datacleaning of the original database. It serves various endpoints for handling different score results of each models of clustering.

### Key Features

- silhouette scores of pre detremined parameters of each clustering models

### Data Validation

- The list of models is not free of choices. It has been pre selected and the filter remains unic.

### Endpoints

See API_spec.md for details.

### Running the backend

- Configured to run locally, accessible via port `8000`.
- `cd back`
- run `python api_models.py`

## Front Documentation

This front end is basic.
-json file for script AJAX => app.js
-webpage for UI

### Key Features

- Filter for chosing the model.
- Running the prediction and scoring.

### Running the model api

- Configured to run locally, accessible via port `8001`.
- `cd front`
- run `python -m server 8001`
