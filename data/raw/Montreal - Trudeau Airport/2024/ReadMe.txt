This folder contains continuous data from the National Air Pollution Surveillance (NAPS) program. This folder should contain the following files:
	ReadMe.txt (this file):  Describes the data in the files "data.csv" and "stations.csv".
	data.csv:  Contains hourly average concentrations for the queried pollutants, stations and time period.
	stations.csv:  Contains additional information on the queried stations.
	query.csv:  Summarizes the query used to generate these files.
	
Note:  For additional information on the NAPS program, refer to the "NAPS Ambient Air Monitoring and Quality Assurance/Quality Control (QA/QC) Guidelines": https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf
Note:  To access additional data, including data from the NAPS integrated monitoring program, visit the NAPS Data Query Tool (https://environmental-maps.canada.ca/naps-snpa/) or the NAPS Data Portal (https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en).
Note:  For questions about the data, contact rnspa-napsinfo@ec.gc.ca
Note:  Turning on word wrap in your text editor may make this file easier to read.

------------------------------
"data.csv" column descriptions
------------------------------
Pollutant:
	CO:  Carbon monoxide
	NO2:  Nitrogen dioxide
	NO:  Nitric oxide
	NOX:  Nitrogen oxides (NO + NO2)
	O3:  Ground-level ozone
	PM2.5:  Particulate matter ≤ 2.5 μm
	PM10:  Particulate matter ≤ 10 μm
	SO2:  Sulphur dioxide
NAPS_ID:  6-digit site identification. Additional site information is provided in the file "stations.csv". Note, the terms "site" and "station" are used interchangeably.
Date_yyyy_mm_dd:  Date (yyyy-mm-dd) that the pollutant concentration was measured. Note, software such as Microsoft Excel may display the date in a different format.
Start_Time_Local_Standard:  Start of the hour that the pollutant concentration was measured. Times usually correspond to the local standard time of the site. The Timezone_UTC column in the file "stations.csv" indicates the time zone that data from each site are reported in, and can be used to convert times to UTC.
End_Time_Local_Standard:  End of the hour that the pollutant concentration was measured. Times usually correspond to the local standard time of the site. The Timezone_UTC column in the file "stations.csv" indicates the time zone that data from each site are reported in, and can be used to convert times to UTC.
Concentration:  Pollutant concentration. Zeros are valid. A blank value denotes no data available.
Units:  Units of the pollutant concentration. Data for a specific pollutant are always presented in the same units.
	ppm:  Parts per million (mole fraction)
	ppb:  Parts per billion (mole fraction)
	μm/m3:  Microgram per cubic metre
Method_Code:  Code corresponding to the instrument and method used to measure the pollutant concentration. Method codes are only reported for PM2.5, NO2, NO and NOX. For a description of the methods used to measure other pollutants, refer to the NAPS QA/QC guidelines.

Note:  If a station has no valid concentrations for a specific pollutant in a specific year, then records for that specific station/pollutant/year are not output.
Note:  If a station has at least one valid concentration for a specific pollutant in a specific year, then a continuous timeseries of records for that specific station/pollutant/year is output, with missing or invalid concentrations denoted by a blank value.
Note:  Pollutant concentrations are rounded to 2 decimal places for CO, 1 decimal place for SO2, and 0 decimal places for all other pollutants.
Note:  Due to rounding differences, a small portion of pollutant concentrations may slightly differ between the NAPS Data Query Tool and the NAPS Data Portal.
Note:  Due to instrument noise, negative pollutant concentrations are sometime recorded. Concentrations ≥ -3 and < 0 should be adjusted to 0. Concentrations < -3 should be treated as invalid. For more information, refer to section 12.5.7 of the NAPS QA/QC guidelines.

------------------------------
PM2.5 method code descriptions
------------------------------

Federal Equivalent Method (FEM) instruments
-------------------------------------------
170:  Met One BAM-1020 Beta Attenuation Mass monitor
181:  Thermo Scientific TEOM® 1400a Ambient Particulate Monitor with Series 8500C Filter Dynamics Measurement System
184:  Thermo Scientific 5030 or 5030i SHARP (Synchronized Hybrid Ambient Realtime Particulate) monitor
195:  GRIMM Environmental Dust Monitor model EDM 180
236:  Teledyne Advanced Pollution Instrumentation Model T640 PM mass monitor
636:  Teledyne Advanced Pollution Instrumentation Model T640 PM mass monitor with network data alignment enabled

Non-FEM/pre-FEM instruments
---------------------------
703:  Thermo Scientific TEOM® Series 1400/1400a with sample equilibrium system monitor
706:  Rupprecht & Patashnick TEOM monitor
731:  Met One BAM-1020 Beta Attenuation Mass monitor (prior to 2008)
760:  Thermo Scientific TEOM® 1400a Ambient Particulate Monitor with Series 8500C Filter Dynamics Measurement System (prior to 2010)

Note:  FEM instruments are instruments designated by the United States Environmental Protection Agency (EPA) intended to provide a level of decision making quality for compliance comparable to that provided by Federal Reference Methods (FRMs). For more information, refer to: https://www.epa.gov/amtic/air-monitoring-methods-criteria-pollutants
Note:  To address a consistent positive bias observed in the Teledyne T640 instruments, a mass concentration alignment factor was applied to T640 instruments across Canada. This alignment factor is intended to improve the consistency of PM2.5 measurement with those obtained from the NAPS Reference Method (RM). Environment and Climate Change Canada, along with provincial, territorial and jurisdictional partners of NAPS have agreed to implement this alignment factor for the T640 instruments.
Note:  Non-FEM/Pre-FEM instruments in the NAPS program are instruments that either do not meet the criteria of an FEM or operated prior to their designation as FEMs and their corresponding coding.
Note:  Non-FEM tapered element oscillating microbalance (TEOM) instruments may under report PM2.5 mass concentrations relative to the NAPS PM2.5 Reference Method, since they do not capture the semi-volatile portion of PM2.5 mass. 
Note:  Since 2005, FEM instruments have gradually replaced Non-FEM TEOM instruments.

-----------------------------------
NO2/NO/NOX method code descriptions
-----------------------------------

[BLANK VALUE]:  Chemiluminescence (method code 074, 099 or 249). NO concentrations are determined photometrically by measuring the light intensity from the chemiluminescent reaction of NO mixed with excess O3. The chemiluminescence method detects only NO, so NO2 must first be converted to NO for measurement purposes. Sample flow either is directed through a converter to reduce NO2 to NO, or it bypasses the converter to allow detection of only NO. The sample stream with reduced NO2 is a measurement of NO plus NO2, expressed as NOX. The difference between NOX and NO detection is calculated as the NO2 concentration.
Direct:  Direct measurement. Indicates values measured using direct NO2 instrumentation such as cavity attenuated phase shift (CAPS; method code 256). CAPS uses gas phase titration (GPT) to convert NO into NO2 for direct measurement of NOX. NO is calculated as NOX – NO2 = NO.

----------------------------------
"stations.csv" column descriptions
----------------------------------

Station information
-------------------
NAPS_ID:  6-digit site identification. The first two digits identify the province or territory. Site IDs are assigned by Environment and Climate Change Canada (ECCC) in no particular order.
Station_Name:  Common name given to the site by the Province or Territory.
Status:	 Indicates whether the station was active (1) or inactive (0) in the current Station List year.
Location_Address:  Street address or location.
City:  Municipality or place name.
Province/Territory_EN:  Province or territory in English.
Province/Territory_FR:  Province or territory in French.
Postal_Code:  6-digit alphanumeric postal code.
Timezone_UTC:  Time zone relative to Coordinated Universal Time (UTC) that data from the station are reported in. Data are usually reported in local standard time; however, there are exceptions since some provinces or territories that span multiple time zones choose to use a single time zone for reporting data. UTC is the primary time standard by which the world regulates clocks and time.
Latitude:  Latitude is a geographic coordinate that specifies the north–south position of a point on the Earth's surface.
Longitude:  Longitude is a geographic coordinate that specifies the east–west position of a point on the Earth's surface.
Elevation_m:  Elevation of the monitoring station at ground level above sea level in metres.
Start_Date_Station_yyyy_mm_dd:  Date (yyyy-mm-dd) when monitoring began at the site. Note: some measurement parameters may have been added or removed after this date.
End_Date_Station_yyyy_mm_dd:  Date (yyyy-mm-dd) when monitoring ended at the site. Note: some measurement parameters may have been removed before this date. No value indicates that monitoring is ongoing as of the most recent data publication year.
Combined_Stations:  The site IDs associated with a station that has moved locations. Data from these sites may be combined for trend analysis. Site combinations are determined in collaboration with provinces and territories. Factors such as proximity, elevation, inlet height and station classification are considered when determining if two sites can be combined for trend analysis.
Inlet_Height_m:  Height of the inlet probe above ground level in metres. Unless stated otherwise, the inlet height applies to all pollutants measured at the station.
Network:  Site identified in the most recent version of a Provincial or Territorial Annex to the NAPS Memorandum of Understanding, indicated by "N". Ozone sites operated by ECCC's Canadian Air and Precipitation Monitoring Network (CAPMoN) are indicated by the "C".

Pollutants measured (An X indicates that the station has at least one data record for the pollutant. It does not necessarily mean that monitoring of the pollutant at the station is ongoing.)
-------------------
SO2:  Sulphur dioxide
CO:  Carbon monoxide
NO2:  Nitrogen dioxide
NO: Nitric oxide
NOX:  Nitrogen oxides (NO + NO2)
O3:  Ground-level ozone
PM2.5_Continuous:  Particulate matter less than 2.5 microns via continuous monitoring.
PM10_Continuous:  Particulate matter less than 10 microns via continuous monitoring.
PM2.5_RM:  Particulate matter less than 2.5 microns (NAPS reference (gravimetric) method) via integrated monitoring.
PM10_Integrated:  Particulate matter less than 10 microns via integrated monitoring.
PM2.5-10:  Coarse particulate matter less than 10 microns and greater than 2.5 microns via integrated monitoring. 
PM2.5_Speciation:  Fine particulate matter less than 2.5 microns (chemical constituents) and volatile inorganic compounds via integrated monitoring.
VOC:  Volatile organic compounds via integrated (canister) monitoring.
Carbonyl:  Aldehydes and ketones via integrated monitoring.
PAC:  Polycyclic aromatic compounds via integrated monitoring.

Station classification
----------------------
Site_Type:  Characterizes sites in terms of source influences.
	PE Site_Type:  General Population Exposure - site located in an urban area where populations live, work, shop, play, and that are not classified as transportation or point sources.
	RB Site_Type:  Regional Backgrounds - site outside urban area.
	T Site_Type:  Transportation source–influenced - site within 100 m of a major road or influenced by off-road vehicles and engines, rail, marine or aviation sources located in an urban area.
	PS Site_Type:  Point source–influenced - site located in a populated area, near (< ~10 km) a major stationary emissions source (>= 1 kt per year); classification based on VOC and SO2 ambient measurement data.
Urbanization:  The degree of urbanization around the monitoring site. Population centre (PC) classification (Statistics Canada 2017a, Dictionary) is used to define levels of urbanization.
	LU Urbanization:  Large Urban Area - large population centre (population ≥ 100,000)
	MU Urbanization:  Medium Urban Area - medium population centre (population between 30,000 and 99,999)
	SU Urbanization:  Small Urban Area - small population centre (population between 1,000 and 29,999)
	NU Urbanization:  Non-Urban (Rural) Area - non-urban area (population < 1,000)
Neighbourhood:  The size of residential populations residing within 4 km of NAPS monitoring sites. A distance of 4 km represents the maximum distance associated with a neighbourhood scale of spatial representativeness.
	P1 Neighbourhood:  Neighbourhood population < 500
	P2 Neighbourhood:  Neighbourhood population 500–9,999 
	P3 Neighbourhood:  Neighbourhood population 10,000–49,999
	P4 Neighbourhood:  Neighbourhood population 50,000–99,999
	P5 Neighbourhood:  Neighbourhood population 100,000–149,999
	P6 Neighbourhood:  Neighbourhood population ≥ 150,000
Land_Use:  Represents the dominant land use category within a 400 m radius around each site. A radius of 400 m represents the middle scale of spatial representativeness.
	R Land_Use:  Residential
	C Land_Use:  Commercial
	I Land_Use:  Industrial
	P Land_Use:  Parks
	W Land_Use:  Water
	A Land_Use:  Agriculture
	F Land_Use:  Forested
	O Land_Use:  Open
Scale:  The spatial scale of representativeness the air sample with the scale most appropriate for the monitoring objective at the site.
	MI Scale:  Micro - Concentrations in air typical of areas ranging from several metres up to approximately 100 m.
	M Scale:  Middle - Concentrations in air typical of areas up to several city blocks ranging from about 100 m to 0.5 km.
	N Scale:  Neighbourhood - Concentrations in air typical of some extended area of the city that has relatively uniform land use on the order of 0.5-4 km.
	U Scale:  Urban - Concentrations in air typical of the overall city-wide area on the order of 4-50 km.
	R Scale:  Regional - usually a non-urban area of reasonably homogenous geography that may extend from tens to hundreds of kilometers (U.S. EPA, 1997).
PC:  Population Centre
CD:  Census Division
CSD:  Census Subdivision
CMA/CA:  Census Metropolitan Area/Census Agglomeration
AQMS_Airzone:  Air Quality Management System - Provincial/Territorial Air Zone
Core_Site:  Core sites include a comprehensive set of measurements at a select number of representative locations across Canada that addresses multiple monitoring objectives. Tier (T)1 core sites are based on the PM2.5 speciation sampling sites. Tier (T)2 sites have NAPS PM2.5 reference method (gravimetric) samplers.

Note:  This file gets filtered to only show stations that have records in the file "data.csv". The full list of NAPS stations is available on the NAPS Data Portal: https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=en

---------------------------
"stations.csv" data sources
---------------------------
Please refer to the NAPS QA/QC Guidelines for information on how classifications are determined: https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf
Each classification is derived from the following data sources

Census Division:  Census Division Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Census Subdivision:  Census Subdivision Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Census Metropolitan Area/Census Agglomeration:  Census Metropolitan Area/Census Agglomeration Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Population Centre:  Population Centre Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Urbanization:  Population Centre Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Urbanization:  Population Centre Population Data (https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E)
Neighbourhood:  Dissemination Block Boundaries (https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?Year=21)
Neighbourhood:  Dissemination Block Population Data (https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E)
Land Use Land Cover:  Open Street Map Data (https://download.geofabrik.de/north-america/canada.html)
Land Use Land Cover:  Sentinel-2 10m (https://www.arcgis.com/apps/instant/media/index.html?appid=fc92d38533d440078f17678ebc20e8e2)
Site_Type:  NPRI Data (https://open.canada.ca/data/en/dataset/1fb7d8d4-7713-4ec6-b957-4a882a84fed3)
Site_Type:  NAPS QA/QC Data (https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf)
Scale:  NAPS QA/QC Data (https://ccme.ca/en/res/ambientairmonitoringandqa-qcguidelines_ensecure.pdf)

----------------------------
"query.csv" file description
----------------------------
Query Date:  Date (yyyy-mm-dd) that the data were downloaded from the NAPS Data Query Tool.
Date of Last Data Publication:  Date (yyyy-mm-dd) when continuous data were most recently updated in the NAPS Data Query Tool. Updates may include both publication of new data and corrections to existing data, if issues were discovered.
Database:  Indicates whether data were queried from the continuous or integrated database.
Pollutants:  Pollutants that data were queried for.
Province/Territory:  Provinces and territories that data were queried for.
City/Town:  Cities and towns that data were queried for.
Station:  Stations that data were queried for.
Time period:  Date range (yyyy-mm-dd) that data were queried for.
Number of Records:  Number of records returned by the query.

Note:  This file summarizes the query differently than the "Summary of query and results" section of the NAPS Data Query Tool. The "Summary of query and results" section displays the time period and locations exactly as they were entered using the filters. This file filters the time period and locations to display only what the query returned data records for. For example, if Manitoba and Nunavut were both selected in the province/territory filter, but data are only available for Manitoba, this file will display only Manitoba.