from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


districts_url = "http://inspire.misoportal.com/geoserver/sandwell_metropolitan_borough_council_polling_districts_polygon/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=sandwell_metropolitan_borough_council_polling_districts_polygon"
council_id = 'E08000028'


districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
