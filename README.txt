1.to run this app you need to have docker launched
2.you need to prepare your .env file with:
    
    DB_HOST=db
    DB_PORT=****
    DB_NAME=****
    DB_USER=****
    DB_PASSWORD=****

3.type <docker compoese up --build> in terminal which must be opened in the same directory where file "docker compose.yml" is.
4.run homesimulator.py