# Hallazgos iniciales de investigación

La validación programática inicial confirmó que `fluxnet-shuttle` puede instalarse de forma reproducible desde GitHub mediante `pip install git+https://github.com/fluxnet/shuttle.git`. La herramienta quedó disponible como comando de línea `fluxnet-shuttle` y expone tres operaciones principales: `listall`, `download` y `listdatahubs`.

En la inspección de `listdatahubs`, se verificó soporte para **AmeriFlux**, **ICOS** y **TERN**. Para el alcance sudamericano de este proyecto, **AmeriFlux** es la fuente prioritaria y operacionalmente más relevante en la etapa inicial.

Se generó un inventario reproducible con `fluxnet-shuttle listall ameriflux`, que produjo un archivo CSV de snapshot con metadatos y enlaces de descarga para productos disponibles. En ese inventario quedaron confirmadas las estaciones semilla del proyecto:

| site_id | nombre oficial | latitud | longitud | IGBP | red | primer año | último año | producto FLUXNET |
|---|---|---:|---:|---|---|---:|---:|---|
| CL-SDF | Senda Darwin Forest | -41.8830 | -73.6760 | EBF | AmeriFlux | 2014 | 2021 | AMF_CL-SDF_FLUXNET_2014-2021_v1.3_r1.zip |
| CL-SDP | Senda Darwin Peatland | -41.8790 | -73.6660 | WET | AmeriFlux | 2014 | 2021 | AMF_CL-SDP_FLUXNET_2014-2021_v1.3_r1.zip |
| CL-ACF | Alerce Costero Forest | -40.1726 | -73.4439 | ENF | AmeriFlux | 2018 | 2020 | AMF_CL-ACF_FLUXNET_2018-2020_v1.3_r1.zip |

Estos resultados son consistentes con los identificadores oficiales devueltos por la infraestructura de AmeriFlux y constituyen una base suficiente para avanzar a la construcción del repositorio reproducible. También se observó que algunos accesos web directos a páginas de Berkeley Lab pueden quedar bloqueados por Cloudflare desde navegador, por lo que el método preferente para este proyecto será el acceso programático reproducible mediante `fluxnet-shuttle`, complementado con referencias DOI y registros oficiales disponibles en resultados de búsqueda.

Como implicancia metodológica, el proyecto documentará claramente que la validación oficial puede provenir de una combinación de: metadatos recuperados por `fluxnet-shuttle`, títulos y DOI oficiales de AmeriFlux/FLUXNET, y cualquier endpoint o recurso público accesible sin eludir autenticación, licencia ni restricciones de acceso.
