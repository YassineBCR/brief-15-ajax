# API Specification
## Introduction
The API will give the silhouette scores of each clustering models running on a mall_customers database.

## Base URL

host="0.0.0.0", port=8000
you should run port 8001 via

```py
python -m server 8001
```

## Endpoints
1. /kmeans
Description
This endpoint performs k-means clustering on the provided data.

Method
GET

Parameters
None
Response
200 OK: Returns the silhouette score of the k-means clustering as a float.
Example Response:

json
Copy code
{
    "silhouette_score": 0.75
}
500 Internal Server Error: Indicates a server error occurred.

2. /dbscan
Description
This endpoint performs DBSCAN clustering on the provided data.

Method
GET

Parameters
None
Response
200 OK: Returns the silhouette score of the DBSCAN clustering as a float.
Example Response:

json
Copy code
{
    "silhouette_score": 0.68
}
500 Internal Server Error: Indicates a server error occurred.

3. /hierarchical
Description
This endpoint performs hierarchical clustering on the provided data.

Method
GET

Parameters
None
Response
200 OK: Returns the silhouette score of the hierarchical clustering as a float.
Example Response:

json
Copy code
{
    "silhouette_score": 0.82
}
500 Internal Server Error: Indicates a server error occurred.

## Error Handling
Errors are handled in the API, returning error 500 in case the score cannot be given .



## Examples
Filter choice : DBscan 

| Key                | Value  |
|--------------------|--------|
| silhouette_score   | 0.82   |



## Conclusion
The keypoints give only score. An upgrade should be possible by having the possibility to change the parameters of the clustering.

