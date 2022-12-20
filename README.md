# Portland Yearly Neighborhood Offense Statistics


The aim of this project is to collect and visualize Portland, Oregon crime data from 2018 to 2022.

![Portland Yearly Neighborhood Offense Statistics](https://user-images.githubusercontent.com/104397181/208736468-02b4737d-ac0f-4ac9-85a0-7e527c7e75d2.png)


**Link to project**: [PDX Crime](https://public.tableau.com/views/Crime_Visualization_16715528480120/PortlandYearlyNeighborhoodOffenseStatistics?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)


## How It's Made:
**Tech used:** Python, pandas, Tableau

- Crime data is collected from the Portland Police Bureau's [Open Data](https://public.tableau.com/app/profile/portlandpolicebureau/viz/New_Monthly_Neighborhood/MonthlyOffenseTotals)
- Geospatial data for Portland neighborhoods is collected from [Portland Maps](https://gis-pdx.opendata.arcgis.com/datasets/PDX::neighborhoods-regions/explore?location=45.540245%2C-122.627185%2C10.98)
- Python and pandas are used to clean, reformat and concatenate data
- Transformed data and geospatial data are uploaded to Tableau to create an interactive dashboard


## Interactive Dashboard:
**Dashboard**: Interactivity allows the users to filter the information by selecting certain years, months, neighborhoods and crime categories. An overview of the filters is included below.


### Year Filter
The year filter defaults to 'All' which includes 2018, 2019, 2020, 2021 and 2022. The year can be changed by selecting the blank circle next to the chosen year. The text table, monthly bar chart and frequency map will update upon selection.

### Category Filter
The table **Offense Count by Category** provides a listing of the reported frequency of offenses during the selected time period. Additionally, this table works as a filter. Clicking on the name of a particular offense category automatically updates the monthly bar chart and the frequency map to show the distribution and frequency of those crimes. Multiple categories and be selected by holding down the COMMAND button and clicking the categories.

### Neighborhood Filter
The frequency map is an outline of all Portland neighborhoods using boundaries from Portland Maps. The map is dynamically updated based on selected filters and years. Darker colors indicate a higher number of reported offenses. By hovering over a polygon on the map, the neighborhood name and number of total offenses is displayed. The map can also be used as a filter by clicking a neighborhood. The text table and the monthly bar chart will be updated based on the selected neighborhood. Multiple neighborhoods can be selected by holding down the COMMAND button and clicking each neighborhood. 

### Month Filter
The **Offense Count by Month** bar chart displays the offense count for all months included in the year filter. The bar chart can also be used to filter results by selecting one or more months to view the offense and regional breakdown for that month. 

**Note:** Different filters can be selected to further refine data. 
