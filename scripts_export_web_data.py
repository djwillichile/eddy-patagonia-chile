from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path('/home/ubuntu/eddy-patagonia-chile')
SRC = ROOT / 'outputs' / 'tables' / 'station_overview.csv'
DST = ROOT / 'client' / 'src' / 'lib' / 'stationsData.ts'


def _to_native(value):
    if pd.isna(value):
        return None
    if hasattr(value, 'item'):
        try:
            return value.item()
        except Exception:
            return value
    return value


def main() -> None:
    df = pd.read_csv(SRC)

    stations = []
    for _, row in df.sort_values(['utility_score', 'site_id'], ascending=[False, True]).iterrows():
        stations.append(
            {
                'siteId': _to_native(row['site_id']),
                'siteName': _to_native(row['site_name']),
                'country': _to_native(row['country']),
                'regionalScope': _to_native(row['regional_scope']),
                'ecosystem': _to_native(row['ecosystem_note']),
                'network': _to_native(row['network']),
                'lat': float(row['location_lat']),
                'lon': float(row['location_long']),
                'yearStart': int(row['year_start']),
                'yearEnd': int(row['year_end']),
                'coverageYears': int(row['temporal_coverage_years']),
                'observations': int(row['total_observations']),
                'validNeePct': float(row['valid_nee_pct']),
                'validGppPct': float(row['valid_gpp_pct']),
                'validLePct': float(row['valid_le_pct']),
                'validHPct': float(row['valid_h_pct']),
                'validTaPct': float(row['valid_ta_pct']),
                'validSwInPct': float(row['valid_sw_in_pct']),
                'acceptableQcPct': float(row['acceptable_qc_pct']),
                'variablesAvailableCount': int(row['variables_available_count']),
                'utilityScore': float(row['utility_score']),
                'qualityClass': _to_native(row['quality_class']),
                'qualityColor': _to_native(row['quality_color']),
                'markerRadius': float(row['marker_radius']),
                'variablesPresent': [part.strip() for part in str(row['variables_present']).split(',') if part.strip()],
                'productId': _to_native(row['product_id']),
                'notes': _to_native(row['notes']),
            }
        )

    stats = {
        'stationCount': len(stations),
        'countryCount': int(df['country'].nunique()),
        'networkCount': int(df['network'].nunique()),
        'yearMin': int(df['year_start'].min()),
        'yearMax': int(df['year_end'].max()),
        'observationSum': int(df['total_observations'].sum()),
        'highQualityCount': int((df['quality_class'] == 'high').sum()),
        'mediumQualityCount': int((df['quality_class'] == 'medium').sum()),
        'lowQualityCount': int((df['quality_class'] == 'low').sum()),
        'meanUtilityScore': round(float(df['utility_score'].mean()), 3),
        'topSiteId': str(df.sort_values('utility_score', ascending=False).iloc[0]['site_id']),
    }

    module_text = (
        '// Design reminder: regional scientific editorialism with cartographic modernism.\n'
        '// Keep data presentation traceable, elegant, and publication-oriented.\n\n'
        'export type StationRecord = {\n'
        '  siteId: string;\n'
        '  siteName: string;\n'
        '  country: string;\n'
        '  regionalScope: string;\n'
        '  ecosystem: string;\n'
        '  network: string;\n'
        '  lat: number;\n'
        '  lon: number;\n'
        '  yearStart: number;\n'
        '  yearEnd: number;\n'
        '  coverageYears: number;\n'
        '  observations: number;\n'
        '  validNeePct: number;\n'
        '  validGppPct: number;\n'
        '  validLePct: number;\n'
        '  validHPct: number;\n'
        '  validTaPct: number;\n'
        '  validSwInPct: number;\n'
        '  acceptableQcPct: number;\n'
        '  variablesAvailableCount: number;\n'
        '  utilityScore: number;\n'
        '  qualityClass: string;\n'
        '  qualityColor: string;\n'
        '  markerRadius: number;\n'
        '  variablesPresent: string[];\n'
        '  productId: string;\n'
        '  notes: string;\n'
        '};\n\n'
        'export type ProjectStats = {\n'
        '  stationCount: number;\n'
        '  countryCount: number;\n'
        '  networkCount: number;\n'
        '  yearMin: number;\n'
        '  yearMax: number;\n'
        '  observationSum: number;\n'
        '  highQualityCount: number;\n'
        '  mediumQualityCount: number;\n'
        '  lowQualityCount: number;\n'
        '  meanUtilityScore: number;\n'
        '  topSiteId: string;\n'
        '};\n\n'
        f'export const stationData: StationRecord[] = {json.dumps(stations, ensure_ascii=False, indent=2)} as StationRecord[];\n\n'
        f'export const projectStats: ProjectStats = {json.dumps(stats, ensure_ascii=False, indent=2)} as ProjectStats;\n'
    )

    DST.write_text(module_text + '\n', encoding='utf-8')
    print(f'Wrote {DST}')


if __name__ == '__main__':
    main()
