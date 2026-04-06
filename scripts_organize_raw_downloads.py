from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile
import shutil

BASE_DIR = Path('/home/ubuntu/eddy-patagonia-chile')
RAW_DIR = BASE_DIR / 'data' / 'raw'

TARGET_ZIPS = {
    'CL-SDF': RAW_DIR / 'AMF_CL-SDF_FLUXNET_2014-2021_v1.3_r1.zip',
    'CL-SDP': RAW_DIR / 'AMF_CL-SDP_FLUXNET_2014-2021_v1.3_r1.zip',
    'CL-ACF': RAW_DIR / 'AMF_CL-ACF_FLUXNET_2018-2020_v1.3_r1.zip',
    'AR-TF1': RAW_DIR / 'AMF_AR-TF1_FLUXNET_2016-2018_v1.3_r1.zip',
    'AR-TF2': RAW_DIR / 'AMF_AR-TF2_FLUXNET_2016-2018_v1.3_r1.zip',
    'AR-CCg': RAW_DIR / 'AMF_AR-CCg_FLUXNET_2018-2024_v1.3_r1.zip',
}


def pick_member(names: list[str], token: str) -> str:
    for name in names:
        if token in name and name.endswith('.csv'):
            return name
    raise FileNotFoundError(f'No member matching {token} was found inside ZIP archive.')



def ensure_original_copy(site_id: str, zip_path: Path) -> Path:
    site_raw_dir = RAW_DIR / site_id
    site_raw_dir.mkdir(parents=True, exist_ok=True)
    destination = site_raw_dir / zip_path.name
    if not destination.exists():
        shutil.copy2(zip_path, destination)
    return destination



def extract_selected_members(zip_copy_path: Path, site_id: str) -> None:
    site_raw_dir = RAW_DIR / site_id
    with ZipFile(zip_copy_path) as zf:
        names = zf.namelist()
        selected = [
            pick_member(names, '_FLUXMET_DD_'),
            pick_member(names, '_BIF_'),
            pick_member(names, '_BIFVARINFO_DD_'),
        ]
        text_members = [name for name in names if name in {'README.txt', 'DATA_POLICY_LICENSE_AND_INSTRUCTIONS.txt'}]
        selected.extend(text_members)
        for member in selected:
            output_path = site_raw_dir / Path(member).name
            if not output_path.exists():
                with zf.open(member) as src, open(output_path, 'wb') as dst:
                    dst.write(src.read())



def main() -> None:
    for site_id, zip_path in TARGET_ZIPS.items():
        if not zip_path.exists():
            continue
        zip_copy = ensure_original_copy(site_id, zip_path)
        extract_selected_members(zip_copy, site_id)


if __name__ == '__main__':
    main()
