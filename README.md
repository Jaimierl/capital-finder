# Countries and Capitals

## API

This app contains a serverless function that handles two kinds of queries:

A GET http request with a given country name that responds with a string with the form The capital of X is Y

E.g./capital-finder?country=Gabon should generate an http response of The capital of Gabon is Libreville.

A GET http request with a given capital that responds with a string with the form The capital of X is Y

E.g./capital-finder?capital=Muscat should generate an http response of Muscat is the capital of Oman.
