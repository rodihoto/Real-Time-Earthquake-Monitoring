{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5b4a1e1-ee23-472e-8b94-d4502d30a8cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.express as px\n",
    "import pandas as pd\n",
    "import requests\n",
    "\n",
    "# Fetch earthquake data from the USGS API\n",
    "url = \"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson\"\n",
    "response = requests.get(url)\n",
    "data = response.json()\n",
    "\n",
    "# Parse the data into a DataFrame\n",
    "earthquakes = {\n",
    "    \"latitude\": [],\n",
    "    \"longitude\": [],\n",
    "    \"magnitude\": [],\n",
    "    \"place\": []\n",
    "}\n",
    "\n",
    "for feature in data['features']:\n",
    "    coordinates = feature['geometry']['coordinates']\n",
    "    properties = feature['properties']\n",
    "    magnitude = properties['mag']\n",
    "    \n",
    "    # Only add the earthquake if the magnitude is non-negative\n",
    "    if magnitude is not None and magnitude >= 0:\n",
    "        earthquakes['latitude'].append(coordinates[1])\n",
    "        earthquakes['longitude'].append(coordinates[0])\n",
    "        earthquakes['magnitude'].append(magnitude)\n",
    "        earthquakes['place'].append(properties['place'])\n",
    "\n",
    "df = pd.DataFrame(earthquakes)\n",
    "\n",
    "# Create an interactive map\n",
    "fig = px.scatter_geo(\n",
    "    df,\n",
    "    lat='latitude',\n",
    "    lon='longitude',\n",
    "    hover_name='place',\n",
    "    size='magnitude',\n",
    "    size_max=20,\n",
    "    color='magnitude',\n",
    "    color_continuous_scale=px.colors.sequential.Plasma,\n",
    "    projection=\"natural earth\",\n",
    "    title=\"Real-Time-Earthquake-Locations\"\n",
    ")\n",
    "\n",
    "fig.show()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    data = fetch_earthquake_data()\n",
    "    df = parse_earthquake_data(data)\n",
    "    create_visualization(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c448567-3b82-4362-b1b1-572836d3720b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
