// Design reminder: regional scientific editorialism with cartographic modernism.
// Keep data presentation traceable, elegant, and publication-oriented.

export type StationRecord = {
  siteId: string;
  siteName: string;
  country: string;
  regionalScope: string;
  ecosystem: string;
  network: string;
  lat: number;
  lon: number;
  yearStart: number;
  yearEnd: number;
  coverageYears: number;
  observations: number;
  validNeePct: number;
  validGppPct: number;
  validLePct: number;
  validHPct: number;
  validTaPct: number;
  validSwInPct: number;
  acceptableQcPct: number;
  variablesAvailableCount: number;
  utilityScore: number;
  qualityClass: string;
  qualityColor: string;
  markerRadius: number;
  variablesPresent: string[];
  productId: string;
  notes: string;
};

export type ProjectStats = {
  stationCount: number;
  countryCount: number;
  networkCount: number;
  yearMin: number;
  yearMax: number;
  observationSum: number;
  highQualityCount: number;
  mediumQualityCount: number;
  lowQualityCount: number;
  meanUtilityScore: number;
  topSiteId: string;
};

export const stationData: StationRecord[] = [
  {
    "siteId": "CL-SDP",
    "siteName": "Senda Darwin Peatland",
    "country": "Chile",
    "regionalScope": "Chiloé Island, Northern Patagonia / peatland region",
    "ecosystem": "Peatland / wetland",
    "network": "AmeriFlux",
    "lat": -41.879,
    "lon": -73.666,
    "yearStart": 2014,
    "yearEnd": 2021,
    "coverageYears": 8,
    "observations": 2922,
    "validNeePct": 99.66,
    "validGppPct": 99.66,
    "validLePct": 99.38,
    "validHPct": 100.0,
    "validTaPct": 100.0,
    "validSwInPct": 92.37,
    "acceptableQcPct": 82.2,
    "variablesAvailableCount": 6,
    "utilityScore": 0.902,
    "qualityClass": "high",
    "qualityColor": "#2F6B3B",
    "markerRadius": 16.0,
    "variablesPresent": [
      "NEE",
      "GPP",
      "LE",
      "H",
      "TA",
      "SW_IN"
    ],
    "productId": "10.17190/AMF/2571108",
    "notes": "Daily FLUXMET standardized from FLUXNET product. Missing sentinels converted to NaN. QC acceptable threshold set to >= 0.5 for available QC variables."
  },
  {
    "siteId": "CL-SDF",
    "siteName": "Senda Darwin Forest",
    "country": "Chile",
    "regionalScope": "Chiloé Island, Northern Patagonia / temperate rainforest region",
    "ecosystem": "Old-growth North Patagonian rainforest",
    "network": "AmeriFlux",
    "lat": -41.883,
    "lon": -73.676,
    "yearStart": 2014,
    "yearEnd": 2021,
    "coverageYears": 8,
    "observations": 2922,
    "validNeePct": 94.32,
    "validGppPct": 94.32,
    "validLePct": 96.0,
    "validHPct": 96.0,
    "validTaPct": 100.0,
    "validSwInPct": 92.33,
    "acceptableQcPct": 78.78,
    "variablesAvailableCount": 6,
    "utilityScore": 0.886,
    "qualityClass": "high",
    "qualityColor": "#2F6B3B",
    "markerRadius": 16.0,
    "variablesPresent": [
      "NEE",
      "GPP",
      "LE",
      "H",
      "TA",
      "SW_IN"
    ],
    "productId": "10.17190/AMF/2469441",
    "notes": "Daily FLUXMET standardized from FLUXNET product. Missing sentinels converted to NaN. QC acceptable threshold set to >= 0.5 for available QC variables."
  },
  {
    "siteId": "AR-CCg",
    "siteName": "Carlos Casares grassland",
    "country": "Argentina",
    "regionalScope": "Argentina, included as regional comparator outside core Patagonia",
    "ecosystem": "Grassland",
    "network": "AmeriFlux",
    "lat": -35.9244,
    "lon": -61.1855,
    "yearStart": 2018,
    "yearEnd": 2024,
    "coverageYears": 7,
    "observations": 2557,
    "validNeePct": 85.8,
    "validGppPct": 85.8,
    "validLePct": 84.0,
    "validHPct": 87.17,
    "validTaPct": 100.0,
    "validSwInPct": 100.0,
    "acceptableQcPct": 74.14,
    "variablesAvailableCount": 6,
    "utilityScore": 0.837,
    "qualityClass": "high",
    "qualityColor": "#2F6B3B",
    "markerRadius": 14.0,
    "variablesPresent": [
      "NEE",
      "GPP",
      "LE",
      "H",
      "TA",
      "SW_IN"
    ],
    "productId": "10.17190/AMF/2469434",
    "notes": "Daily FLUXMET standardized from FLUXNET product. Missing sentinels converted to NaN. QC acceptable threshold set to >= 0.5 for available QC variables."
  },
  {
    "siteId": "CL-ACF",
    "siteName": "Alerce Costero Forest",
    "country": "Chile",
    "regionalScope": "Alerce Costero, southern Chile",
    "ecosystem": "Temperate forest",
    "network": "AmeriFlux",
    "lat": -40.1726,
    "lon": -73.4439,
    "yearStart": 2018,
    "yearEnd": 2020,
    "coverageYears": 3,
    "observations": 1096,
    "validNeePct": 98.63,
    "validGppPct": 98.63,
    "validLePct": 98.63,
    "validHPct": 98.63,
    "validTaPct": 98.63,
    "validSwInPct": 98.63,
    "acceptableQcPct": 93.05,
    "variablesAvailableCount": 6,
    "utilityScore": 0.804,
    "qualityClass": "high",
    "qualityColor": "#2F6B3B",
    "markerRadius": 6.0,
    "variablesPresent": [
      "NEE",
      "GPP",
      "LE",
      "H",
      "TA",
      "SW_IN"
    ],
    "productId": "10.17190/AMF/2571129",
    "notes": "Daily FLUXMET standardized from FLUXNET product. Missing sentinels converted to NaN. QC acceptable threshold set to >= 0.5 for available QC variables."
  },
  {
    "siteId": "AR-TF1",
    "siteName": "Rio Moat bog",
    "country": "Argentina",
    "regionalScope": "Tierra del Fuego / Southern Patagonia",
    "ecosystem": "Bog / wetland",
    "network": "AmeriFlux",
    "lat": -54.9733,
    "lon": -66.7335,
    "yearStart": 2016,
    "yearEnd": 2018,
    "coverageYears": 3,
    "observations": 1096,
    "validNeePct": 79.29,
    "validGppPct": 79.29,
    "validLePct": 79.29,
    "validHPct": 79.29,
    "validTaPct": 79.01,
    "validSwInPct": 79.11,
    "acceptableQcPct": 75.84,
    "variablesAvailableCount": 6,
    "utilityScore": 0.713,
    "qualityClass": "medium",
    "qualityColor": "#C78C1B",
    "markerRadius": 6.0,
    "variablesPresent": [
      "NEE",
      "GPP",
      "LE",
      "H",
      "TA",
      "SW_IN"
    ],
    "productId": "10.17190/AMF/1818370",
    "notes": "Daily FLUXMET standardized from FLUXNET product. Missing sentinels converted to NaN. QC acceptable threshold set to >= 0.5 for available QC variables."
  },
  {
    "siteId": "AR-TF2",
    "siteName": "Rio Pipo bog",
    "country": "Argentina",
    "regionalScope": "Tierra del Fuego / Southern Patagonia",
    "ecosystem": "Bog / wetland",
    "network": "AmeriFlux",
    "lat": -54.8269,
    "lon": -68.4549,
    "yearStart": 2016,
    "yearEnd": 2018,
    "coverageYears": 3,
    "observations": 1096,
    "validNeePct": 75.91,
    "validGppPct": 75.91,
    "validLePct": 75.91,
    "validHPct": 75.91,
    "validTaPct": 75.55,
    "validSwInPct": 65.78,
    "acceptableQcPct": 66.84,
    "variablesAvailableCount": 6,
    "utilityScore": 0.678,
    "qualityClass": "medium",
    "qualityColor": "#C78C1B",
    "markerRadius": 6.0,
    "variablesPresent": [
      "NEE",
      "GPP",
      "LE",
      "H",
      "TA",
      "SW_IN"
    ],
    "productId": "10.17190/AMF/2571120",
    "notes": "Daily FLUXMET standardized from FLUXNET product. Missing sentinels converted to NaN. QC acceptable threshold set to >= 0.5 for available QC variables."
  }
] as StationRecord[];

export const projectStats: ProjectStats = {
  "stationCount": 6,
  "countryCount": 2,
  "networkCount": 1,
  "yearMin": 2014,
  "yearMax": 2024,
  "observationSum": 11689,
  "highQualityCount": 4,
  "mediumQualityCount": 2,
  "lowQualityCount": 0,
  "meanUtilityScore": 0.803,
  "topSiteId": "CL-SDP"
} as ProjectStats;

