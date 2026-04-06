# Source Notes for README Phase

## Verified source: FLUXNET Shuttle GitHub repository

Source URL: https://github.com/fluxnet/shuttle

Key points confirmed from the public repository page:

- FLUXNET Shuttle is described as a Python library to discover and download global FLUXNET data from multiple data hubs, including **AmeriFlux**, **ICOS**, and **TERN**.
- The repository documents a command-line interface named `fluxnet-shuttle`.
- The documented workflow includes `listall` to create a metadata snapshot and `download` to retrieve selected site products from that snapshot.
- The repository explicitly documents `--quiet` as a way to skip optional user-information prompts and confirmation prompts when downloading all sites from a snapshot.
- The repository states that FLUXNET data are shared under a **CC-BY-4.0** data use license and points users to the license document included inside downloaded FLUXNET product archives.

## Verified source: data license bundled with downloaded FLUXNET products

Local file used:
`/home/ubuntu/eddy-patagonia-chile/data/raw/CL-SDF/DATA_POLICY_LICENSE_AND_INSTRUCTIONS.txt`

Key points confirmed from the bundled license document:

- The FLUXNET data product is distributed under **CC-BY-4.0**.
- Attribution is required for every use.
- Each site used must be cited individually.
- A global FLUXNET acknowledgment text is required.
- For AmeriFlux data, an additional acknowledgment is required indicating support from the U.S. Department of Energy Office of Science.
- The document recommends citing the ONEFlux / FLUXNET2015 processing paper by Pastorello et al. (2020).
- The document explains that data availability statements should identify the source interface or tool used for access and the download date.

## Verified source limitation: AmeriFlux data policy webpage

Attempted URL: https://ameriflux.lbl.gov/data/data-policy/

Observation:

- Direct access from the browser session was blocked by a **Berkeley Lab Cloudflare WAF Action** page.
- Because the official webpage could not be accessed directly in-session, the README should rely on the bundled FLUXNET license file for authoritative attribution wording, while also citing the AmeriFlux data policy URL as a relevant official source.

## Implication for project documentation

The README can safely state that:

1. The operational pipeline used `fluxnet-shuttle` as the reproducible discovery/download client.
2. The legal and attribution requirements were taken from the license text packaged with the downloaded FLUXNET archives.
3. The project must preserve site-level attribution and network-level acknowledgment for any reuse of the downloaded data products.
