rm table.csv; scrapy crawl quotes -o table.csv
rm next.csv; scrapy crawl next -o next.csv
python predict.py

