from __future__ import annotations

from pathlib import Path
import pandas as pd

BASE_DIR = Path('/home/ubuntu/eddy-patagonia-chile')
RESEARCH_DIR = BASE_DIR / 'research'
METADATA_DIR = BASE_DIR / 'data' / 'metadata'
OUTPUTS_TABLES_DIR = BASE_DIR / 'outputs' / 'tables'

TARGET_SITES = {
    'CL-SDF': {
        'country': 'Chile',
        'region_scope': 'Chiloé Island, Northern Patagonia / temperate rainforest region',
        'ecosystem_note': 'Old-growth North Patagonian rainforest',
        'access_type': 'open',
        'access_method': 'fluxnet-shuttle + AmeriFlux/FLUXNET product link',
    },
    'CL-SDP': {
        'country': 'Chile',
        'region_scope': 'Chiloé Island, Northern Patagonia / peatland region',
        'ecosystem_note': 'Peatland / wetland',
        'access_type': 'open',
        'access_method': 'fluxnet-shuttle + AmeriFlux/FLUXNET product link',
    },
    'CL-ACF': {
        'country': 'Chile',
        'region_scope': 'Alerce Costero, southern Chile',
        'ecosystem_note': 'Temperate forest',
        'access_type': 'open',
        'access_method': 'fluxnet-shuttle + AmeriFlux/FLUXNET product link',
    },
    'AR-TF1': {
        'country': 'Argentina',
        'region_scope': 'Tierra del Fuego / Southern Patagonia',
        'ecosystem_note': 'Bog / wetland',
        'access_type': 'open',
        'access_method': 'fluxnet-shuttle + AmeriFlux/FLUXNET product link',
    },
    'AR-TF2': {
        'country': 'Argentina',
        'region_scope': 'Tierra del Fuego / Southern Patagonia',
        'ecosystem_note': 'Bog / wetland',
        'access_type': 'open',
        'access_method': 'fluxnet-shuttle + AmeriFlux/FLUXNET product link',
    },
    'AR-CCg': {
        'country': 'Argentina',
        'region_scope': 'Argentina, included as regional comparator outside core Patagonia',
        'ecosystem_note': 'Grassland',
        'access_type': 'open',
        'access_method': 'fluxnet-shuttle + AmeriFlux/FLUXNET product link',
    },
}

IGBP_TO_BIOME = {
    'EBF': 'Evergreen Broadleaf Forest',
    'ENF': 'Evergreen Needleleaf Forest',
    'WET': 'Wetland',
    'GRA': 'Grassland',
}


def load_snapshot() -> pd.DataFrame:
    files = sorted(RESEARCH_DIR.glob('fluxnet_shuttle_snapshot_*.csv'))
    if not files:
        raise FileNotFoundError('No fluxnet-shuttle snapshot found in research/.')
    return pd.read_csv(files[-1])



def build_station_metadata(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['site_id'].isin(TARGET_SITES.keys())].copy()
    df['country'] = df['site_id'].map(lambda s: TARGET_SITES[s]['country'])
    df['regional_scope'] = df['site_id'].map(lambda s: TARGET_SITES[s]['region_scope'])
    df['ecosystem_biome'] = df['igbp'].map(IGBP_TO_BIOME).fillna(df['igbp'])
    df['ecosystem_note'] = df['site_id'].map(lambda s: TARGET_SITES[s]['ecosystem_note'])
    df['temporal_period_available'] = df['first_year'].astype('Int64').astype(str) + '-' + df['last_year'].astype('Int64').astype(str)
    df['download_availability'] = df['download_link'].notna().map({True: 'available', False: 'unknown'})
    df['access_type'] = df['site_id'].map(lambda s: TARGET_SITES[s]['access_type'])
    df['access_method'] = df['site_id'].map(lambda s: TARGET_SITES[s]['access_method'])
    df['official_validation_source'] = df['product_citation'].fillna('AmeriFlux / FLUXNET metadata via fluxnet-shuttle')

    cols = [
        'site_id', 'site_name', 'country', 'regional_scope', 'location_lat', 'location_long',
        'igbp', 'ecosystem_biome', 'ecosystem_note', 'network', 'first_year', 'last_year',
        'temporal_period_available', 'download_availability', 'access_type', 'access_method',
        'download_link', 'fluxnet_product_name', 'product_id', 'oneflux_code_version',
        'official_validation_source'
    ]
    return df[cols].sort_values(['country', 'site_id']).reset_index(drop=True)



def build_download_log(stations: pd.DataFrame) -> pd.DataFrame:
    log = stations[[
        'site_id', 'site_name', 'network', 'download_link', 'access_type', 'access_method'
    ]].copy()
    log['download_status'] = 'pending'
    log['failure_reason'] = ''
    log['notes'] = 'Initial log created from fluxnet-shuttle snapshot.'
    return log[[
        'site_id', 'site_name', 'network', 'access_type', 'access_method',
        'download_status', 'failure_reason', 'download_link', 'notes'
    ]]



def build_variables_placeholder(stations: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for site_id, site_name in stations[['site_id', 'site_name']].itertuples(index=False):
        rows.append({
            'site_id': site_id,
            'site_name': site_name,
            'variables_present': '',
            'standardized_core_variables_present': '',
            'source_file': '',
            'notes': 'To be populated after file download and variable harmonization.'
        })
    return pd.DataFrame(rows)



def build_quality_placeholder(stations: pd.DataFrame) -> pd.DataFrame:
    quality = stations[[
        'site_id', 'site_name', 'country', 'first_year', 'last_year'
    ]].copy()
    quality['total_observations'] = pd.NA
    quality['temporal_coverage_years'] = (quality['last_year'] - quality['first_year'] + 1).astype('Int64')
    quality['valid_nee_pct'] = pd.NA
    quality['valid_gpp_pct'] = pd.NA
    quality['valid_le_pct'] = pd.NA
    quality['valid_h_pct'] = pd.NA
    quality['valid_ta_pct'] = pd.NA
    quality['valid_sw_in_pct'] = pd.NA
    quality['acceptable_qc_pct'] = pd.NA
    quality['variables_available_count'] = pd.NA
    quality['utility_score'] = pd.NA
    quality['quality_class'] = 'pending'
    quality['notes'] = 'Template created before data download and harmonization.'
    return quality



def main() -> None:
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_TABLES_DIR.mkdir(parents=True, exist_ok=True)

    snapshot = load_snapshot()
    stations = build_station_metadata(snapshot)
    download_log = build_download_log(stations)
    variables = build_variables_placeholder(stations)
    quality = build_quality_placeholder(stations)

    stations.to_csv(BASE_DIR / 'stations_metadata.csv', index=False)
    download_log.to_csv(BASE_DIR / 'download_log.csv', index=False)
    variables.to_csv(BASE_DIR / 'variables_by_station.csv', index=False)
    quality.to_csv(BASE_DIR / 'stations_quality.csv', index=False)

    stations.to_csv(METADATA_DIR / 'stations_metadata.csv', index=False)
    download_log.to_csv(METADATA_DIR / 'download_log.csv', index=False)
    variables.to_csv(METADATA_DIR / 'variables_by_station.csv', index=False)
    quality.to_csv(METADATA_DIR / 'stations_quality.csv', index=False)

    stations.to_csv(OUTPUTS_TABLES_DIR / 'stations_metadata.csv', index=False)
    download_log.to_csv(OUTPUTS_TABLES_DIR / 'download_log.csv', index=False)
    variables.to_csv(OUTPUTS_TABLES_DIR / 'variables_by_station.csv', index=False)
    quality.to_csv(OUTPUTS_TABLES_DIR / 'stations_quality.csv', index=False)

    summary = pd.DataFrame([
        {'metric': 'n_stations', 'value': len(stations)},
        {'metric': 'n_chile', 'value': int((stations['country'] == 'Chile').sum())},
        {'metric': 'n_argentina', 'value': int((stations['country'] == 'Argentina').sum())},
        {'metric': 'source', 'value': 'AmeriFlux/FLUXNET metadata via fluxnet-shuttle'},
    ])
    summary.to_csv(OUTPUTS_TABLES_DIR / 'metadata_summary.csv', index=False)


if __name__ == '__main__':
    main()
