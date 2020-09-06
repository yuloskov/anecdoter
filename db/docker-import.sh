mongoimport --db=db --collection=jokes --file=/jokes.csv
echo 'db.jokes.createIndex({ joke: "text" })' | mongo db
